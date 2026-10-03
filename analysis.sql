-- run this in powershell: & "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" --default-character-set=utf8mb4 -u root -p salesoptimizer -e "source C:/projects/project-1.0.0/salesop/analysis.sql"

DROP TABLE IF EXISTS salesoptimizer.analysis_grade_one;

CREATE TABLE salesoptimizer.analysis_grade_one AS
WITH product_signals AS (
    SELECT
        p.product_code,
        p.category_code,
        p.total_inventory,
        p.first_show_date,
        p.age_in_months,
        p.age_in_days,
        p.discount_percentage,
        p.total_sold,
        p.total_sold_12_months,

        (p.total_inventory - p.total_sold) AS remaining_inventory,
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
            WHEN c.age_in_months < 2 THEN 'داده_ناکافی'
            WHEN c.current_velocity > c.prior_velocity * 1.10 THEN 'شتاب‌گیرنده'
            WHEN c.current_velocity < c.prior_velocity * 0.90 THEN 'نزولی'
            ELSE 'ثابت'
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
        END AS velocity_gap,

        CASE
            WHEN c.total_inventory > 0 AND c.total_inventory - c.total_sold <= 0 THEN 1
            ELSE 0
        END AS completed,

        CASE
            WHEN c.discount_percentage - c.avg_discount_percentage <= 0 THEN 'طبیعی'
            WHEN c.discount_percentage - c.avg_discount_percentage <= 10 THEN 'حمایت‌شده'
            WHEN c.discount_percentage - c.avg_discount_percentage <= 25 THEN 'وابسته'
            ELSE 'در_فشار'
        END AS discount_quality

    FROM combined c
),

tagged AS (
    SELECT
        m.*,

        CASE
            WHEN m.age_in_months > 6 AND m.completed = 1 THEN 'موجودی_مرده_کامل'
            WHEN m.age_in_months > 6 AND m.completed = 0 THEN 'موجودی_مرده_مانده'
            WHEN m.age_in_months <= 6 AND m.completed = 1 THEN 'زود_تمام_شده'
            -- باز تر کردن متوسط نه صفر
            WHEN m.age_in_months >= 2
                 AND m.current_velocity = 0
                 AND m.prior_velocity = 0
                 AND m.cumulative_sell_through < 50 THEN 'متوقف_شده'


            WHEN m.rstr IS NOT NULL AND m.rstr >= 1.30
                 AND m.cdr IS NOT NULL AND m.cdr >= 0.80
                 AND m.discount_quality IN ('طبیعی', 'حمایت‌شده') THEN 'قوی'

            WHEN m.velocity_gap IS NOT NULL AND m.velocity_gap < 0.50
                 AND m.age_in_months >= 4 THEN 'خطر'

            WHEN m.rstr IS NOT NULL AND m.rstr >= 0.90
                 AND m.velocity_gap IS NOT NULL AND m.velocity_gap >= 1.0 THEN 'سلامت'

            WHEN m.rstr IS NOT NULL AND m.rstr < 0.90
                 AND m.age_in_months <= 5 THEN 'ضعیف'

            ELSE 'na'
        END AS status_tag,

        CASE
            WHEN m.age_in_months > 6 AND m.completed = 1 THEN 'آرشیو'
            WHEN m.age_in_months > 6 AND m.completed = 0 AND m.discount_quality = 'در_فشار' THEN 'حذف'
            WHEN m.age_in_months > 6 AND m.completed = 0 THEN 'پایان_فصل'

            WHEN m.age_in_months <= 6 AND m.completed = 1
                 AND m.rstr >= 1.30
                 AND m.cdr >= 0.80
                 AND m.discount_quality IN ('طبیعی', 'وابسته') THEN 'خرید'

            WHEN m.age_in_months <= 6 AND m.completed = 1 THEN 'تحقیق'

            WHEN m.age_in_months >= 2
                 AND m.current_velocity = 0
                 AND m.prior_velocity = 0 THEN 'تخفیف_50'

            WHEN m.rstr >= 1.30
                 AND m.cdr >= 0.80
                 AND m.discount_quality IN ('طبیعی', 'وابسته')
                 AND m.velocity_gap IS NOT NULL
                 AND m.velocity_gap >= 1.0 THEN 'خرید'

            WHEN m.rstr >= 1.30
                 AND m.cdr >= 0.80
                 AND m.discount_quality IN ('طبیعی', 'حمایت‌شده') THEN 'کنترل'

            WHEN m.velocity_gap IS NOT NULL AND m.velocity_gap < 0.50
                 AND m.age_in_months >= 4 THEN 'تخفیف_30'

            WHEN m.rstr >= 0.90
                 AND m.velocity_gap >= 1.0 THEN 'کنترل'

            WHEN m.rstr < 0.90 THEN 'تخفیف_20'

            ELSE 'کنترل'
        END AS action

    FROM metrics m
),

action_rollup AS (
    SELECT
        a.product_code,
        COUNT(*) AS action_count_total,
        SUM(CASE WHEN a.measurement_status IN ('کامل_شده','داده_ناکافی')
                 THEN 1 ELSE 0 END) AS action_count_measured
    FROM salesoptimizer.actions a
    GROUP BY a.product_code
),

last_completed AS (
    SELECT
        a.product_code,
        a.action_type,
        a.action_verdict,
        a.action_lift,
        a.action_margin_impact,
        ROW_NUMBER() OVER (
            PARTITION BY a.product_code
            ORDER BY a.measurement_end_date DESC, a.id DESC
        ) AS rn
    FROM salesoptimizer.actions a
    WHERE a.measurement_status = 'کامل_شده'
),

current_active AS (
    SELECT
        a.product_code,
        a.action_type,
        a.action_start_date,
        a.action_end_date,
        ROW_NUMBER() OVER (
            PARTITION BY a.product_code
            ORDER BY a.action_start_date DESC, a.id DESC
        ) AS rn
    FROM salesoptimizer.actions a
    WHERE a.action_start_date <= CURDATE()
      AND (a.action_end_date IS NULL OR a.action_end_date >= CURDATE())
)

SELECT
    t.*,
    pc.category_name AS name,
    -- Currently active action
    ca.action_type            AS active_action,
    ca.action_start_date      AS active_action_start_date,
    ca.action_end_date        AS active_action_end_date,

    -- Action history
    COALESCE(ar.action_count_total,    0) AS action_count_total,
    COALESCE(ar.action_count_measured, 0) AS action_count_measured,
    lc.action_type            AS last_action,
    lc.action_verdict         AS last_action_verdict,
    lc.action_lift            AS last_action_lift,
    lc.action_margin_impact   AS last_action_margin_impact,

    -- Ladder state (case framework)
    CASE
        WHEN t.status_tag = 'موجودی_مرده_کامل'  THEN 2
        WHEN t.status_tag = 'موجودی_مرده_مانده' THEN 3
        ELSE 0
    END AS actions_remaining,

    -- Next recommended action
    CASE
        -- No actions allowed → nothing to recommend
        WHEN t.status_tag NOT IN ('موجودی_مرده_کامل','موجودی_مرده_مانده')
            THEN NULL

        -- Already have an active action → don't recommend another
        WHEN ca.action_type IS NOT NULL THEN NULL

        -- No actions yet → recommend the baseline action from the analysis
        WHEN COALESCE(ar.action_count_total, 0) = 0 THEN t.action

        -- Last action was effective → repeat it
        WHEN lc.action_verdict = 'موثر' THEN lc.action_type

        -- Last action was ineffective → escalate
        WHEN lc.action_verdict = 'فاقد_تاثیر' AND lc.action_type = 'تخفیف_20' THEN 'تخفیف_30'
        WHEN lc.action_verdict = 'فاقد_تاثیر' AND lc.action_type = 'تخفیف_30' THEN 'تخفیف_50'
        WHEN lc.action_verdict = 'فاقد_تاثیر' THEN 'حذف'

        -- Ambiguous → try the analysis's own suggestion, unless we've already tried it
        WHEN lc.action_verdict = 'مبهم' AND lc.action_type <> t.action THEN t.action
        WHEN lc.action_verdict = 'مبهم' THEN 'کنترل'

        -- Fallback
        ELSE t.action
    END AS next_recommended_action

FROM tagged t
LEFT JOIN salesoptimizer.product_categories pc ON pc.category_code = t.category_code
LEFT JOIN action_rollup   ar ON ar.product_code = t.product_code
LEFT JOIN last_completed  lc ON lc.product_code = t.product_code AND lc.rn = 1
LEFT JOIN current_active  ca ON ca.product_code = t.product_code AND ca.rn = 1;

-- SELECT
--     product_code,
--     category_code,
--     age_in_months,
--     age_in_days,
--     total_inventory,
--     total_sold_12_months,
--     remaining_inventory,
--     remaining_months,
--     cumulative_sell_through,
--     benchmark_cumulative_sell_through,
--     rstr,
--     cdr,
--     rvr,
--     vt,
--     discount_percentage,
--     avg_discount_percentage,
--     dd,
--     discount_quality,
--     current_velocity,
--     required_future_velocity,
--     velocity_gap,
--     completed,
--     status_tag,
--     action
-- FROM tagged;