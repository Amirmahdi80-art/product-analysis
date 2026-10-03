create table category_contr_avgs as
SELECT 
    MAX(pc.category_name) AS category_name,
    MAX(tma.category_code) AS category_code,

    ROUND(AVG(first_month_qty), 2) AS avg_first_month_qty,
    ROUND(AVG(second_month_qty), 2) AS avg_second_month_qty,
    ROUND(AVG(third_month_qty), 2) AS avg_third_month_qty,
    ROUND(AVG(forth_month_qty), 2) AS avg_forth_month_qty,
    ROUND(AVG(fifth_month_qty), 2) AS avg_fifth_month_qty,
    ROUND(AVG(sixth_month_qty), 2) AS avg_sixth_month_qty,
    ROUND(AVG(seventh_month_qty), 2) AS avg_seventh_month_qty,
    ROUND(AVG(eighth_month_qty), 2) AS avg_eighth_month_qty,
    ROUND(AVG(ninth_month_qty), 2) AS avg_ninth_month_qty,
    ROUND(AVG(tenth_month_qty), 2) AS avg_tenth_month_qty,
    ROUND(AVG(eleventh_month_qty), 2) AS avg_eleventh_month_qty,
    ROUND(AVG(twelveth_month_qty), 2) AS avg_twelveth_month_qty,


    ROUND(AVG(first_month_per), 2) AS avg_first_month_per,
    ROUND(AVG(second_month_per), 2) AS avg_second_month_per,
    ROUND(AVG(third_month_per), 2) AS avg_third_month_per,
    ROUND(AVG(forth_month_per), 2) AS avg_forth_month_per,
    ROUND(AVG(fifth_month_per), 2) AS avg_fifth_month_per,
    ROUND(AVG(sixth_month_per), 2) AS avg_sixth_month_per,
    ROUND(AVG(seventh_month_per), 2) AS avg_seventh_month_per,
    ROUND(AVG(eighth_month_per), 2) AS avg_eighth_month_per,
    ROUND(AVG(ninth_month_per), 2) AS avg_ninth_month_per,
    ROUND(AVG(tenth_month_per), 2) AS avg_tenth_month_per,
    ROUND(AVG(eleventh_month_per), 2) AS avg_eleventh_month_per,
    ROUND(AVG(twelveth_month_per), 2) AS avg_twelveth_month_per,


    ROUND(AVG(discount_percentage), 2) AS avg_discount_percentage

FROM salesoptimizer.twelve_month_analysis tma

LEFT JOIN salesoptimizer.product_categories pc
    ON tma.category_code = pc.category_code

GROUP BY tma.category_code;