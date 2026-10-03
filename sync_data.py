import pymysql
import pyodbc
import pandas as pd
from datetime import datetime
import logging
import time
from sqlalchemy import create_engine, text

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sync_log.txt'),
        logging.StreamHandler()
    ]
)

class DataSyncer:
    def __init__(self):
        # MySQL connection config
        self.mysql_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Amir@13511348',
            'database': 'salesoptimizer',
            'charset': 'utf8mb4'
        }
        
        # SQL Server connection string - UPDATE THESE VALUES
        self.sqlserver_conn_str = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=172.16.30.20;'
            'DATABASE=Webpoosh_Sg3;'
            'UID=reports;'
            'PWD=123456789'
        )
        
        # SQLAlchemy engine for SQL Server
        # Format: mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server
        self.sqlserver_engine = create_engine(
            "mssql+pyodbc://reports:123456789@172.16.30.20/Webpoosh_Sg3?driver=ODBC+Driver+17+for+SQL+Server"
        )
        
        self.batch_size = 1000000  
        
    def get_mysql_connection(self):
        return pymysql.connect(**self.mysql_config)
    
    def truncate_tables(self):
        """Truncate local tables before full sync"""
        conn = self.get_mysql_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
                cursor.execute("TRUNCATE TABLE voucher")
                cursor.execute("TRUNCATE TABLE invoiceitems")
                cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
                conn.commit()
                logging.info("Tables truncated successfully")
        finally:
            conn.close()
    
    def sync_voucher(self):
        """Sync voucher table"""
        logging.info("Starting voucher sync...")
        start_time = time.time()
        
        try:
            with self.sqlserver_engine.connect() as sql_conn:
                # Get total count
                count_query = text("SELECT COUNT(*) FROM dbo.BVoucherItemStoreOnly")
                total_rows = pd.read_sql(count_query, sql_conn).iloc[0, 0]
                logging.info(f"Total rows to sync: {total_rows}")
                
                # Query data in batches
                offset = 0
                total_synced = 0
                
                while offset < total_rows:
                    query = text(f"""
                    SELECT 
                        StoreID, Name, 
                        InventoryVoucherID, Number, Tarikh, 
                        PartID, Code, PName, MajorUnitQuantity, InventoryVoucherSpecificationRef
                    FROM dbo.BVoucherItemStoreOnly
                    ORDER BY InventoryVoucherID, PartID
                    OFFSET {offset} ROWS
                    FETCH NEXT {self.batch_size} ROWS ONLY
                    """)
                    
                    df = pd.read_sql(query, sql_conn)
                    
                    if df.empty:
                        break
                    
                    # Convert datetime columns
                    df['Tarikh'] = pd.to_datetime(df['Tarikh'])
                    
                    # Insert into MySQL (excluding auto-increment id column)
                    self.bulk_insert_mysql('voucher', df)
                    
                    total_synced += len(df)
                    offset += self.batch_size
                    progress = (total_synced / total_rows) * 100
                    logging.info(f"Synced {total_synced}/{total_rows} rows for voucher ({progress:.1f}%)")
                
                logging.info(f"Voucher sync completed in {time.time() - start_time:.2f} seconds")
            
        except Exception as e:
            logging.error(f"Error during voucher sync: {e}")
            raise
    
    def sync_invoiceitems(self):
        """Sync invoiceitems table"""
        logging.info("Starting invoiceitems sync...")
        start_time = time.time()
        
        try:
            with self.sqlserver_engine.connect() as sql_conn:
                # Get total count
                count_query = text("SELECT COUNT(*) FROM dbo.BInvoiceItem")
                total_rows = pd.read_sql(count_query, sql_conn).iloc[0, 0]
                logging.info(f"Total rows to sync: {total_rows}")
                
                # Query data in batches
                offset = 0
                total_synced = 0
                
                while offset < total_rows:
                    query = text(f"""
                    SELECT 
                        InvoiceItemID, Expr2, SalesOfficeID, Name, 
                        InvoiceID, Number, PartyID, FullName, 
                        Mobile, PartID, Code, Expr1, MajorUnitQuantity, 
                        Price, ReductionAmount, AdditionAmount, NetPrice, 
                        FirstName, LastName
                    FROM dbo.BInvoiceItem
                    ORDER BY InvoiceItemID
                    OFFSET {offset} ROWS
                    FETCH NEXT {self.batch_size} ROWS ONLY
                    """)
                    
                    df = pd.read_sql(query, sql_conn)
                    
                    if df.empty:
                        break
                    
                    # Convert datetime columns
                    df['Expr2'] = pd.to_datetime(df['Expr2'])
                    
                    # Insert into MySQL (including InvoiceItemID as it's the primary key)
                    self.bulk_insert_mysql_invoiceitems('invoiceitems', df)
                    
                    total_synced += len(df)
                    offset += self.batch_size
                    progress = (total_synced / total_rows) * 100
                    logging.info(f"Synced {total_synced}/{total_rows} rows for invoiceitems ({progress:.1f}%)")
                
                logging.info(f"Invoiceitems sync completed in {time.time() - start_time:.2f} seconds")
            
        except Exception as e:
            logging.error(f"Error during invoiceitems sync: {e}")
            raise
    
    def bulk_insert_mysql(self, table_name, df):
        """Perform bulk insert into MySQL for voucher table"""
        conn = self.get_mysql_connection()
        try:
            with conn.cursor() as cursor:
                # Convert NaN to None for MySQL compatibility
                df = df.where(pd.notnull(df), None)
                
                # Define columns to insert (exclude auto-increment 'id' column)
                columns = [
                    'StoreID', 'Name', 
                    'InventoryVoucherID', 'Number', 'Tarikh', 
                    'PartID', 'Code', 'PName', 'MajorUnitQuantity', 'InventoryVoucherSpecificationRef'
                ]
                
                # Ensure DataFrame has only these columns in correct order
                df = df[columns]
                
                # Build insert query
                placeholders = ', '.join(['%s'] * len(columns))
                query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                
                # Convert DataFrame to list of tuples for executemany
                data = [tuple(row) for row in df.values]
                
                # Execute batch insert
                cursor.executemany(query, data)
                conn.commit()
                logging.debug(f"Inserted {len(df)} rows into {table_name}")
                
        except Exception as e:
            logging.error(f"Bulk insert failed for {table_name}: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()
    
    def bulk_insert_mysql_invoiceitems(self, table_name, df):
        """Perform bulk insert into MySQL for invoiceitems table"""
        conn = self.get_mysql_connection()
        try:
            with conn.cursor() as cursor:
                # Convert NaN to None for MySQL compatibility
                # This is the critical fix - replace NaN with None
                df = df.where(pd.notnull(df), None)
                
                # Additional fix: Ensure numeric columns don't have NaN
                # Convert any remaining NaN in numeric columns to 0 or None
                numeric_columns = ['Price', 'ReductionAmount', 'AdditionAmount', 'NetPrice', 'MajorUnitQuantity']
                for col in numeric_columns:
                    if col in df.columns:
                        # Replace NaN with None (which MySQL interprets as NULL)
                        df[col] = df[col].where(pd.notnull(df[col]), None)
                        # Also replace any infinity values
                        df[col] = df[col].replace([float('inf'), float('-inf')], None)
                
                # Define columns to insert (all columns including InvoiceItemID)
                columns = [
                    'InvoiceItemID', 'Expr2', 'SalesOfficeID', 'Name', 
                    'InvoiceID', 'Number', 'PartyID', 'FullName', 
                    'Mobile', 'PartID', 'Code', 'Expr1', 'MajorUnitQuantity', 
                    'Price', 'ReductionAmount', 'AdditionAmount', 'NetPrice', 
                    'FirstName', 'LastName'
                ]
                
                # Ensure DataFrame has only these columns in correct order
                df = df[columns]
                
                # Build insert query (including InvoiceItemID since it's the primary key)
                placeholders = ', '.join(['%s'] * len(columns))
                query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                
                # Convert DataFrame to list of tuples for executemany
                # This is where we ensure no NaN values remain
                data = []
                for row in df.values:
                    clean_row = []
                    for value in row:
                        # Check if value is NaN or infinite
                        if isinstance(value, float) and (pd.isna(value) or pd.isnull(value)):
                            clean_row.append(None)
                        else:
                            clean_row.append(value)
                    data.append(tuple(clean_row))
                
                # Execute batch insert
                cursor.executemany(query, data)
                conn.commit()
                logging.debug(f"Inserted {len(df)} rows into {table_name}")
                
        except Exception as e:
            logging.error(f"Bulk insert failed for {table_name}: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()
    
    def incremental_sync(self, last_sync_time=None):
        """Perform incremental sync based on timestamp"""
        if last_sync_time is None:
            last_sync_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        logging.info(f"Performing incremental sync from {last_sync_time}")
        
        try:
            with self.sqlserver_engine.connect() as sql_conn:
                # Sync voucher table
                query = text("""
                SELECT 
                    StoreID, Name, 
                    InventoryVoucherID, Number, Tarikh, 
                    PartID, Code, PName, MajorUnitQuantity, InventoryVoucherSpecificationRef
                FROM dbo.BVoucherItemStoreOnly
                WHERE Tarikh > :last_sync_time
                ORDER BY InventoryVoucherID, PartID
                """)
                
                df = pd.read_sql(query, sql_conn, params={'last_sync_time': last_sync_time})
                
                if not df.empty:
                    df['Tarikh'] = pd.to_datetime(df['Tarikh'])
                    self.upsert_mysql('voucher', df)
                    logging.info(f"Upserted {len(df)} rows into voucher")
                
                # Sync invoiceitems table
                query = text("""
                SELECT 
                    InvoiceItemID, Expr2, SalesOfficeID, Name, 
                    InvoiceID, Number, PartyID, FullName, 
                    Mobile, PartID, Code, Expr1, MajorUnitQuantity, 
                    Price, ReductionAmount, AdditionAmount, NetPrice, 
                    FirstName, LastName
                FROM dbo.BInvoiceItem
                WHERE Expr2 > :last_sync_time
                ORDER BY InvoiceItemID
                """)
                
                df = pd.read_sql(query, sql_conn, params={'last_sync_time': last_sync_time})
                
                if not df.empty:
                    df['Expr2'] = pd.to_datetime(df['Expr2'])
                    self.upsert_mysql_invoiceitems('invoiceitems', df)
                    logging.info(f"Upserted {len(df)} rows into invoiceitems")
                
                logging.info(f"Incremental sync completed successfully")
                
        except Exception as e:
            logging.error(f"Incremental sync failed: {e}")
            raise
    
    def upsert_mysql(self, table_name, df):
        """Perform upsert (insert or update) into MySQL for voucher table"""
        conn = self.get_mysql_connection()
        try:
            with conn.cursor() as cursor:
                # Convert NaN to None
                df = df.where(pd.notnull(df), None)
                
                # Define columns (exclude auto-increment 'id')
                columns = [
                    'StoreID', 'Name', 
                    'InventoryVoucherID', 'Number', 'Tarikh', 
                    'PartID', 'Code', 'PName', 'MajorUnitQuantity', 'InventoryVoucherSpecificationRef'
                ]
                
                df = df[columns]
                
                # Build upsert query
                placeholders = ', '.join(['%s'] * len(columns))
                update_clause = ', '.join([
                    f"{col}=VALUES({col})" for col in columns 
                    if col not in ['InventoryVoucherID', 'PartID']
                ])
                
                query = f"""
                INSERT INTO {table_name} ({', '.join(columns)}) 
                VALUES ({placeholders})
                ON DUPLICATE KEY UPDATE {update_clause}
                """
                
                data = [tuple(row) for row in df.values]
                cursor.executemany(query, data)
                conn.commit()
                
        except Exception as e:
            logging.error(f"Upsert failed for {table_name}: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()
    

    def upsert_mysql_invoiceitems(self, table_name, df):
        """Perform upsert (insert or update) into MySQL for invoiceitems table"""
        conn = self.get_mysql_connection()
        try:
            with conn.cursor() as cursor:
                # Convert NaN to None
                df = df.where(pd.notnull(df), None)
                
                # Handle numeric columns with NaN
                numeric_columns = ['Price', 'ReductionAmount', 'AdditionAmount', 'NetPrice', 'MajorUnitQuantity']
                for col in numeric_columns:
                    if col in df.columns:
                        df[col] = df[col].where(pd.notnull(df[col]), None)
                        df[col] = df[col].replace([float('inf'), float('-inf')], None)
                
                # Define columns (all columns including InvoiceItemID)
                columns = [
                    'InvoiceItemID', 'Expr2', 'SalesOfficeID', 'Name', 
                    'InvoiceID', 'Number', 'PartyID', 'FullName', 
                    'Mobile', 'PartID', 'Code', 'Expr1', 'MajorUnitQuantity', 
                    'Price', 'ReductionAmount', 'AdditionAmount', 'NetPrice', 
                    'FirstName', 'LastName'
                ]
                
                df = df[columns]
                
                # Clean data row by row
                data = []
                for row in df.values:
                    clean_row = []
                    for value in row:
                        if isinstance(value, float) and (pd.isna(value) or pd.isnull(value)):
                            clean_row.append(None)
                        else:
                            clean_row.append(value)
                    data.append(tuple(clean_row))
                
                # Build upsert query
                placeholders = ', '.join(['%s'] * len(columns))
                update_clause = ', '.join([
                    f"{col}=VALUES({col})" for col in columns 
                    if col != 'InvoiceItemID'
                ])
                
                query = f"""
                INSERT INTO {table_name} ({', '.join(columns)}) 
                VALUES ({placeholders})
                ON DUPLICATE KEY UPDATE {update_clause}
                """
                
                cursor.executemany(query, data)
                conn.commit()
                
        except Exception as e:
            logging.error(f"Upsert failed for {table_name}: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    
    def verify_sync(self):
        """Verify sync by comparing row counts"""
        try:
            # Get MySQL counts
            mysql_conn = self.get_mysql_connection()
            with mysql_conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM voucher")
                mysql_voucher_count = cursor.fetchone()[0]
                cursor.execute("SELECT COUNT(*) FROM invoiceitems")
                mysql_invoice_count = cursor.fetchone()[0]
            mysql_conn.close()
            
            # Get SQL Server counts
            with self.sqlserver_engine.connect() as sql_conn:
                voucher_count = pd.read_sql(text("SELECT COUNT(*) FROM dbo.BVoucherItemStoreOnly"), sql_conn).iloc[0, 0]
                invoice_count = pd.read_sql(text("SELECT COUNT(*) FROM dbo.BInvoiceItem"), sql_conn).iloc[0, 0]
            
            logging.info("=" * 50)
            logging.info("VERIFICATION RESULTS:")
            logging.info(f"Voucher - SQL Server: {voucher_count}, MySQL: {mysql_voucher_count}")
            logging.info(f"Invoiceitems - SQL Server: {invoice_count}, MySQL: {mysql_invoice_count}")
            
            if voucher_count == mysql_voucher_count and invoice_count == mysql_invoice_count:
                logging.info("✅ All counts match! Sync successful.")
            else:
                logging.warning("⚠️ Counts don't match! Please investigate.")
            logging.info("=" * 50)
            
        except Exception as e:
            logging.error(f"Verification failed: {e}")
    
    def full_sync(self):
        """Perform full sync with verification"""
        logging.info("Starting full sync...")
        start_time = time.time()
        
        try:
            # Truncate existing data
            self.truncate_tables()
            
            # Sync both tables
            self.sync_voucher()
            self.sync_invoiceitems()
            
            # Verify the sync
            self.verify_sync()
            
            logging.info(f"Full sync completed in {time.time() - start_time:.2f} seconds")
            
        except Exception as e:
            logging.error(f"Full sync failed: {e}")
            raise

if __name__ == "__main__":
    # Install required packages:
    # pip install pymysql pyodbc pandas sqlalchemy
    
    syncer = DataSyncer()
    
    # Choose sync method:
    
    # 1. Full sync (first time or complete refresh)
    syncer.full_sync()
    
    # 2. For incremental sync (for regular updates)
    # Uncomment to use:
    # from datetime import datetime, timedelta
    # last_sync = datetime.now() - timedelta(days=1)  # Sync last 24 hours
    # syncer.incremental_sync(last_sync)
    
    # 3. For daily automated sync without truncating everything
    # syncer.sync_voucher()
    # syncer.sync_invoiceitems()