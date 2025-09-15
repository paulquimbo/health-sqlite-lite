import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text

DB_PATH = Path("clinic_simple.db")
CSV_PATH = Path("data/patients.csv")

def main():
    # Load CSV into DataFrame
    pat_df = pd.read_csv(CSV_PATH, dtype=str)

    # Create SQL database engine
    engine = create_engine(f"sqlite:///{DB_PATH}")

    # Check for existing patient IDs to avoid duplicates
    with engine.connect() as conn:
        try:
            existing_ids = pd.read_sql("SELECT patient_id FROM patients", conn)
            pat_df = pat_df[~pat_df['patient_id'].isin(existing_ids['patient_id'])]
        except Exception:
            # Table doesn't exist yet — safe to insert all rows
            pass

    # Append only new rows to 'patients' table
    pat_df.to_sql('patients', con=engine, if_exists="append", index=False)

    # Count total rows in the table
    sql_count = text("SELECT COUNT(*) FROM patients")
    with engine.connect() as conn:
        result = conn.execute(sql_count)
        total = result.scalar()

    print(f"Inserted {len(pat_df)} new rows into patients. Table now has {total} rows.")

if __name__ == "__main__":
    main()
