import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text

DB_PATH = Path("clinic_simple.db")
CSV_PATH = Path("data/patients.csv")

def main():
    # Loading CSV file into DataFrame
    pat_df = pd.read_csv(CSV_PATH, dtype=str)

    # Creating SQL database engine
    engine = create_engine(f"sqlite:///{DB_PATH}")

    # Writing DataFrame to 'patients' table
    # Need to change "append" to "replace" for testing purposes
    pat_df.to_sql('patients', con=engine, if_exists="replace", index=False)

    # Checking number of rows loaded
    sql_count = text("SELECT COUNT(*) FROM patients")
    with engine.connect() as conn:
        result = conn.execute(sql_count)
        total = result.scalar()

    print(f"Loaded {len(pat_df)} rows into patients. Table now has {total} rows")

if __name__ == "__main__":
    main()

