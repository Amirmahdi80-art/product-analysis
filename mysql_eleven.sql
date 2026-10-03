update salesoptimizer.cumulative_product_lookup 
set
date_diff = 0,
first_entered_inventory_date = first_show_date,
days_since_entry = days_since_show
where days_since_show > days_since_entry;