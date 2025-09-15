import sqlite3

## if you are not using schema.sql you can use the script below.

    # conn = sqlite3.connect('clinic_simple.db')
    # cursor = conn.cursor()

    # cursor.execute("""CREATE TABLE patients (
    #           id patient_id INTEGER PRIMARY KEY,
    #           birth_date TEXT,
    #           primary_icd10 TEXT, 
    #           last_cpt TEXT, 
    #          last_visit_dt TEXT)""");
    #    conn.close() 

## using schema.sql

from pathlib import Path

# Convert string paths to Path objects
DB_PATH = Path("./clinic_simple.db")
CSV_PATH = Path("./data/patients.csv")
SCHEMA_PATH = Path("./sql/schema.sql")

def main():
    # Read the schema SQL file
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

    # Create (or overwrite) the database and apply the schema
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)
        conn.commit()

    print(f"Created database: {DB_PATH}")

if __name__ == "__main__":
    main()