import pandas as pd
from sqlalchemy import create_engine

# Create engine using SQLAlchemy (recommended for pandas)
engine = create_engine("postgresql+psycopg2://..../drivebcevent_project")

# Read entire table into a DataFrame
df = pd.read_sql("SELECT * FROM drivebcevents;", engine)

# Export to CSV
df.to_csv("drivebcevents.csv", index=False)