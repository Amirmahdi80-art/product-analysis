"""
run.py — Top 10 Inventory Voucher records (spec ref 68)

Fixes the original query:
  - v.CounterpartEntityRef is 100% NULL for spec 68
  - The real party column for spec 68 is
        vi.DelivererOrReceiverPartyRef   (457 rows)
    or  v.DelivererOrReceiverPartyRef    (15 rows / matches same 457 items)
  - Uses SQLAlchemy so pandas doesn't warn.
"""

import logging
from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# ─────────────────────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("top10_query_log.txt"),
        logging.StreamHandler(),
    ],
)

# ─────────────────────────────────────────────────────────────
# SQL Server engine (no pandas warning)
# ─────────────────────────────────────────────────────────────
ENGINE = create_engine(
    URL.create(
        "mssql+pyodbc",
        username="reports",
        password="123456789",
        host="172.16.30.20",
        database="Webpoosh_Sg3",
        query={
            "driver": "ODBC Driver 17 for SQL Server",
            "TrustServerCertificate": "yes",
        },
    ),
    fast_executemany=True,
)


# ─────────────────────────────────────────────────────────────
# Query
# ─────────────────────────────────────────────────────────────
SPEC_REF = 68
TOP_N    = 250

# Change to "LEFT JOIN" + comment out the pa line if you want
# the rows where the party is NULL (Option B).
QUERY = text(f"""
    SELECT TOP {TOP_N}
    v.InventoryVoucherID,
    v.Number                AS VoucherNo,
    v.Date                  AS VoucherDate,
    src.StoreID             AS SourceStoreID,
    src.Name                AS SourceStore,
    dst.StoreID             AS DestStoreID,
    dst.Name                AS DestStore,
    p.Code                  AS PartCode,
    p.Name                  AS PartName,
    vi.MajorUnitQuantity    AS Qty
    FROM     LGS3.InventoryVoucher       AS v
    INNER JOIN LGS3.InventoryVoucherItem AS vi  ON vi.InventoryVoucherRef = v.InventoryVoucherID
    INNER JOIN LGS3.Part                 AS p   ON p.PartID               = vi.PartRef
    INNER JOIN LGS3.Store                AS src ON src.StoreID            = vi.StoreRef
    LEFT  JOIN LGS3.Store                AS dst ON dst.StoreID            = v.CounterpartStoreRef
    WHERE   v.InventoryVoucherSpecificationRef = 68
    AND   src.StoreID IN (6, 2)
    AND dst.StoreID IN (17, 5, 13, 18, 16, 3, 10, 15)
    AND p.Code like '2034517902%'
    ORDER BY v.InventoryVoucherID DESC, vi.RowNumber
""")


def get_top10(spec_ref: int = SPEC_REF, top_n: int = TOP_N) -> pd.DataFrame:
    logging.info(f"Running top {top_n} query (SpecificationRef={spec_ref})...")
    start = datetime.now()

    # TOP is baked into the SQL text, so we don't need to param it.
    # If you want it parameterised, replace TOP {top_n} with TOP (:n)
    # and pass params={"spec": spec_ref, "n": top_n}.
    with ENGINE.connect() as conn:
        df = pd.read_sql(QUERY, conn, params={"spec": spec_ref})

    logging.info(f"Returned {len(df)} rows in {(datetime.now() - start).total_seconds():.2f}s")
    return df


def display(df: pd.DataFrame) -> None:
    if df.empty:
        print("\n⚠️  0 rows — try switching the party JOIN to LEFT JOIN.\n")
        return

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 300)
    pd.set_option("display.max_colwidth", 40)

    print("\n" + "=" * 110)
    print(f"TOP {len(df)} RECORDS — {len(df.columns)} columns")
    print("=" * 110)

    # Show a compact summary of the interesting columns
    interesting = [c for c in (
        "InventoryVoucherID", "Number", "Date",
        "InventoryVoucherItemID", "PartID", "Code", "Name",
        "MajorUnitQuantity", "Quantity",
        "StoreID", "PartyID", "FullName", "Mobile",
    ) if c in df.columns]

    if interesting:
        print("\n── Key columns ──")
        print(df[interesting].to_string(index=False))

    print("\n── Full rows ──")
    print(df.to_string(index=False))


if __name__ == "__main__":
    df = get_top10()
    display(df)

    if not df.empty:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_path = f"top10_spec{SPEC_REF}_{stamp}.csv"
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        logging.info(f"Saved {csv_path}")

        try:
            xlsx_path = csv_path.replace(".csv", ".xlsx")
            df.to_excel(xlsx_path, index=False)
            logging.info(f"Saved {xlsx_path}")
        except ImportError:
            logging.warning("openpyxl not installed; skipped Excel export.")