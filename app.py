import streamlit as st
import pandas as pd
import database as db  # 先に database.py を準備している前提

st.title("勤怠分析ダッシュボード")

# --------------------------
# DBリセットボタン
# --------------------------
if st.button("DBをリセット"):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM attendance")
    cursor.execute("DELETE FROM department")
    conn.commit()
    conn.close()
    # SQLiteファイルサイズを縮小（任意）
    conn = db.get_connection()
    conn.execute("VACUUM")
    conn.close()
    st.success("DBのデータを全て削除しました")

st.markdown("---")

# --------------------------
# CSVアップロード
# --------------------------
att_file = st.file_uploader("勤怠CSVアップロード", type="csv")
dep_file = st.file_uploader("部署CSVアップロード", type="csv")

if att_file and dep_file:
    df_att = pd.read_csv(att_file)
    df_dep = pd.read_csv(dep_file)

    # DB初期化（テーブル作成）
    db.init_db()

    # データ投入
    db.insert_attendance(df_att)
    db.insert_department(df_dep)

    st.success("データをDBに登録しました")

    # --------------------------
    # データ取得・表示
    # --------------------------
    rows = db.fetch_attendance_with_department()
    df_result = pd.DataFrame(
        rows, 
        columns=["employee_id", "date", "start_time", "end_time", "work_hours", "department"]
    )

    st.subheader("結合データ")
    st.dataframe(df_result)

    st.subheader("部署別労働時間")
    summary = df_result.groupby("department")["work_hours"].sum()
    st.bar_chart(summary)