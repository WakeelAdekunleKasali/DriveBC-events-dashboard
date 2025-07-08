-- 1. Preview a few rows
SELECT * FROM drivebcevents LIMIT 10;

-- 2. Check how many rows are in the table
SELECT COUNT(*) FROM drivebcevents;

-- 3. List distinct event types
SELECT DISTINCT "EVENT_TYPE" FROM drivebcevents;

-- 4. Count events per year
SELECT "YEAR", COUNT(*) 
FROM drivebcevents 
GROUP BY "YEAR" 
ORDER BY "YEAR";

-- 5. Count missing values in ROAD_STATE
SELECT "ROAD_STATE", COUNT(*) 
FROM drivebcevents 
GROUP BY "ROAD_STATE";