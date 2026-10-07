"""
list_dest_stores.py — distinct destination stores for spec 68, source store 7
"""
import logging
from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

ENGINE = create_engine(
    URL.create(
        "mssql+pyodbc",
        username="reports",
        password="123456789",
        host="172.16.30.20",
        database="Webpoosh_Sg3",
        query={"driver": "ODBC Driver 17 for SQL Server",
               "TrustServerCertificate": "yes"},
    ),
    fast_executemany=True,
)

SPEC_REF     = 68
SRC_STORE_ID = 7

SQL = text("""
    SELECT
        dst.StoreID                          AS DestStoreID,
        dst.Name                             AS DestStore,
        dst.Code                             AS DestStoreCode,
        COUNT(DISTINCT v.InventoryVoucherID) AS VoucherCount,
        COUNT(*)                             AS LineCount,
        SUM(vi.MajorUnitQuantity)            AS TotalQty
    FROM     LGS3.InventoryVoucher       AS v
    INNER JOIN LGS3.InventoryVoucherItem AS vi  ON vi.InventoryVoucherRef = v.InventoryVoucherID
    INNER JOIN LGS3.Store                AS src ON src.StoreID            = vi.StoreRef
    LEFT  JOIN LGS3.Store                AS dst ON dst.StoreID            = v.CounterpartStoreRef
    WHERE   v.InventoryVoucherSpecificationRef = :spec
      AND   src.StoreID = :src_store
    GROUP BY
        dst.StoreID, dst.Name, dst.Code
    ORDER BY VoucherCount DESC
""")

if __name__ == "__main__":
    with ENGINE.connect() as conn:
        df = pd.read_sql(SQL, conn, params={"spec": SPEC_REF, "src_store": SRC_STORE_ID})

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)
    pd.set_option("display.max_colwidth", 40)

    print("\n" + "=" * 90)
    print(f"DISTINCT DESTINATION STORES — spec={SPEC_REF}, source store={SRC_STORE_ID}")
    print("=" * 90)
    print(df.to_string(index=False))
    print("=" * 90)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv = f"dest_stores_spec{SPEC_REF}_src{SRC_STORE_ID}_{stamp}.csv"
    df.to_csv(csv, index=False, encoding="utf-8-sig")
    logging.info(f"Saved {csv}")