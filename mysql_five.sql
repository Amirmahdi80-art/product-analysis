SET SQL_SAFE_UPDATES = 0;
delete FROM salesoptimizer.total_inventory where product_code is not null;
INSERT INTO salesoptimizer.total_inventory 
    (product_code, category_code, total_inventory, first_entered_inventory_date)
SELECT 
    MAX(substring(Code, 1, length(Code) - 2)) as product_code,
    MAX(substring(Code, 4, 2)) as category_code,
    sum(MajorUnitQuantity) as total_inventory,
    min(Tarikh) as first_entered_inventory_date
FROM salesoptimizer.voucher 
WHERE InventoryVoucherSpecificationRef in (2, 18) 
GROUP BY substring(Code, 1, length(Code) - 2);