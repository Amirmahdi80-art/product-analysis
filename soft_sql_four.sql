-- run this in powershell: & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" --default-character-set=utf8mb4 -u root -p salesoptimizer -e "source C:/projects/project-1.0.0/salesop/soft_sql_four.sql"

SELECT COUNT(*) AS current_rows FROM salesoptimizer.twelve_month_analysis;

TRUNCATE TABLE salesoptimizer.twelve_month_analysis;


INSERT INTO salesoptimizer.twelve_month_analysis
    (product_code, category_code, total_inventory, first_show_date,
     age_in_months, age_in_days,
     first_month_qty, second_month_qty, third_month_qty, forth_month_qty,
     fifth_month_qty, sixth_month_qty, seventh_month_qty, eighth_month_qty,
     ninth_month_qty, tenth_month_qty, eleventh_month_qty, twelveth_month_qty,
     first_month_per, second_month_per, third_month_per, forth_month_per,
     fifth_month_per, sixth_month_per, seventh_month_per, eighth_month_per,
     ninth_month_per, tenth_month_per, eleventh_month_per, twelveth_month_per,
     max_cumulative_reduction, max_cumulative_price, discount_percentage,
     total_sold_12_months, total_sold)
-- WITH base_data AS (
--     SELECT 
--         ParentCode,
--         category_code,
--         MajorUnitQuantity,
--         total_inventory,
--         first_show_date,
--         TIMESTAMPDIFF(MONTH, first_show_date, Expr2) + 1 AS month_number,
--         TIMESTAMPDIFF(MONTH, first_show_date, CURDATE()) AS age_months,
--         DATEDIFF(CURDATE(), first_show_date) AS age_days,
--         cumulative_reduction,
--         cumulative_price
--     FROM salesoptimizer.cumulative_product_lookup
--     WHERE Expr2 > first_show_date
--       AND first_show_date IS NOT NULL
-- ),
-- monthly_qty AS (
--     SELECT 
--         ParentCode,
--         category_code,
--         total_inventory,
--         first_show_date,
--         age_months,
--         age_days,
--         month_number,
--         SUM(MajorUnitQuantity) AS month_qty,
--         MAX(cumulative_reduction) AS max_cumulative_reduction,
--         MAX(cumulative_price) AS max_cumulative_price
--     FROM base_data
--     WHERE month_number BETWEEN 1 AND 12
--     GROUP BY ParentCode, category_code, total_inventory,
--              first_show_date, age_months, age_days, month_number
-- ),
-- pivoted AS (
--     SELECT 
--         ParentCode,
--         category_code,
--         total_inventory,
--         first_show_date,
--         age_months,
--         age_days,
--         MAX(CASE WHEN month_number = 1  THEN month_qty ELSE 0 END) AS first_month_qty,
--         MAX(CASE WHEN month_number = 2  THEN month_qty ELSE 0 END) AS second_month_qty,
--         MAX(CASE WHEN month_number = 3  THEN month_qty ELSE 0 END) AS third_month_qty,
--         MAX(CASE WHEN month_number = 4  THEN month_qty ELSE 0 END) AS forth_month_qty,
--         MAX(CASE WHEN month_number = 5  THEN month_qty ELSE 0 END) AS fifth_month_qty,
--         MAX(CASE WHEN month_number = 6  THEN month_qty ELSE 0 END) AS sixth_month_qty,
--         MAX(CASE WHEN month_number = 7  THEN month_qty ELSE 0 END) AS seventh_month_qty,
--         MAX(CASE WHEN month_number = 8  THEN month_qty ELSE 0 END) AS eighth_month_qty,
--         MAX(CASE WHEN month_number = 9  THEN month_qty ELSE 0 END) AS ninth_month_qty,
--         MAX(CASE WHEN month_number = 10 THEN month_qty ELSE 0 END) AS tenth_month_qty,
--         MAX(CASE WHEN month_number = 11 THEN month_qty ELSE 0 END) AS eleventh_month_qty,
--         MAX(CASE WHEN month_number = 12 THEN month_qty ELSE 0 END) AS twelveth_month_qty,
--         MAX(max_cumulative_reduction) AS max_cumulative_reduction,
--         MAX(max_cumulative_price) AS max_cumulative_price
--     FROM monthly_qty
--     GROUP BY ParentCode, category_code, total_inventory,
--              first_show_date, age_months, age_days
-- )
-- SELECT 
--     ParentCode,
--     category_code,
--     total_inventory,
--     first_show_date,
--     age_months,
--     age_days,
--     first_month_qty, second_month_qty, third_month_qty, forth_month_qty,
--     fifth_month_qty, sixth_month_qty, seventh_month_qty, eighth_month_qty,
--     ninth_month_qty, tenth_month_qty, eleventh_month_qty, twelveth_month_qty,
--     ROUND((first_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((second_month_qty  / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((third_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((forth_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((fifth_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((sixth_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((seventh_month_qty / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((eighth_month_qty  / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((ninth_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((tenth_month_qty   / NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((eleventh_month_qty/ NULLIF(total_inventory, 0)) * 100, 2),
--     ROUND((twelveth_month_qty/ NULLIF(total_inventory, 0)) * 100, 2),
--     max_cumulative_reduction,
--     max_cumulative_price,
--     ROUND((max_cumulative_reduction / NULLIF(max_cumulative_price, 0)) * 100, 2),
--     ROUND(first_month_qty + second_month_qty + third_month_qty + forth_month_qty 
--         + fifth_month_qty + sixth_month_qty + seventh_month_qty + eighth_month_qty 
--         + ninth_month_qty + tenth_month_qty + eleventh_month_qty + twelveth_month_qty, 2)
-- FROM pivoted;


-- SELECT COUNT(*) FROM salesoptimizer.twelve_month_analysis;

WITH base_data AS (
    SELECT 
        ParentCode,
        category_code,
        MajorUnitQuantity,
        total_inventory,
        first_show_date,
        TIMESTAMPDIFF(MONTH, first_show_date, Expr2) + 1 AS month_number,
        TIMESTAMPDIFF(MONTH, first_show_date, CURDATE()) AS age_months,
        DATEDIFF(CURDATE(), first_show_date) AS age_days,
        cumulative_reduction,
        cumulative_price,
        cumulative_qty
    FROM salesoptimizer.cumulative_product_lookup
    WHERE Expr2 > first_show_date
      AND first_show_date IS NOT NULL
),
total_sold_per_product AS (
    SELECT 
        ParentCode,
        MAX(cumulative_qty) AS total_sold
    FROM base_data
    GROUP BY ParentCode
),
monthly_qty AS (
    SELECT 
        ParentCode,
        category_code,
        total_inventory,
        first_show_date,
        age_months,
        age_days,
        month_number,
        SUM(MajorUnitQuantity) AS month_qty,
        MAX(cumulative_reduction) AS max_cumulative_reduction,
        MAX(cumulative_price) AS max_cumulative_price
    FROM base_data
    WHERE month_number BETWEEN 1 AND 12
    GROUP BY ParentCode, category_code, total_inventory,
             first_show_date, age_months, age_days, month_number
),
pivoted AS (
    SELECT 
        ParentCode,
        category_code,
        total_inventory,
        first_show_date,
        age_months,
        age_days,
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
        MAX(CASE WHEN month_number = 12 THEN month_qty ELSE 0 END) AS twelveth_month_qty,
        MAX(max_cumulative_reduction) AS max_cumulative_reduction,
        MAX(max_cumulative_price) AS max_cumulative_price
    FROM monthly_qty
    GROUP BY ParentCode, category_code, total_inventory,
             first_show_date, age_months, age_days
)
SELECT 
    p.ParentCode,
    p.category_code,
    p.total_inventory,
    p.first_show_date,
    p.age_months,
    p.age_days,
    p.first_month_qty, p.second_month_qty, p.third_month_qty, p.forth_month_qty,
    p.fifth_month_qty, p.sixth_month_qty, p.seventh_month_qty, p.eighth_month_qty,
    p.ninth_month_qty, p.tenth_month_qty, p.eleventh_month_qty, p.twelveth_month_qty,
    ROUND((p.first_month_qty    / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.second_month_qty   / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.third_month_qty    / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.forth_month_qty    / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.fifth_month_qty    / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.sixth_month_qty    / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.seventh_month_qty  / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.eighth_month_qty   / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.ninth_month_qty    / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.tenth_month_qty    / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.eleventh_month_qty / NULLIF(p.total_inventory, 0)) * 100, 2),
    ROUND((p.twelveth_month_qty / NULLIF(p.total_inventory, 0)) * 100, 2),
    p.max_cumulative_reduction,
    p.max_cumulative_price,
    ROUND((p.max_cumulative_reduction / NULLIF(p.max_cumulative_price, 0)) * 100, 2),
    ROUND(p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty 
        + p.fifth_month_qty + p.sixth_month_qty + p.seventh_month_qty + p.eighth_month_qty 
        + p.ninth_month_qty + p.tenth_month_qty + p.eleventh_month_qty + p.twelveth_month_qty, 2),
    t.total_sold
FROM pivoted p
LEFT JOIN total_sold_per_product t
    ON p.ParentCode = t.ParentCode;