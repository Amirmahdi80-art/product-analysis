import pyodbc

CONN_STR = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=172.16.30.20;'
    'DATABASE=Webpoosh_Sg3;'
    'UID=reports;'
    'PWD=123456789'
)

conn = pyodbc.connect(CONN_STR)
cur = conn.cursor()

def show(label, sql):
    print(f"\n── {label} ──")
    cur.execute(sql)
    cols = [c[0] for c in cur.description]
    print("   " + " | ".join(cols))
    for r in cur.fetchall():
        print("   " + " | ".join("" if v is None else str(v) for v in r))

# 1) Which party-column is populated on the voucher HEADER for spec 68?
show("Header party columns (spec 68)", """
    SELECT
        SUM(CASE WHEN CounterpartEntityRef        IS NULL THEN 1 ELSE 0 END) AS ctr_null,
        SUM(CASE WHEN CounterpartEntityRef        IS NOT NULL THEN 1 ELSE 0 END) AS ctr_notnull,
        SUM(CASE WHEN DelivererOrReceiverPartyRef IS NULL THEN 1 ELSE 0 END) AS deliv_null,
        SUM(CASE WHEN DelivererOrReceiverPartyRef IS NOT NULL THEN 1 ELSE 0 END) AS deliv_notnull,
        COUNT(*) AS total
    FROM LGS3.InventoryVoucher
    WHERE InventoryVoucherSpecificationRef = 68
""")

# 2) Same, on the ITEM rows
show("Item party columns (spec 68)", """
    SELECT
        SUM(CASE WHEN vi.CounterpartEntityRef        IS NULL THEN 1 ELSE 0 END) AS ctr_null,
        SUM(CASE WHEN vi.CounterpartEntityRef        IS NOT NULL THEN 1 ELSE 0 END) AS ctr_notnull,
        SUM(CASE WHEN vi.DelivererOrReceiverPartyRef IS NULL THEN 1 ELSE 0 END) AS deliv_null,
        SUM(CASE WHEN vi.DelivererOrReceiverPartyRef IS NOT NULL THEN 1 ELSE 0 END) AS deliv_notnull,
        COUNT(*) AS total
    FROM LGS3.InventoryVoucherItem vi
    JOIN LGS3.InventoryVoucher v ON v.InventoryVoucherID = vi.InventoryVoucherRef
    WHERE v.InventoryVoucherSpecificationRef = 68
""")

# 3) Try joining via item.CounterpartEntityRef
show("Join via vi.CounterpartEntityRef", """
    SELECT COUNT(*) AS n
    FROM LGS3.InventoryVoucher v
    JOIN LGS3.InventoryVoucherItem vi ON vi.InventoryVoucherRef = v.InventoryVoucherID
    JOIN GNR3.Party pa ON pa.PartyID = vi.CounterpartEntityRef
    WHERE v.InventoryVoucherSpecificationRef = 68
""")

# 4) Try joining via vi.DelivererOrReceiverPartyRef
show("Join via vi.DelivererOrReceiverPartyRef", """
    SELECT COUNT(*) AS n
    FROM LGS3.InventoryVoucher v
    JOIN LGS3.InventoryVoucherItem vi ON vi.InventoryVoucherRef = v.InventoryVoucherID
    JOIN GNR3.Party pa ON pa.PartyID = vi.DelivererOrReceiverPartyRef
    WHERE v.InventoryVoucherSpecificationRef = 68
""")

# 5) Try joining via header.DelivererOrReceiverPartyRef
show("Join via v.DelivererOrReceiverPartyRef", """
    SELECT COUNT(*) AS n
    FROM LGS3.InventoryVoucher v
    JOIN LGS3.InventoryVoucherItem vi ON vi.InventoryVoucherRef = v.InventoryVoucherID
    JOIN GNR3.Party pa ON pa.PartyID = v.DelivererOrReceiverPartyRef
    WHERE v.InventoryVoucherSpecificationRef = 68
""")

# 6) Sanity: how many distinct PartyIDs are in GNR3.Party overall
show("Party rows in GNR3.Party", "SELECT COUNT(*) AS n FROM GNR3.Party")

conn.close()