import sqlite3
from pathlib import Path

DB_PATH = Path("./clinic_simple.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Define SQL queries
SQLQquery1 = "SELECT COUNT(*) AS n_patients FROM patients;"
SQLQquery2 = "SELECT primary_icd10, COUNT(*) AS n FROM patients GROUP BY primary_icd10 ORDER BY n DESC;"
SQLQquery3 = "SELECT patient_id, last_cpt, last_visit_dt FROM patients WHERE last_cpt LIKE '992%' AND last_visit_dt >= '2025-01-01' ORDER BY last_visit_dt DESC;"
SQLQquery4 = "SELECT patient_id, birth_date, last_visit_dt, CAST((julianday(date('now')) - julianday(birth_date)) / 365.25 AS INT) AS age_years FROM patients ORDER BY age_years DESC LIMIT 10;"
SQLQquery5 = "SELECT * FROM patients WHERE primary_icd10 = '' OR last_cpt = '';"


# A) Number of patients
cursor.execute(SQLQquery1)
result = cursor.fetchone()
print(f"A) Number of patients:\n{result[0]}")

# B) Top primary diagnoses by count
cursor.execute(SQLQquery2)
rows = cursor.fetchall()
formatted = "\n".join(f"{row[0].ljust(8)}{row[1]}" for row in rows)
print(f"B) Top primary diagnoses by count:\n{formatted}")

# C) Office-visit CPTs since Jan 1, 2025
cursor.execute(SQLQquery3)
rows = cursor.fetchall()
formatted = "\n".join(f"{str(row[0]).ljust(12)}{row[1].ljust(8)}{row[2]}" for row in rows)
print(f"C) Office-visit CPTs since Jan 1, 2025:\n{formatted}")

# D) Age at last visit for 10 oldest patients
cursor.execute(SQLQquery4)
rows = cursor.fetchall()
formatted_rows = "\n".join(
    f"{str(row[0]).ljust(12)}{row[1].ljust(12)}{row[2].ljust(12)}{row[3]}"
    for row in rows
)
print(f"D) Age at last visit for 10 oldest patients:\n{formatted_rows}")

# E) Quick data quality check — any blank codes?
cursor.execute(SQLQquery5)
rows = cursor.fetchall()
formatted_rows = "\n".join(str(row) for row in rows)
print(f"E) Data quality check — blank codes:\n{formatted_rows}")

# Close connection
conn.close()