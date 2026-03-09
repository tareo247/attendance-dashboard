import csv
import random
from datetime import datetime, timedelta

# ----------------------
# 設定
# ----------------------
EMPLOYEE_COUNT = 20
DAYS = 30

departments = [
    "営業",
    "開発",
    "総務",
    "人事",
    "経理"
]

# ----------------------
# 部署CSV
# ----------------------
with open("department.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["employee_id", "department"])

    for emp_id in range(1, EMPLOYEE_COUNT + 1):
        dept = departments[(emp_id - 1) % len(departments)]
        writer.writerow([emp_id, dept])

# ----------------------
# 勤怠CSV
# ----------------------
start_date = datetime(2026, 3, 1)

with open("attendance.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "employee_id",
        "date",
        "start_time",
        "end_time",
        "work_hours"
    ])

    for day in range(DAYS):
        date = start_date + timedelta(days=day)

        for emp_id in range(1, EMPLOYEE_COUNT + 1):

            start_hour = random.choice([8, 9, 9, 9, 10])
            start_min = random.choice([0, 15, 30, 45])

            work_hours = random.choice([
                7.5, 8, 8, 8, 8.5, 9, 9.5
            ])

            end_hour = start_hour + int(work_hours)
            end_min = start_min

            writer.writerow([
                emp_id,
                date.strftime("%Y-%m-%d"),
                f"{start_hour:02}:{start_min:02}",
                f"{end_hour:02}:{end_min:02}",
                work_hours
            ])

print("CSV生成完了")