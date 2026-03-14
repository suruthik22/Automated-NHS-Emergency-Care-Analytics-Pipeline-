import pandas as pd
import sqlite3 
import os

db_path = r"data\database\nhs_ae.db"

file_path=r"data\processed\combined_data.csv"

if not os.path.exists(file_path):
    print("No processed data found. skipping database load")
    exit()

conn=sqlite3.connect(db_path)

df=pd.read_csv(file_path)

df.to_sql("ae_attendence_staging",
          conn,
          if_exists="replace",
          index=False)

print("Data loaded into staging table")

##---BUILDING STAR SCHEMA---

#Transforming into dimension tables

cursor=conn.cursor()

cursor.execute("""
    INSERT OR IGNORE INTO dim_organisation(org_code,parent_org,org_name)
    SELECT DISTINCT TRIM(org_code),TRIM(parent_org),TRIM(org_name)
    FROM ae_attendence_staging
    WHERE UPPER(org_code) NOT LIKE '%TOTAL%' AND
    UPPER(parent_org) NOT LIKE '%TOTAL%' AND
    UPPER(org_name) NOT LIKE '%TOTAL%'
               """)

cursor.execute("""
               INSERT OR IGNORE INTO dim_date (period,month,year)
               SELECT DISTINCT TRIM(period),TRIM(month),TRIM(year)
               FROM ae_attendence_staging
               WHERE UPPER(period) NOT LIKE '%TOTAL%' AND
               UPPER(month) NOT LIKE '%TOTAL%' AND
                year NOT LIKE '%TOTAL%'
               """)

cursor.execute("""
               INSERT OR IGNORE INTO fact_nhs_booked_attendance(
                        date_id,org_id,
                        ae_attendances_booked_appointments_type_1,
                        ae_attendances_booked_appointments_type_2,
                        ae_attendances_booked_appointments_other_department,
                        attendances_over_4hrs_booked_appointments_type_1,
                        attendances_over_4hrs_booked_appointments_type_2,
                        attendances_over_4hrs_booked_appointments_other_department
                        )
               
               SELECT d.date_id, o.org_id,
                        s.ae_attendances_booked_appointments_type_1,
                        s.ae_attendances_booked_appointments_type_2,
                        s.ae_attendances_booked_appointments_other_department,
                        s.attendances_over_4hrs_booked_appointments_type_1,
                        s.attendances_over_4hrs_booked_appointments_type_2,
                        s.attendances_over_4hrs_booked_appointments_other_department 

                FROM ae_attendence_staging AS s
               
                JOIN dim_date AS d
                ON d.period=s.period

               JOIN dim_organisation AS o
               ON o.org_code=s.org_code
               """)
#Transforming into fact tables

cursor.execute("""
               INSERT OR IGNORE INTO fact_nhs_unbooked_attendance(
                        date_id,org_id,
                        ae_attendances_type_1,
                        ae_attendances_type_2,
                        ae_attendances_other_ae_department,

                        attendances_over_4hrs_type_1,
                        attendances_over_4hrs_type_2,
                        attendances_over_4hrs_other_department,

                        patients_who_have_waited_412_hs_from_dta_to_admission,
                        patients_who_have_waited_12_hrs_from_dta_to_admission,

                        emergency_admissions_via_ae__type_1,
                        emergency_admissions_via_ae__type_2,
                        emergency_admissions_via_ae__other_ae_department,
                        other_emergency_admissions
                        )
               
               SELECT d.date_id, o.org_id,
                        s.ae_attendances_type_1,
                        s.ae_attendances_type_2,
                        s.ae_attendances_other_ae_department,

                        s.attendances_over_4hrs_type_1,
                        s.attendances_over_4hrs_type_2,
                        s.attendances_over_4hrs_other_department,

                        s.patients_who_have_waited_412_hs_from_dta_to_admission,
                        s.patients_who_have_waited_12_hrs_from_dta_to_admission,

                        s.emergency_admissions_via_ae__type_1,
                        s.emergency_admissions_via_ae__type_2,
                        s.emergency_admissions_via_ae__other_ae_department,
                        s.other_emergency_admissions 

                FROM ae_attendence_staging AS s
               
                JOIN dim_date AS d
                ON d.period=s.period

               JOIN dim_organisation AS o
               ON o.org_code=s.org_code
               """)
conn.commit()

print("Star Schema tables populated")

conn.close()
