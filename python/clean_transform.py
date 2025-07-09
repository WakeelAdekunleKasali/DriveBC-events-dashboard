import pandas as pd
import os

# Read Excel Sheets from the folder
file_path = "data/DriveBC_events_2020_2024.xlsx"  # Adjust to your own file path
years = ['2020', '2021', '2022', '2023', '2024']

df_list = []
for year in years:
    try:
        df = pd.read_excel(file_path, sheet_name=year)
        df["YEAR"] = int(year)
        df_list.append(df)
        print(f"✅ Loaded sheet: {year}")
    except Exception as e:
        print(f"❌ Failed to load {year}: {e}")

# Combine all sheets
if df_list:
    df_all = pd.concat(df_list, ignore_index=True)
    print(f"\n✅ Combined shape: {df_all.shape}")
else:
    raise ValueError("❌ No sheets were loaded. Check sheet names or file path.")       

df_all = pd.concat(df_list, ignore_index=True) 

# Remove rows where critical info is missing
df_all = df_all.dropna(subset=["STATUS", "START_DATETIME"])

# Convert to datetime format
df_all["START_DATETIME"] = pd.to_datetime(df_all["START_DATETIME"], errors='coerce')
df_all["END_DATETIME"] = pd.to_datetime(df_all["END_DATETIME"], errors='coerce')
df_all["CREATED"] = pd.to_datetime(df_all["CREATED"], errors='coerce')

# Add new columns
df_all["MONTH"] = df_all["START_DATETIME"].dt.month
df_all["DAY"] = df_all["START_DATETIME"].dt.day
df_all["WEEKDAY"] = df_all["START_DATETIME"].dt.day_name()

# Save to local file
df_all.to_csv("data/drivebc_2020_2024_cleaned.csv", index=False)
print("✅ Saved cleaned combined file: data/drivebc_2020_2024_cleaned.csv")

import matplotlib.pyplot as plt

# Group and reshape
pivot = df_all.groupby(["YEAR", "SEVERITY"]).size().unstack(fill_value=0)

# Make the plot
pivot.plot(kind="bar", figsize=(10, 6), stacked=True)
plt.title("DriveBC Road Events by Severity (2020–2024)")
plt.xlabel("Year")
plt.ylabel("Number of Events")
plt.legend(title="Severity")
plt.tight_layout()
plt.savefig("data/severity_by_year.png")
plt.show()




