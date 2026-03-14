CREATE TABLE IF NOT EXISTS dim_date(
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    period TEXT,
    month TEXT,
    year INTEGER,

    UNIQUE(period, month, year)
);

CREATE TABLE IF NOT EXISTS dim_organisation(
    org_id INTEGER PRIMARY KEY AUTOINCREMENT,
    org_code TEXT,
    parent_org TEXT,
    org_name TEXT,
    
    UNIQUE(org_code, parent_org, org_name)
);

CREATE TABLE IF NOT EXISTS fact_nhs_unbooked_attendance(
    fact_id_unbooked INTEGER PRIMARY KEY AUTOINCREMENT,
    
    date_id INTEGER,
    org_id INTEGER,

    ae_attendances_type_1 INTEGER,
    ae_attendances_type_2 INTEGER,
    ae_attendances_other_ae_department INTEGER,

    attendances_over_4hrs_type_1 INTEGER,
    attendances_over_4hrs_type_2 INTEGER,
    attendances_over_4hrs_other_department INTEGER,

    patients_who_have_waited_412_hs_from_dta_to_admission INTEGER,
    patients_who_have_waited_12_hrs_from_dta_to_admission INTEGER,

    emergency_admissions_via_ae__type_1 INTEGER,
    emergency_admissions_via_ae__type_2 INTEGER,
    emergency_admissions_via_ae__other_ae_department INTEGER,
    other_emergency_admissions INTEGER,

    UNIQUE(date_id,org_id)
);

CREATE TABLE IF NOT EXISTS fact_nhs_booked_attendance(
    fact_id_booked INTEGER PRIMARY KEY AUTOINCREMENT,
    
    date_id INTEGER,
    org_id INTEGER,

    ae_attendances_booked_appointments_type_1 INTEGER,
    ae_attendances_booked_appointments_type_2 INTEGER,
    ae_attendances_booked_appointments_other_department INTEGER,

    attendances_over_4hrs_booked_appointments_type_1 INTEGER,
    attendances_over_4hrs_booked_appointments_type_2 INTEGER,
    attendances_over_4hrs_booked_appointments_other_department INTEGER,

    UNIQUE(date_id,org_id)
);