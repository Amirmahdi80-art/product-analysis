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