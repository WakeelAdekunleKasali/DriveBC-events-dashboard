-- Create the project database
-- Note: If running manually, do this in psql
CREATE DATABASE drivebcevent_project;

-- Connect to the database:
-- \c drivebcevent_project

-- Create the drivebcevents table
CREATE TABLE drivebcevents (
    "Unnamed: 0" TEXT,
    "ID" TEXT PRIMARY KEY,
    "STATUS" VARCHAR(20),
    "HEADLINE" TEXT,
    "EVENT_TYPE" VARCHAR(50),
    "EVENT_SUBTYPE" VARCHAR(50),
    "SEVERITY" VARCHAR(20),
    "CREATED" TIMESTAMP,
    "UPDATED" TIMESTAMP,
    "TIME_ZONE" VARCHAR(50),
    "START_DATETIME" TIMESTAMP,
    "END_DATETIME" TIMESTAMP,
    "OPEN511_DB_UPDATE_TIMESTAMP" TIMESTAMP,
    "AREA_NAME" VARCHAR(100),
    "AREA_ID" TEXT,
    "AREA_LINK" TEXT,
    "HEAD_LATITUDE" DOUBLE PRECISION,
    "HEAD_LONGITUDE" DOUBLE PRECISION,
    "TAIL_LATITUDE" DOUBLE PRECISION,
    "TAIL_LONGITUDE" DOUBLE PRECISION,
    "ROAD_NAME" VARCHAR(100),
    "ROAD_FROM_DESCRIPTION" TEXT,
    "ROAD_TO_DESCRIPTION" TEXT,
    "ROAD_DIRECTION" VARCHAR(10),
    "ROAD_STATE" VARCHAR(50),
    "ROAD_DELAY" TEXT,
    "YEAR" INTEGER,
    "IVR_MESSAGE" TEXT,
    "MONTH" INTEGER,
    "DAY" INTEGER,
    "WEEKDAY" VARCHAR(20)
);

-- Create indexes for query optimization
CREATE INDEX idx_year ON drivebcevents("YEAR");
CREATE INDEX idx_area_name ON drivebcevents("AREA_NAME");
CREATE INDEX idx_event_type ON drivebcevents("EVENT_TYPE");
CREATE INDEX idx_severity ON drivebcevents("SEVERITY");