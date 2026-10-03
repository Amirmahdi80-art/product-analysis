SET SQL_SAFE_UPDATES = 0;
delete FROM salesoptimizer.products_lookup  where product_code is not null;
INSERT INTO salesoptimizer.products_lookup 
    (product_code, category_code, total_inventory, first_entered_inventory_date, 
     first_show_date, days_since_entry, days_since_show)
SELECT 
    ti.product_code, 
    ti.category_code, 
    ti.total_inventory, 
    ti.first_entered_inventory_date, 
    fs.first_show_date, 
    DATEDIFF('2026-09-11', ti.first_entered_inventory_date) AS days_since_entry, 
    DATEDIFF('2026-09-11', fs.first_show_date) AS days_since_show
FROM salesoptimizer.total_inventory ti 
INNER JOIN salesoptimizer.first_show fs 
    ON fs.product_code = ti.product_code;