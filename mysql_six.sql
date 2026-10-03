SET SQL_SAFE_UPDATES = 0;
delete FROM salesoptimizer.first_show where product_code is not null;
INSERT INTO salesoptimizer.first_show 
    (product_code, category_code, first_show_date)
SELECT 
    MAX(substring(Code, 1, length(Code) - 2)) as product_code,
    MAX(substring(Code, 4, 2)) as category_code,
    min(Tarikh) as first_show_date
FROM salesoptimizer.voucher 
WHERE StoreID in (6, 13, 16, 18, 17, 3, 10, 15)
GROUP BY substring(Code, 1, length(Code) - 2);
