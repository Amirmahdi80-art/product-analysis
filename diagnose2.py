import pyodbc

CONN_STR = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=172.16.30.20;'
    'DATABASE=Webpoosh_Sg3;'
    'UID=reports;'
    'PWD=123456789'
)

def show(cur, label, sql, params=()):
    print(f"\n── {label} ──")
    try:
        cur.execute(sql, params)
        rows = cur.fetchall()
        if not rows:
            print("   (0 rows)")
            return
        cols = [c[0] for c in cur.description]
        print("   " + " | ".join(cols))
        for r in rows[:30]:
            print("   " + " | ".join("" if v is None else str(v) for v in r))
    except Exception as e:
        print(f"   ERROR: {e}")

conn = pyodbc.connect(CONN_STR)
cur = conn.cursor()

# 1) Columns of each table involved
for tbl in ("LGS3.InventoryVoucher",
            "LGS3.InventoryVoucherItem",
            "LGS3.Part",
            "LGS3.Store",
            "GNR3.Party"):
    show(cur, f"Columns of {tbl}", f"""
        SELECT COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = '{tbl.split('.')[0]}'
          AND TABLE_NAME   = '{tbl.split('.')[1]}'
        ORDER BY ORDINAL_POSITION
    """)

# 2) Are CounterpartEntityRef values NULL for spec 68?
show(cur, "CounterpartEntityRef distribution (spec 68)", """
    SELECT TOP 20
        CASE WHEN CounterpartEntityRef IS NULL THEN 'NULL' ELSE 'NOT NULL' END AS state,
        COUNT(*) AS cnt
    FROM LGS3.InventoryVoucher
    WHERE InventoryVoucherSpecificationRef = 68
    GROUP BY CASE WHEN CounterpartEntityRef IS NULL THEN 'NULL' ELSE 'NOT NULL' END
""")

# 3) Do InventoryVoucherItem rows exist for spec-68 vouchers?
show(cur, "Item count for spec-68 vouchers", """
    SELECT COUNT(*) AS item_rows
    FROM LGS3.InventoryVoucher v
    JOIN LGS3.InventoryVoucherItem vi ON vi.InventoryVoucherRef = v.InventoryVoucherID
    WHERE v.InventoryVoucherSpecificationRef = 68
""")

# 4) Does the Party join survive?
show(cur, "v + vi + party", """
    SELECT COUNT(*) AS n
    FROM LGS3.InventoryVoucher v
    JOIN LGS3.InventoryVoucherItem vi ON vi.InventoryVoucherRef = v.InventoryVoucherID
    JOIN GNR3.Party pa ON pa.PartyID = v.CounterpartEntityRef
    WHERE v.InventoryVoucherSpecificationRef = 68
""")

# 5) Part join
show(cur, "v + vi + part", """
    SELECT COUNT(*) AS n
    FROM LGS3.InventoryVoucher v
    JOIN LGS3.InventoryVoucherItem vi ON vi.InventoryVoucherRef = v.InventoryVoucherID
    JOIN LGS3.Part p ON p.PartID = vi.PartRef
    WHERE v.InventoryVoucherSpecificationRef = 68
""")

# 6) Store join
show(cur, "v + vi + store", """
    SELECT COUNT(*) AS n
    FROM LGS3.InventoryVoucher v
    JOIN LGS3.InventoryVoucherItem vi ON vi.InventoryVoucherRef = v.InventoryVoucherID
    JOIN LGS3.Store s ON s.StoreID = vi.StoreRef
    WHERE v.InventoryVoucherSpecificationRef = 68
""")

conn.close()