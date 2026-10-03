DROP TABLE IF EXISTS salesoptimizer.actions;

CREATE TABLE salesoptimizer.actions (
    id                      BIGINT        NOT NULL AUTO_INCREMENT,

    -- Identity
    product_code            VARCHAR(64)   NOT NULL,
    action_number           INT           NOT NULL,

    -- What the action is
    action_type             VARCHAR(64)   NOT NULL,
    action_target           VARCHAR(64)   NULL,      -- store ID for TRANSFER, else NULL

    -- When
    action_created_date     DATE          NOT NULL,
    action_start_date       DATE          NOT NULL,
    action_end_date         DATE          NULL,      -- NULL = open-ended

    -- Measurement
    measurement_start_date  DATE          NULL,
    measurement_end_date    DATE          NULL,
    measurement_status      VARCHAR(20)   NOT NULL DEFAULT 'در انتظار',
    action_lift             DECIMAL(12,4) NULL,
    action_margin_impact    DECIMAL(14,4) NULL,
    action_verdict          VARCHAR(16)   NULL,

    -- Who / notes
    created_by              VARCHAR(64)   NULL,
    notes                   TEXT          NULL,

    PRIMARY KEY (id),
    UNIQUE KEY uq_actions_product_number (product_code, action_number),
    KEY idx_actions_product        (product_code),
    KEY idx_actions_active         (product_code, action_start_date, action_end_date),
    KEY idx_actions_measurement    (product_code, measurement_status, measurement_end_date),
    KEY idx_actions_type           (action_type),
    CONSTRAINT chk_actions_measurement_status
        CHECK (measurement_status IN ('در انتظار','فعال','کامل شده','داده_ناکافی')),
    CONSTRAINT chk_actions_verdict
        CHECK (action_verdict IS NULL
               OR action_verdict IN ('موثر','فاقد تاثیر','مبهم'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;