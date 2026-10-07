"""
diagnose.py — find out why the query returns 0 rows
"""
import pyodbc

CONN_STR = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=172.16.30.20;'
    'DATABASE=Webpoosh_Sg3;'
    'UID=reports;'
    'PWD=123456789'
)

def run(cur, label, sql, params=None):
    try:
        cur.execute(sql, params or ())
        rows = cur.fetchall()
        print(f"\n── {label} ──")
        for r in rows[:20]:
            print("  ", tuple(r))
        if not rows:
            print("   (0 rows)")
    except Exception as e:
        print(f"\n── {label} ──\n   ERROR: {e}")

conn = pyodbc.connect(CONN_STR)
cur = conn.cursor()

# 1) Which database / server are we on?
run(cur, "Current DB", "SELECT DB_NAME(), @@SERVERNAME")

# 2) Do the schemas LGS3 / GNR3 exist in this DB?
run(cur, "Schemas", """
    SELECT name FROM sys.schemas WHERE name IN ('LGS3','GNR3','dbo')
""")

# 3) Do the tables exist as LGS3.* ?
run(cur, "LGS3 tables", """
    SELECT s.name + '.' + t.name
    FROM sys.tables t JOIN sys.schemas s ON s.schema_id = t.schema_id
    WHERE s.name IN ('LGS3','GNR3')
    ORDER BY 1
""")

# 4) Are LGS3 / GNR3 *databases* on this server?
run(cur, "Databases", """
    SELECT name FROM sys.databases WHERE name IN ('LGS3','GNR3','Webpoosh_Sg3')
""")

# 5) Count rows in the base table
run(cur, "InventoryVoucher count", "SELECT COUNT(*) FROM LGS3.InventoryVoucher")

# 6) Count rows filtered by spec ref
run(cur, "Spec ref = 68 count", """
    SELECT InventoryVoucherSpecificationRef, COUNT(*)
    FROM LGS3.InventoryVoucher
    GROUP BY InventoryVoucherSpecificationRef
    ORDER BY 2 DESC
""")

# 7) Any spec refs at all?
run(cur, "Distinct spec refs (top 20)", """
    SELECT DISTINCT TOP 20 InventoryVoucherSpecificationRef
    FROM LGS3.InventoryVoucher
    ORDER BY 1
""")

conn.close()