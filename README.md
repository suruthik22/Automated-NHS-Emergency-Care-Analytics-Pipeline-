# PROJECT OVERVIEW
This project is an end to end automated data analytics pipeline to analyse A&E attendences and emergency admissions data of NHS UK.

The project involves automatic monthly extraction of publicly available NHS yearly and monthly datasets by scraping, processing the data using python, uploading them into SQL lite database in a star schema, loads it into a dynamic interactive Power BI dashboard for analysis of performance metrics.

The dashboard helps in analysis of historical trends in A&E performance, patient load, performance metrics/KPIs measuring service level of NHS regions and organisations alike and helps in understanding the current pressure and identifying organisations with scope for improvement.

## OBJECTIVES

1. Build an automated ETL pipeline for healthcare data analysis
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

## Insights and recommendations
1. High proportion of patients breaching the 4-hour target :
About 25.83% of A&E attendances exceeded the 4-hour wait target (vs NHS standard of 95% within 4 hours), showing system pressure despite slight improvement from 2024 to 2025.
Recommendation: Improve patient flow and implement real-time operational dashboards for capacity monitoring, planning or staff reorganisation.

2. Seasonal demand drives waiting time:
Waiting times increase between August and January, indicating higher pressure linked to seasonal illnesses in winter and higher emergency demand.
Recommendation: Use predictive demand forecasting and increase winter staffing, bed capacity and community support.

3. Type 1 emergency departments drive most delays:
Type 1 departments handle 61% of attendances but account for 95% of >4-hour waits, highlighting congestion in major emergency departments.
Recommendation: Can consider diversion to urgent treatment centres (Type 3) and expand capacity in high-pressure departments

4. Long admission delays (>12 hours) are increasing:
Around 2% of patients face >12-hour delays from decision to admit to admission, indicating downstream hospital bed and capacity constraints.
Recommendation: Improve discharge planning, bed management and hospital flow systems to reduce admission bottlenecks.

5. Performance varies significantly across regions and organisations:
Some low volume regions show higher waiting percentages, while certain high volume organisations maintain better performance, suggesting operational efficiency differences.
Recommendation: Benchmark high-performing trusts, analyse staffing and resource allocation and implement targeted performance improvement strategies.

## Business value of this project
1. Operational performance monitoring: The dashboard enables continuous tracking of A&E demand, waiting time performance and regional variations to support operational decision-making.
2. Demand and capacity planning: Identifying seasonal patterns and long admission delays helps healthcare managers plan staffing, bed capacity and winter demand strategies more effectively
3. Benchmarking and performance improvement: Organisation-level comparisons highlight high-performing trusts and underperforming systems, enabling the adoption of best practices across the NHS network.
4. This analysis demonstrates how healthcare operational data can be transformed into actionable insights for improving patient flow and reducing waiting times
5. Scalable analytics framework supporting large-scale healthcare performance analytics across multiple organisations and regions.

## Future Improvements

1. Integrate with other data like staff data, ambulance performance, demographic indicators of NHS regions to assess actual pressure, identify reasons for service target breach and suggest improvement measures
2. Analyse department level performance and seasonality of pressures
3. Add advanced analytics and forecasting to compare with actuals considering effects of seasonality

   
## Dashboard Preview
![Dashboard](https://github.com/suruthik22/Automated-NHS-Emergency-Care-Analytics-Pipeline-/blob/main/Images/Dashboard%20screenshot_1.png)
![Dashboard](https://github.com/suruthik22/Automated-NHS-Emergency-Care-Analytics-Pipeline-/blob/main/Images/Dashboard%20preview_2.png)

