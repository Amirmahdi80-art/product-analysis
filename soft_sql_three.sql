-- run this in powershell: & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" --default-character-set=utf8mb4 -u root -p salesoptimizer -e "source C:/projects/project-1.0.0/salesop/soft_sql_three.sql"

-- ============================================
-- STEP 1: Pre-flight verification
-- ============================================

-- How many rows currently exist?
SELECT COUNT(*) FROM salesoptimizer.cumulative_product_lookup;

-- Preview what the new data looks like (before insert)
WITH ctr AS (
    SELECT 
        ip.*,
        pl.category_code,
        pl.total_inventory,
        pl.first_entered_inventory_date,
        pl.first_show_date,
        pl.days_since_entry,
        pl.days_since_show,
        pl.days_since_entry - pl.days_since_show AS date_diff,
        SUM(ip.MajorUnitQuantity) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_qty,
        SUM(ip.NetPrice) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_netprice,
        SUM(ip.ReductionAmount) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_reduction,
        SUM(ip.AdditionAmount) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_addition,
        SUM(ip.Price) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_price
    FROM salesoptimizer.invoiceitems_parent ip
    INNER JOIN salesoptimizer.products_lookup pl
        ON ip.ParentCode = pl.product_code
)
SELECT COUNT(*) FROM ctr;

-- ============================================
-- STEP 2: Truncate and re-insert
-- ============================================
TRUNCATE TABLE salesoptimizer.cumulative_product_lookup;

INSERT INTO salesoptimizer.cumulative_product_lookup
    (ParentCode, Expr1, Name, category_code, Expr2, SalesOfficeID, 
     MajorUnitQuantity, total_inventory, first_entered_inventory_date, 
     first_show_date, days_since_entry, days_since_show, date_diff, 
     cumulative_qty, cumulative_netprice, cumulative_reduction, 
     cumulative_addition, cumulative_price)
WITH ctr AS (
    SELECT 
        ip.ParentCode,
        ip.Expr1,
        ip.Name,
        pl.category_code,
        ip.Expr2,
        ip.SalesOfficeID,
        ip.MajorUnitQuantity,
        pl.total_inventory,
        pl.first_entered_inventory_date,
        pl.first_show_date,
        pl.days_since_entry,
        pl.days_since_show,
        pl.days_since_entry - pl.days_since_show AS date_diff,
        SUM(ip.MajorUnitQuantity) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_qty,
        SUM(ip.NetPrice) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_netprice,
        SUM(ip.ReductionAmount) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_reduction,
        SUM(ip.AdditionAmount) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_addition,
        SUM(ip.Price) OVER (
            PARTITION BY ip.ParentCode
            ORDER BY ip.Expr2
        ) AS cumulative_price
    FROM salesoptimizer.invoiceitems_parent ip
    INNER JOIN salesoptimizer.products_lookup pl
        ON ip.ParentCode = pl.product_code
)
SELECT 
    ParentCode, Expr1, Name, category_code, Expr2, SalesOfficeID, 
    MajorUnitQuantity, total_inventory, first_entered_inventory_date, 
    first_show_date, days_since_entry, days_since_show, date_diff, 
    cumulative_qty, cumulative_netprice, cumulative_reduction, 
    cumulative_addition, cumulative_price
FROM ctr;
