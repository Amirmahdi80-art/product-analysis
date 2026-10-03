UPDATE salesoptimizer.cumulative_product_lookup c1
JOIN (
    SELECT ParentCode, MAX(cumulative_qty) AS max_qty
    FROM salesoptimizer.cumulative_product_lookup
    GROUP BY ParentCode
) c2 ON c1.ParentCode = c2.ParentCode
SET c1.complete = 1
WHERE c2.max_qty = c1.total_inventory;