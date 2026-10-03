create table salesoptimizer.cumulative_product_lookup as 
WITH ctr AS (
    SELECT 
        ip.*,
        pl.product_code,
        pl.category_code,
        pl.total_inventory,
        pl.first_entered_inventory_date,
        pl.first_show_date,
        pl.days_since_entry,
        pl.days_since_show,
        pl.days_since_entry - days_since_show as date_diff,
        -- Cumulative columns
        SUM(ip.MajorUnitQuantity) OVER (PARTITION BY ip.ParentCode ORDER BY ip.Expr2) AS cumulative_qty,
        SUM(ip.NetPrice) OVER (PARTITION BY ip.ParentCode ORDER BY ip.Expr2) AS cumulative_netprice,
        SUM(ip.ReductionAmount) OVER (PARTITION BY ip.ParentCode ORDER BY ip.Expr2) AS cumulative_reduction,
        SUM(ip.AdditionAmount) OVER (PARTITION BY ip.ParentCode ORDER BY ip.Expr2) AS cumulative_addition,
        SUM(ip.Price) OVER (PARTITION BY ip.ParentCode ORDER BY ip.Expr2) AS cumulative_price
    FROM salesoptimizer.invoiceitems_parent ip
    INNER JOIN salesoptimizer.products_lookup pl
        ON ip.ParentCode = pl.product_code
    -- WHERE ip.Expr2 > pl.first_show_date
)
SELECT ParentCode, Expr1, Name, category_code, Expr2, SalesOfficeID, MajorUnitQuantity, total_inventory, first_entered_inventory_date, first_show_date, days_since_entry, days_since_show, date_diff, cumulative_qty, cumulative_netprice, cumulative_reduction, cumulative_addition, cumulative_price
FROM ctr
ORDER BY Expr2;