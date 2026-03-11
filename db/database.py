import sqlite3
from pathlib import Path
import os

if os.getenv("STREAMLIT_RUNTIME"):
    DB_FILE = Path("/tmp/attendance.db")
else:
    BASE_DIR = Path(__file__).resolve().parent
    DB_FILE = BASE_DIR / "attendance.db"

def get_connection():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)  # /tmp/ がなければ作成
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            employee_id INTEGER,
            date TEXT,
            start_time TEXT,
            end_time TEXT,
            work_hours REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS department (
            employee_id INTEGER,
            department TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_attendance(df):
    conn = get_connection()
    cursor = conn.cursor()
    data = [(int(r.employee_id), r.date, r.start_time, r.end_time, float(r.work_hours)) for _, r in df.iterrows()]
    cursor.executemany("INSERT INTO attendance VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

def insert_department(df):
    conn = get_connection()
    cursor = conn.cursor()
    data = [(int(r.employee_id), r.department) for _, r in df.iterrows()]
    cursor.executemany("INSERT INTO department VALUES (?, ?)", data)
    conn.commit()
    conn.close()

def fetch_attendance_with_department():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.employee_id, a.date, a.start_time, a.end_time, a.work_hours, d.department
        FROM attendance a
        LEFT JOIN department d ON a.employee_id = d.employee_id
        ORDER BY a.employee_id, a.date
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows