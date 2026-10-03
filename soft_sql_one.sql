-- run this in powershell: & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" --default-character-set=utf8mb4 -u root -p salesoptimizer -e "source C:/projects/project-1.0.0/salesop/soft_sql_one.sql"

-- Clean up if re-running in the same session
DROP TEMPORARY TABLE IF EXISTS total_inventory_and_first_entered_inventory_date;
DROP TEMPORARY TABLE IF EXISTS first_show_date;
DROP TEMPORARY TABLE IF EXISTS data_source;

-- Step 1: total inventory + first entered inventory date (bought)
CREATE TEMPORARY TABLE total_inventory_and_first_entered_inventory_date AS
SELECT 
    SUBSTRING(Code, 1, LENGTH(Code) - 2) AS product_code,
    MAX(SUBSTRING(Code, 4, 2)) AS category_code,
    MIN(Tarikh) AS first_entered_inventory_date,
    SUM(MajorUnitQuantity) AS total_inventory
FROM salesoptimizer.voucher
WHERE InventoryVoucherSpecificationRef = 2
GROUP BY SUBSTRING(Code, 1, LENGTH(Code) - 2);

-- Step 2: first show date (first sent to branches)
CREATE TEMPORARY TABLE first_show_date AS
SELECT 
    SUBSTRING(Code, 1, LENGTH(Code) - 2) AS product_code,
    MAX(SUBSTRING(Code, 4, 2)) AS category_code,
    MIN(Tarikh) AS first_show_date
FROM salesoptimizer.voucher
WHERE InventoryVoucherSpecificationRef = 68
GROUP BY SUBSTRING(Code, 1, LENGTH(Code) - 2);

-- Step 3: join them
CREATE TEMPORARY TABLE data_source AS
SELECT 
    tiafeid.product_code,
    tiafeid.category_code,
    tiafeid.total_inventory,
    tiafeid.first_entered_inventory_date,
    fsd.first_show_date
FROM total_inventory_and_first_entered_inventory_date tiafeid
INNER JOIN first_show_date fsd 
    ON fsd.product_code = tiafeid.product_code
   AND fsd.category_code = tiafeid.category_code;

-- Step 1: Clear existing data
TRUNCATE TABLE salesoptimizer.products_lookup;

-- Step 2: Insert fresh data
INSERT INTO salesoptimizer.products_lookup 
    (product_code, category_code, total_inventory, 
     first_entered_inventory_date, first_show_date, 
     days_since_entry, days_since_show)
SELECT 
    product_code,
    category_code,
    total_inventory,
    first_entered_inventory_date,
    first_show_date,
    DATEDIFF(CURDATE(), first_entered_inventory_date) AS days_since_entry,
    DATEDIFF(CURDATE(), first_show_date) AS days_since_show
FROM data_source;