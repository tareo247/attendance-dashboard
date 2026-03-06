import streamlit as st
import pandas as pd
import database as db

st.title("勤怠分析ダッシュボード")

att_file = st.file_uploader("勤怠CSVアップロード", type="csv")
dep_file = st.file_uploader("部署CSVアップロード", type="csv")

if att_file and dep_file:
    df_att = pd.read_csv(att_file)
    df_dep = pd.read_csv(dep_file)

    db.init_db()
    db.insert_attendance(df_att)
    db.insert_department(df_dep)

    rows = db.fetch_attendance_with_department()
    df_result = pd.DataFrame(rows, columns=["employee_id", "date", "start_time", "end_time", "work_hours", "department"])
    st.subheader("結合データ")
    st.dataframe(df_result)

    st.subheader("部署別労働時間")
    summary = df_result.groupby("department")["work_hours"].sum()
    st.bar_chart(summary)