DROP TABLE IF EXISTS patients;

-- need to replace DATE to TEXT since sqlite does not have a DATE type

CREATE TABLE patients (
    patient_id TEXT PRIMARY KEY,        -- e.g. P00001
    birth_date TEXT NOT NULL,           -- ISO: YYYY-MM-DD
    primary_icd10 TEXT NOT NULL,        -- e.g. E11.9
    last_cpt TEXT NOT NULL,             -- e.g. 99213
    last_visit_dt TEXT NOT NULL         -- ISO date
);