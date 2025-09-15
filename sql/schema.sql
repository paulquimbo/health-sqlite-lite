DROP TABLE IF EXISTS patients;

-- need to replace date to text since sqlite does not have a date type

CREATE TABLE patients (
    patient_id TEXT PRIMARY KEY,        -- e.g. P00001
    birth_date TEXT NOT NULL,           -- ISO: YYYY-MM-DD
    primary_icd10 TEXT NOT NULL,        -- e.g. E11.9
    last_cpt TEXT NOT NULL,             -- e.g. 99213
    last_visit_dt TEXT NOT NULL         -- ISO date
);