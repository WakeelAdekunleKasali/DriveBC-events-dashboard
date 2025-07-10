import pandas as pd
from sqlalchemy import create_engine

# Load the cleaned CSV
file_path = "drivebc_2020_2024_cleaned.csv"
df = pd.read_csv(file_path, low_memory=False)

# Connect to PostgreSQL (no password for local user assumed)
engine = create_engine("postgresql://wakeelkasali@localhost:5432/drivebc_project")

# Upload only if the table already exists — DO NOT overwrite
# Append to existing table safely
df.to_sql("drivebc_events", con=engine, if_exists="append", index=False, method='multi')

print("Data successfully uploaded to 'drivebc_events'")