-- run this in powershell: & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" --default-character-set=utf8mb4 -u root -p salesoptimizer -e "source C:/projects/project-1.0.0/salesop/soft_sql_five.sql"

SELECT COUNT(*) AS current_rows FROM salesoptimizer.twelve_month_analysis_store;

TRUNCATE TABLE salesoptimizer.twelve_month_analysis_store;

INSERT INTO salesoptimizer.twelve_month_analysis_store
    (product_code, SalesOfficeID, Name, category_code,
     total_inventory, first_show_date, age_in_months, age_in_days,
     first_month_qty, second_month_qty, third_month_qty, forth_month_qty,
     fifth_month_qty, sixth_month_qty, seventh_month_qty, eighth_month_qty,
     ninth_month_qty, tenth_month_qty, eleventh_month_qty, twelveth_month_qty,
     first_month_per, second_month_per, third_month_per, forth_month_per,
     fifth_month_per, sixth_month_per, seventh_month_per, eighth_month_per,
     ninth_month_per, tenth_month_per, eleventh_month_per, twelveth_month_per,
     total_sold_12_months)
WITH base_data AS (
    SELECT 
        ParentCode,
        Name,
        category_code,
        SalesOfficeID,
        MajorUnitQuantity,
        total_inventory,
        first_show_date,
        TIMESTAMPDIFF(MONTH, first_show_date, Expr2) + 1 AS month_number,
        TIMESTAMPDIFF(MONTH, first_show_date, CURDATE()) AS age_months,
        DATEDIFF(CURDATE(), first_show_date) AS age_days
    FROM salesoptimizer.cumulative_product_lookup
    WHERE Expr2 > first_show_date
      AND first_show_date IS NOT NULL
),
monthly_qty AS (
    SELECT 
        ParentCode, category_code, SalesOfficeID, Name,
        total_inventory, first_show_date, age_months, age_days, month_number,
        SUM(MajorUnitQuantity) AS month_qty
    FROM base_data
    WHERE month_number BETWEEN 1 AND 12
    GROUP BY 
        ParentCode, SalesOfficeID, Name, category_code,
        total_inventory, first_show_date, age_months, age_days, month_number
),
pivoted AS (
    SELECT 
        ParentCode, category_code, SalesOfficeID, Name,
        total_inventory, first_show_date, age_months, age_days,
        MAX(CASE WHEN month_number = 1  THEN month_qty ELSE 0 END) AS first_month_qty,
        MAX(CASE WHEN month_number = 2  THEN month_qty ELSE 0 END) AS second_month_qty,
        MAX(CASE WHEN month_number = 3  THEN month_qty ELSE 0 END) AS third_month_qty,
        MAX(CASE WHEN month_number = 4  THEN month_qty ELSE 0 END) AS forth_month_qty,
        MAX(CASE WHEN month_number = 5  THEN month_qty ELSE 0 END) AS fifth_month_qty,
        MAX(CASE WHEN month_number = 6  THEN month_qty ELSE 0 END) AS sixth_month_qty,
        MAX(CASE WHEN month_number = 7  THEN month_qty ELSE 0 END) AS seventh_month_qty,
        MAX(CASE WHEN month_number = 8  THEN month_qty ELSE 0 END) AS eighth_month_qty,
        MAX(CASE WHEN month_number = 9  THEN month_qty ELSE 0 END) AS ninth_month_qty,
        MAX(CASE WHEN month_number = 10 THEN month_qty ELSE 0 END) AS tenth_month_qty,
        MAX(CASE WHEN month_number = 11 THEN month_qty ELSE 0 END) AS eleventh_month_qty,
        MAX(CASE WHEN month_number = 12 THEN month_qty ELSE 0 END) AS twelveth_month_qty
    FROM monthly_qty
    GROUP BY 
        ParentCode, SalesOfficeID, Name, category_code,
        total_inventory, first_show_date, age_months, age_days
)
SELECT 
    ParentCode, SalesOfficeID, Name, category_code,
    total_inventory, first_show_date, age_months, age_days,
    first_month_qty, second_month_qty, third_month_qty, forth_month_qty,
    fifth_month_qty, sixth_month_qty, seventh_month_qty, eighth_month_qty,
    ninth_month_qty, tenth_month_qty, eleventh_month_qty, twelveth_month_qty,
    ROUND((first_month_qty    / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((second_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((third_month_qty    / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((forth_month_qty    / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((fifth_month_qty    / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((sixth_month_qty    / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((seventh_month_qty  / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((eighth_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((ninth_month_qty    / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((tenth_month_qty    / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((eleventh_month_qty / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND((twelveth_month_qty / NULLIF(total_inventory, 0)) * 100, 2),
    ROUND(first_month_qty + second_month_qty + third_month_qty + forth_month_qty 
        + fifth_month_qty + sixth_month_qty + seventh_month_qty + eighth_month_qty 
        + ninth_month_qty + tenth_month_qty + eleventh_month_qty + twelveth_month_qty, 2)
FROM pivoted;

-- ============================================
-- STEP 4: Verify
-- ============================================
SELECT COUNT(*) FROM salesoptimizer.twelve_month_analysis_store;
