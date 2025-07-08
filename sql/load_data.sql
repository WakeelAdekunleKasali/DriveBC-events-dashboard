ALTER TABLE drivebcevents DROP CONSTRAINT IF EXISTS drivebcevents_pkey;

-- Load the data from CSV file
-- Adjust the path as necessary
\COPY drivebcevents FROM '/absolute/path/to/drivebc_2020_2024_cleaned.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');

-- Verify number of rows inserted
SELECT COUNT(*) FROM drivebcevents;

-- Optional: Preview some rows
SELECT * FROM drivebcevents LIMIT 10;