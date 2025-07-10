# 🚗 DriveBC Events Analysis (2020–2024)

This project analyzes roadway events across British Columbia (BC) between 2020 and 2024 using publicly available datasets. It includes steps for data extraction, cleaning, SQL database loading, exploratory analysis in Python, and interactive dashboarding with Tableau.

---

## 📊 Tableau Dashboard

Explore the interactive dashboard on Tableau Public:  
🔗 [View Dashboard](https://public.tableau.com/views/DriveBC/Dashboard2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

The dashboard displays:
- Quarterly trends of DriveBC events by **Area Name**
- Distribution by **Event Type** (e.g., Incident, Road Condition, Construction, Weather)
- Filter options to compare regions
- Key indicators for infrastructure monitoring

📷 Dashboard Preview:

![Dashboard Preview](tableau/dashboard_screenshots/drivebc_dashboard_preview.png)

---

## 📁 Project Structure

## 🗂️ Data Sources

- **Dataset**: [DriveBC Events (2020–2024)](https://open.canada.ca/data/en/dataset/cdf6ab31-fa03-479a-b6e0-f9a0c71edf91) from the Government of Canada Open Data Portal  
- **License**: [Open Government Licence – British Columbia](https://www2.gov.bc.ca/gov/content/data/policy-standards/data-policies/open-data/open-government-licence-bc)

This project uses publicly available data distributed under the terms of the Open Government Licence – BC.

---

## ⚙️ Technologies Used

- **Python** – pandas, seaborn, matplotlib, sqlalchemy  
- **SQL** – PostgreSQL  
- **Tableau Public** – for interactive data visualization  
- **GitHub** – for project versioning and documentation  

---

## ✅ Summary

This project provides a complete and transparent pipeline for analyzing transportation-related events in BC. It supports:
- Cleaning and transforming multi-year event data
- Loading structured data into PostgreSQL
- Generating charts and visuals with Python
- Publishing interactive dashboards using Tableau

The dashboard enables quick insights for government agencies, transport analysts, and the public. It highlights where and when events occurred and their frequency in British Columbia, Canada, helping to inform policy or planning discussions.
