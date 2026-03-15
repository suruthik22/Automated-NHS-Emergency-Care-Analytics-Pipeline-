# PROJECT OVERVIEW
This project is an end to end automated data analytics pipeline to analyse A&E attendences and emergency admissions data of NHS UK.

The project involves automatic monthly extraction of publicly available NHS yearly and monthly datasets by scraping, processing the data using python, uploading them into SQL lite database in a star schema, loads it into a dynamic interactive Power BI dashboard for analysis of performance metrics.

The dashboard helps in analysis of historical trends in A&E performance, patient load, performance metrics/KPIs measuring service level of NHS regions and organisations alike and helps in understanding the current pressure and identifying organisations with scope for improvement.

## OBJECTIVES

1. Build an automated ETL pipeline for healthcare data analysis.
2. Design a star schema data model suitable for analytics.
3. Perform trend analysis of A&E attendances.
4. Track Month-over-Month (MoM) and Year-over-Year (YoY) performance.
5. Visualise hospital demand and performance metrics using Power BI.
6. Identify performance levels of NHS regions and organisations

## Tech Stack
#### VS Code:
Coding
#### Python:
Web scraping, Data ingestion and ETL pipeline
#### Pandas:
Data transformation and cleaning
#### SQLite
Data warehouse storage
#### SQL 
Star schema modelling and querying
#### Power BI
Interactive dashboard and data visualisation connected to SQL Database

## Data Source

Public NHS datasets from NHS England covering monthly Accident & Emergency attendance statistics : https://www.england.nhs.uk/

## Data Pipeline Architecture

1. Data Extraction - Monthly NHS datasets are scraped from website automatically and combined using Python
2. Data Processing - Data is cleaned and standardised using Python and Pandas.
3. Database Loading - Processed data is loaded into a SQLite database
4. Data Modelling - Star schema is implemented with dimension tables (dim_date; dim_organisation) and fact tables (fact_nhs_booked_attendence; fact_nhs_unbooked_attendence) to enable time series and   organisational performance based analysis
5. Visualization - Power BI connects directly to the SQLite database to create an analytics dashboard.

## Key Metrics

Total A&E Attendances ; Month-over-Month (MoM) Change; Year-over-Year (YoY) Change; 4-hour waiting time breaches; Emergency admissions

## Dashboard Features

KPI cards for cumulative upto date and latest month attendance metrics; Attendance trend analysis; Organisation performance drill-down; Hospital pressure comparison

## Automation

The pipeline is designed to for scheduled run monthly, with data updated automatically when new datasets are released. The analytics dashboard also gets updated automatically on refresh.

## Project Structure

nhs/
│
├── data/
│   ├── raw
│   ├── processed
│   └── database
│
├── src/
│   ├── create_database.py
│   ├── init_db.py
│   ├── extract_data.py
│   ├── process_data.py
│   ├── load_to_sqlite.py
│   └── pipeline.py
│
├── sql/
│   └── create_tables.sql
│
├── dashboard/
│   └── nhs_portfolio.pbix
│ 
├── Images/
│   ├── Dashboard screenshot_1.png
│   └── Dashboard preview_2.png
│
├── run_pipeline.bat
├── README.md
└── requirements.txt

## Insights





## Future Improvements

1. Integrate with other data like staff data, ambulance performance, demographic indicators of NHS regions to assess actual pressure, identify reasons for service target breach and suggest improvement measures
2. Analyse department level performance and seasonality of pressures
3. Add advanced analytics and forecasting to compare with actuals considering effects of seasonality

   
## Dashboard Preview
![Dashboard](https://github.com/suruthik22/Automated-NHS-Emergency-Care-Analytics-Pipeline-/blob/main/Images/Dashboard%20screenshot_1.png)
![Dashboard](https://github.com/suruthik22/Automated-NHS-Emergency-Care-Analytics-Pipeline-/blob/main/Images/Dashboard%20preview_2.png)

