-- run this in powershell: & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" --default-character-set=utf8mb4 -u root -p salesoptimizer -e "source C:/projects/project-1.0.0/salesop/soft_sql_three_point_five.sql"

UPDATE salesoptimizer.cumulative_product_lookup c1
JOIN (
    SELECT 
        ParentCode, 
        MAX(cumulative_qty) AS max_cumulative_qty
    FROM salesoptimizer.cumulative_product_lookup
    GROUP BY ParentCode
    HAVING MAX(cumulative_qty) > MAX(total_inventory)
) c2 ON c1.ParentCode = c2.ParentCode
SET c1.total_inventory = c2.max_cumulative_qty;

DELETE FROM salesoptimizer.cumulative_product_lookup 
WHERE ParentCode IN (
    2559511001,
    2559511002,
    2559511101,
    2559511102,
    2559511201,
    2559511202
);

update salesoptimizer.cumulative_product_lookup 
set
date_diff = 0,
first_entered_inventory_date = first_show_date,
days_since_entry = days_since_show
where days_since_show > days_since_entry;