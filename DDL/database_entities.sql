-- Create or ensure the existence of the 'import' schema
CREATE SCHEMA IF NOT EXISTS import;

-- Create or ensure the existence of the 'exchange_rates_table' table within the 'import' schema
CREATE TABLE IF NOT EXISTS "import".exchange_rates_table (
    id SERIAL,
    currency_date DATE NOT NULL,
    currency_symbol VARCHAR NOT NULL,
    currency_rate FLOAT4 NOT NULL,
    UNIQUE(currency_date, currency_symbol) -- Ensure uniqueness of (currency_date, currency_symbol) pairs
);

-- Select distinct currency dates from the 'exchange_rates_table' table within the 'import' schema
SELECT DISTINCT currency_date FROM "import".exchange_rates_table;

-- Insert or update exchange rates data into the 'exchange_rates_table' table
INSERT INTO "import".exchange_rates_table
    (currency_date, currency_symbol, currency_rate)
    VALUES (%s, %s, %s)
    ON CONFLICT (currency_date, currency_symbol) DO UPDATE
    SET currency_rate = EXCLUDED.currency_rate
    RETURNING currency_date;

-- Create or ensure the existence of the 'monthly_stats' materialized view within the 'import' schema
CREATE MATERIALIZED VIEW IF NOT EXISTS "import".monthly_stats AS
    SELECT
        MIN(currency_rate) AS min_rate,
        MAX(currency_rate) AS max_rate,
        AVG(currency_rate) AS avg_rate,
        EXTRACT(MONTH FROM currency_date) AS month,
        EXTRACT(YEAR FROM currency_date) AS year
    FROM
        "import".exchange_rates_table
    GROUP BY
        EXTRACT(MONTH FROM currency_date),
        EXTRACT(YEAR FROM currency_date);

-- Refresh the 'monthly_stats' materialized view to reflect the latest data
REFRESH MATERIALIZED VIEW "import".monthly_stats;

-- Select all columns from the 'monthly_stats' materialized view within the 'import' schema
SELECT *,
    TO_DATE(CONCAT(year, '-', month, '-01'), 'YYYY-MM-DD') AS full_date
FROM "import".monthly_stats
ORDER BY full_date ASC;

-- Create or replace the 'today_rates_view' view within the 'import' schema
CREATE OR REPLACE VIEW "import".today_rates_view AS
    SELECT *
    FROM "import".exchange_rates_table
    WHERE currency_date = CURRENT_DATE;

-- Select all columns from the 'today_rates_view' view within the 'import' schema
SELECT *
FROM "import".today_rates_view;
