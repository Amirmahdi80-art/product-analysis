-- Drop table if it exists
DROP TABLE IF EXISTS salesoptimizer.twelve_month_analysis;

-- Create the table
CREATE TABLE salesoptimizer.twelve_month_analysis AS
WITH base_data AS (
    SELECT 
        ParentCode,
        Expr1,
        Name,
        category_code,
        Expr2,
        SalesOfficeID,
        MajorUnitQuantity,
        total_inventory,
        first_entered_inventory_date,
        first_show_date,
        days_since_entry,
        days_since_show,
        date_diff,
        cumulative_qty,
        cumulative_netprice,
        cumulative_reduction,
        cumulative_addition,
        cumulative_price,
        -- Calculate month number based on first_show_date
        TIMESTAMPDIFF(MONTH, first_show_date, Expr2) + 1 AS month_number,
        -- Calculate age of product based on custom date (September 9, 2026)
        TIMESTAMPDIFF(MONTH, first_show_date, CURDATE()) AS age_months, -- replace '2026-09-09' with CURDATE()
        DATEDIFF(CURDATE(), first_show_date) AS age_days -- replace '2026-09-09' with CURDATE()
    FROM salesoptimizer.cumulative_product_lookup
    WHERE Expr2 > first_show_date
        AND first_show_date IS NOT NULL
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
    GROUP BY 
        ParentCode,
        category_code,
        total_inventory,
        first_show_date,
        age_months,
        age_days,
        month_number
),
pivoted AS (
    SELECT 
        ParentCode,
        category_code,
        total_inventory,
        first_show_date,
        age_months,
        age_days,
        -- Monthly quantities
        MAX(CASE WHEN month_number = 1 THEN month_qty ELSE 0 END) AS first_month_qty,
        MAX(CASE WHEN month_number = 2 THEN month_qty ELSE 0 END) AS second_month_qty,
        MAX(CASE WHEN month_number = 3 THEN month_qty ELSE 0 END) AS third_month_qty,
        MAX(CASE WHEN month_number = 4 THEN month_qty ELSE 0 END) AS forth_month_qty,
        MAX(CASE WHEN month_number = 5 THEN month_qty ELSE 0 END) AS fifth_month_qty,
        MAX(CASE WHEN month_number = 6 THEN month_qty ELSE 0 END) AS sixth_month_qty,
        MAX(CASE WHEN month_number = 7 THEN month_qty ELSE 0 END) AS seventh_month_qty,
        MAX(CASE WHEN month_number = 8 THEN month_qty ELSE 0 END) AS eighth_month_qty,
        MAX(CASE WHEN month_number = 9 THEN month_qty ELSE 0 END) AS ninth_month_qty,
        MAX(CASE WHEN month_number = 10 THEN month_qty ELSE 0 END) AS tenth_month_qty,
        MAX(CASE WHEN month_number = 11 THEN month_qty ELSE 0 END) AS eleventh_month_qty,
        MAX(CASE WHEN month_number = 12 THEN month_qty ELSE 0 END) AS twelveth_month_qty,
        -- Monthly percentages
        ROUND((MAX(CASE WHEN month_number = 1 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS first_month_per,
        ROUND((MAX(CASE WHEN month_number = 2 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS second_month_per,
        ROUND((MAX(CASE WHEN month_number = 3 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS third_month_per,
        ROUND((MAX(CASE WHEN month_number = 4 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS forth_month_per,
        ROUND((MAX(CASE WHEN month_number = 5 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS fifth_month_per,
        ROUND((MAX(CASE WHEN month_number = 6 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS sixth_month_per,
        ROUND((MAX(CASE WHEN month_number = 7 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS seventh_month_per,
        ROUND((MAX(CASE WHEN month_number = 8 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS eighth_month_per,
        ROUND((MAX(CASE WHEN month_number = 9 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS ninth_month_per,
        ROUND((MAX(CASE WHEN month_number = 10 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS tenth_month_per,
        ROUND((MAX(CASE WHEN month_number = 11 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS eleventh_month_per,
        ROUND((MAX(CASE WHEN month_number = 12 THEN month_qty ELSE 0 END) / NULLIF(total_inventory, 0)) * 100, 2) AS twelveth_month_per,
        -- Max cumulative values
        MAX(max_cumulative_reduction) AS max_cumulative_reduction,
        MAX(max_cumulative_price) AS max_cumulative_price
    FROM monthly_qty
    GROUP BY 
        ParentCode,
        category_code,
        total_inventory,
        first_show_date,
        age_months,
        age_days
)
SELECT 
    ParentCode AS product_code,
    category_code,
    total_inventory,
    first_show_date,
    age_months AS age_in_months,
    age_days AS age_in_days,
    first_month_qty,
    second_month_qty,
    third_month_qty,
    forth_month_qty,
    fifth_month_qty,
    sixth_month_qty,
    seventh_month_qty,
    eighth_month_qty,
    ninth_month_qty,
    tenth_month_qty,
    eleventh_month_qty,
    twelveth_month_qty,
    first_month_per,
    second_month_per,
    third_month_per,
    forth_month_per,
    fifth_month_per,
    sixth_month_per,
    seventh_month_per,
    eighth_month_per,
    ninth_month_per,
    tenth_month_per,
    eleventh_month_per,
    twelveth_month_per,
    max_cumulative_reduction,
    max_cumulative_price,
    ROUND((max_cumulative_reduction / NULLIF(max_cumulative_price, 0)) * 100, 2) AS discount_percentage,
    -- Additional useful columns
    ROUND(first_month_qty + second_month_qty + third_month_qty + forth_month_qty + fifth_month_qty + sixth_month_qty + seventh_month_qty + eighth_month_qty + ninth_month_qty + tenth_month_qty + eleventh_month_qty + twelveth_month_qty, 2) AS total_sold_12_months
FROM pivoted
ORDER BY ParentCode;

-- Add indexes for fast querying
ALTER TABLE salesoptimizer.twelve_month_analysis
ADD PRIMARY KEY (product_code),
ADD INDEX idx_category (category_code),
ADD INDEX idx_first_show (first_show_date),
ADD INDEX idx_age (age_in_months),
ADD INDEX idx_discount (discount_percentage DESC),
ADD INDEX idx_first_month (first_month_qty DESC),
ADD INDEX idx_total_sold (total_sold_12_months DESC);