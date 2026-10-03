create table salesoptimizer.first_analysis as
WITH product_signals AS (
    SELECT
        p.product_code,
        p.category_code,
        p.total_inventory,
        p.first_show_date,
        p.age_in_months,
        p.age_in_days,
        p.discount_percentage,
        p.total_sold_12_months,

        (p.total_inventory - p.total_sold_12_months) AS remaining_inventory,
        GREATEST(6 - p.age_in_months, 0) AS remaining_months,

        CASE
            WHEN p.age_in_months >= 12 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per +
                p.fifth_month_per + p.sixth_month_per + p.seventh_month_per + p.eighth_month_per +
                p.ninth_month_per + p.tenth_month_per + p.eleventh_month_per + p.twelveth_month_per
            WHEN p.age_in_months = 11 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per +
                p.fifth_month_per + p.sixth_month_per + p.seventh_month_per + p.eighth_month_per +
                p.ninth_month_per + p.tenth_month_per + p.eleventh_month_per
            WHEN p.age_in_months = 10 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per +
                p.fifth_month_per + p.sixth_month_per + p.seventh_month_per + p.eighth_month_per +
                p.ninth_month_per + p.tenth_month_per
            WHEN p.age_in_months = 9 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per +
                p.fifth_month_per + p.sixth_month_per + p.seventh_month_per + p.eighth_month_per +
                p.ninth_month_per
            WHEN p.age_in_months = 8 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per +
                p.fifth_month_per + p.sixth_month_per + p.seventh_month_per + p.eighth_month_per
            WHEN p.age_in_months = 7 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per +
                p.fifth_month_per + p.sixth_month_per + p.seventh_month_per
            WHEN p.age_in_months = 6 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per +
                p.fifth_month_per + p.sixth_month_per
            WHEN p.age_in_months = 5 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per +
                p.fifth_month_per
            WHEN p.age_in_months = 4 THEN
                p.first_month_per + p.second_month_per + p.third_month_per + p.forth_month_per
            WHEN p.age_in_months = 3 THEN
                p.first_month_per + p.second_month_per + p.third_month_per
            WHEN p.age_in_months = 2 THEN
                p.first_month_per + p.second_month_per
            WHEN p.age_in_months = 1 THEN
                p.first_month_per
            ELSE 0
        END AS cumulative_sell_through,

        CASE
            WHEN p.age_in_months >= 12 THEN p.total_sold_12_months
            WHEN p.age_in_months = 11 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty +
                p.fifth_month_qty + p.sixth_month_qty + p.seventh_month_qty + p.eighth_month_qty +
                p.ninth_month_qty + p.tenth_month_qty + p.eleventh_month_qty
            WHEN p.age_in_months = 10 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty +
                p.fifth_month_qty + p.sixth_month_qty + p.seventh_month_qty + p.eighth_month_qty +
                p.ninth_month_qty + p.tenth_month_qty
            WHEN p.age_in_months = 9 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty +
                p.fifth_month_qty + p.sixth_month_qty + p.seventh_month_qty + p.eighth_month_qty +
                p.ninth_month_qty
            WHEN p.age_in_months = 8 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty +
                p.fifth_month_qty + p.sixth_month_qty + p.seventh_month_qty + p.eighth_month_qty
            WHEN p.age_in_months = 7 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty +
                p.fifth_month_qty + p.sixth_month_qty + p.seventh_month_qty
            WHEN p.age_in_months = 6 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty +
                p.fifth_month_qty + p.sixth_month_qty
            WHEN p.age_in_months = 5 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty +
                p.fifth_month_qty
            WHEN p.age_in_months = 4 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty + p.forth_month_qty
            WHEN p.age_in_months = 3 THEN
                p.first_month_qty + p.second_month_qty + p.third_month_qty
            WHEN p.age_in_months = 2 THEN
                p.first_month_qty + p.second_month_qty
            WHEN p.age_in_months = 1 THEN
                p.first_month_qty
            ELSE 0
        END AS cumulative_qty,

        CASE
            WHEN p.age_in_months >= 12 THEN p.twelveth_month_qty
            WHEN p.age_in_months = 11 THEN p.eleventh_month_qty
            WHEN p.age_in_months = 10 THEN p.tenth_month_qty
            WHEN p.age_in_months = 9 THEN p.ninth_month_qty
            WHEN p.age_in_months = 8 THEN p.eighth_month_qty
            WHEN p.age_in_months = 7 THEN p.seventh_month_qty
            WHEN p.age_in_months = 6 THEN p.sixth_month_qty
            WHEN p.age_in_months = 5 THEN p.fifth_month_qty
            WHEN p.age_in_months = 4 THEN p.forth_month_qty
            WHEN p.age_in_months = 3 THEN p.third_month_qty
            WHEN p.age_in_months = 2 THEN p.second_month_qty
            WHEN p.age_in_months = 1 THEN p.first_month_qty
            ELSE 0
        END AS current_velocity,

        CASE
            WHEN p.age_in_months >= 12 THEN p.eleventh_month_qty
            WHEN p.age_in_months = 11 THEN p.tenth_month_qty
            WHEN p.age_in_months = 10 THEN p.ninth_month_qty
            WHEN p.age_in_months = 9 THEN p.eighth_month_qty
            WHEN p.age_in_months = 8 THEN p.seventh_month_qty
            WHEN p.age_in_months = 7 THEN p.sixth_month_qty
            WHEN p.age_in_months = 6 THEN p.fifth_month_qty
            WHEN p.age_in_months = 5 THEN p.forth_month_qty
            WHEN p.age_in_months = 4 THEN p.third_month_qty
            WHEN p.age_in_months = 3 THEN p.second_month_qty
            WHEN p.age_in_months = 2 THEN p.first_month_qty
            ELSE 0
        END AS prior_velocity

    FROM salesoptimizer.twelve_month_analysis p
),

benchmark_signals AS (
    SELECT
        b.category_code,
        b.avg_first_month_per,
        b.avg_second_month_per,
        b.avg_third_month_per,
        b.avg_forth_month_per,
        b.avg_fifth_month_per,
        b.avg_sixth_month_per,
        b.avg_seventh_month_per,
        b.avg_eighth_month_per,
        b.avg_ninth_month_per,
        b.avg_tenth_month_per,
        b.avg_eleventh_month_per,
        b.avg_twelveth_month_per,
        b.avg_first_month_qty,
        b.avg_second_month_qty,
        b.avg_third_month_qty,
        b.avg_forth_month_qty,
        b.avg_fifth_month_qty,
        b.avg_sixth_month_qty,
        b.avg_seventh_month_qty,
        b.avg_eighth_month_qty,
        b.avg_ninth_month_qty,
        b.avg_tenth_month_qty,
        b.avg_eleventh_month_qty,
        b.avg_twelveth_month_qty,
        b.avg_discount_percentage
    FROM salesoptimizer.category_contr_avgs b
),

combined AS (
    SELECT
        ps.*,
        bs.avg_discount_percentage,

        CASE
            WHEN ps.age_in_months >= 12 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per +
                bs.avg_fifth_month_per + bs.avg_sixth_month_per + bs.avg_seventh_month_per + bs.avg_eighth_month_per +
                bs.avg_ninth_month_per + bs.avg_tenth_month_per + bs.avg_eleventh_month_per + bs.avg_twelveth_month_per
            WHEN ps.age_in_months = 11 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per +
                bs.avg_fifth_month_per + bs.avg_sixth_month_per + bs.avg_seventh_month_per + bs.avg_eighth_month_per +
                bs.avg_ninth_month_per + bs.avg_tenth_month_per + bs.avg_eleventh_month_per
            WHEN ps.age_in_months = 10 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per +
                bs.avg_fifth_month_per + bs.avg_sixth_month_per + bs.avg_seventh_month_per + bs.avg_eighth_month_per +
                bs.avg_ninth_month_per + bs.avg_tenth_month_per
            WHEN ps.age_in_months = 9 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per +
                bs.avg_fifth_month_per + bs.avg_sixth_month_per + bs.avg_seventh_month_per + bs.avg_eighth_month_per +
                bs.avg_ninth_month_per
            WHEN ps.age_in_months = 8 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per +
                bs.avg_fifth_month_per + bs.avg_sixth_month_per + bs.avg_seventh_month_per + bs.avg_eighth_month_per
            WHEN ps.age_in_months = 7 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per +
                bs.avg_fifth_month_per + bs.avg_sixth_month_per + bs.avg_seventh_month_per
            WHEN ps.age_in_months = 6 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per +
                bs.avg_fifth_month_per + bs.avg_sixth_month_per
            WHEN ps.age_in_months = 5 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per +
                bs.avg_fifth_month_per
            WHEN ps.age_in_months = 4 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per + bs.avg_forth_month_per
            WHEN ps.age_in_months = 3 THEN
                bs.avg_first_month_per + bs.avg_second_month_per + bs.avg_third_month_per
            WHEN ps.age_in_months = 2 THEN
                bs.avg_first_month_per + bs.avg_second_month_per
            WHEN ps.age_in_months = 1 THEN
                bs.avg_first_month_per
            ELSE 0
        END AS benchmark_cumulative_sell_through,

        CASE
            WHEN ps.age_in_months >= 12 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty +
                bs.avg_fifth_month_qty + bs.avg_sixth_month_qty + bs.avg_seventh_month_qty + bs.avg_eighth_month_qty +
                bs.avg_ninth_month_qty + bs.avg_tenth_month_qty + bs.avg_eleventh_month_qty + bs.avg_twelveth_month_qty
            WHEN ps.age_in_months = 11 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty +
                bs.avg_fifth_month_qty + bs.avg_sixth_month_qty + bs.avg_seventh_month_qty + bs.avg_eighth_month_qty +
                bs.avg_ninth_month_qty + bs.avg_tenth_month_qty + bs.avg_eleventh_month_qty
            WHEN ps.age_in_months = 10 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty +
                bs.avg_fifth_month_qty + bs.avg_sixth_month_qty + bs.avg_seventh_month_qty + bs.avg_eighth_month_qty +
                bs.avg_ninth_month_qty + bs.avg_tenth_month_qty
            WHEN ps.age_in_months = 9 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty +
                bs.avg_fifth_month_qty + bs.avg_sixth_month_qty + bs.avg_seventh_month_qty + bs.avg_eighth_month_qty +
                bs.avg_ninth_month_qty
            WHEN ps.age_in_months = 8 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty +
                bs.avg_fifth_month_qty + bs.avg_sixth_month_qty + bs.avg_seventh_month_qty + bs.avg_eighth_month_qty
            WHEN ps.age_in_months = 7 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty +
                bs.avg_fifth_month_qty + bs.avg_sixth_month_qty + bs.avg_seventh_month_qty
            WHEN ps.age_in_months = 6 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty +
                bs.avg_fifth_month_qty + bs.avg_sixth_month_qty
            WHEN ps.age_in_months = 5 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty +
                bs.avg_fifth_month_qty
            WHEN ps.age_in_months = 4 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty + bs.avg_forth_month_qty
            WHEN ps.age_in_months = 3 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty + bs.avg_third_month_qty
            WHEN ps.age_in_months = 2 THEN
                bs.avg_first_month_qty + bs.avg_second_month_qty
            WHEN ps.age_in_months = 1 THEN
                bs.avg_first_month_qty
            ELSE 0
        END AS benchmark_cumulative_qty,

        CASE
            WHEN ps.age_in_months >= 12 THEN bs.avg_twelveth_month_qty
            WHEN ps.age_in_months = 11 THEN bs.avg_eleventh_month_qty
            WHEN ps.age_in_months = 10 THEN bs.avg_tenth_month_qty
            WHEN ps.age_in_months = 9 THEN bs.avg_ninth_month_qty
            WHEN ps.age_in_months = 8 THEN bs.avg_eighth_month_qty
            WHEN ps.age_in_months = 7 THEN bs.avg_seventh_month_qty
            WHEN ps.age_in_months = 6 THEN bs.avg_sixth_month_qty
            WHEN ps.age_in_months = 5 THEN bs.avg_fifth_month_qty
            WHEN ps.age_in_months = 4 THEN bs.avg_forth_month_qty
            WHEN ps.age_in_months = 3 THEN bs.avg_third_month_qty
            WHEN ps.age_in_months = 2 THEN bs.avg_second_month_qty
            WHEN ps.age_in_months = 1 THEN bs.avg_first_month_qty
            ELSE 0
        END AS benchmark_current_month_qty

    FROM product_signals ps
    LEFT JOIN benchmark_signals bs
        ON ps.category_code = bs.category_code
),

metrics AS (
    SELECT
        c.*,

        CASE
            WHEN c.benchmark_cumulative_sell_through > 0
            THEN c.cumulative_sell_through / c.benchmark_cumulative_sell_through
            ELSE NULL
        END AS rstr,

        CASE
            WHEN c.benchmark_cumulative_qty > 0
            THEN c.cumulative_qty / c.benchmark_cumulative_qty
            ELSE NULL
        END AS cdr,

        CASE
            WHEN c.benchmark_current_month_qty > 0
            THEN c.current_velocity / c.benchmark_current_month_qty
            ELSE NULL
        END AS rvr,

        CASE
            WHEN c.age_in_months < 2 THEN 'INSUFFICIENT_DATA'
            WHEN c.current_velocity > c.prior_velocity * 1.10 THEN 'ACCELERATING'
            WHEN c.current_velocity < c.prior_velocity * 0.90 THEN 'DECLINING'
            ELSE 'STABLE'
        END AS vt,

        (c.discount_percentage - c.avg_discount_percentage) AS dd,

        CASE
            WHEN c.remaining_months > 0
            THEN c.remaining_inventory / c.remaining_months
            ELSE NULL
        END AS required_future_velocity,

        CASE
            WHEN c.remaining_months > 0 AND c.remaining_inventory > 0
            THEN c.current_velocity / (c.remaining_inventory / c.remaining_months)
            ELSE NULL
        END AS velocity_gap

    FROM combined c
),

tagged AS (
    SELECT
        m.*,

        CASE
            WHEN m.age_in_months > 6 THEN 'DEAD_STOCK'

            WHEN m.age_in_months >= 2
                 AND m.current_velocity = 0
                 AND m.prior_velocity = 0
                 AND m.cumulative_sell_through < 50 THEN 'STALLED'

            -- PLACEHOLDER THRESHOLDS: 1.30, 0.80, 10 — must be validated
            WHEN m.rstr IS NOT NULL AND m.rstr >= 1.30
                 AND m.cdr IS NOT NULL AND m.cdr >= 0.80
                 AND m.dd <= 10 THEN 'STRONG'

            -- PLACEHOLDER THRESHOLD: 0.50
            WHEN m.velocity_gap IS NOT NULL AND m.velocity_gap < 0.50
                 AND m.age_in_months >= 4 THEN 'RISK'

            -- PLACEHOLDER THRESHOLDS: 0.90, 1.0
            WHEN m.rstr IS NOT NULL AND m.rstr >= 0.90
                 AND m.velocity_gap IS NOT NULL AND m.velocity_gap >= 1.0 THEN 'HEALTHY'

            -- PLACEHOLDER THRESHOLD: 0.90
            WHEN m.rstr IS NOT NULL AND m.rstr < 0.90
                 AND m.age_in_months <= 5 THEN 'UNDERPERFORMING'

            ELSE 'UNDERPERFORMING'
        END AS status_tag,

        CASE
            WHEN m.age_in_months > 6 THEN 'DISCOUNT_CLEARANCE'

            WHEN m.age_in_months >= 2
                 AND m.current_velocity = 0
                 AND m.prior_velocity = 0 THEN 'DISCOUNT_60'

            WHEN m.rstr >= 1.30
                 AND m.cdr >= 0.80
                 AND m.dd <= 10
                 AND m.velocity_gap IS NOT NULL
                 AND m.velocity_gap >= 1.0 THEN 'REFILL'

            WHEN m.rstr >= 1.30
                 AND m.cdr >= 0.80
                 AND m.dd <= 10 THEN 'MONITOR'

            WHEN m.velocity_gap IS NOT NULL AND m.velocity_gap < 0.50
                 AND m.age_in_months >= 4 THEN 'DISCOUNT_50'

            WHEN m.rstr >= 0.90
                 AND m.velocity_gap >= 1.0 THEN 'MONITOR'

            WHEN m.rstr < 0.90 THEN 'DISCOUNT_30'

            ELSE 'MONITOR'
        END AS action

    FROM metrics m
)

SELECT
    product_code,
    category_code,
    age_in_months,
    age_in_days,
    total_inventory,
    total_sold_12_months,
    remaining_inventory,
    remaining_months,
    cumulative_sell_through,
    benchmark_cumulative_sell_through,
    rstr,
    cdr,
    rvr,
    vt,
    discount_percentage,
    avg_discount_percentage,
    dd,
    current_velocity,
    required_future_velocity,
    velocity_gap,
    status_tag,
    action
FROM tagged;