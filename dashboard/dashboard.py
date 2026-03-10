import streamlit as st
import pandas as pd
import db.database as db  # 先に database.py を準備している前提

def run():
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

    if att_file:
        st.subheader("勤怠CSVプレビュー")
        st.dataframe(pd.read_csv(att_file).head())

    if dep_file:
        st.subheader("部署CSVプレビュー")
        st.dataframe(pd.read_csv(dep_file).head())


    if att_file and dep_file:
        if st.button("データ登録"):
            try:
                df_att = pd.read_csv(att_file)
                df_dep = pd.read_csv(dep_file)
            except Exception as e:
                st.error(f"CSV読み込みエラー: {e}")

            # DB初期化（テーブル作成）
            db.init_db()

            # データ投入
            db.insert_attendance(df_att)
            db.insert_department(df_dep)

            st.success("データをDBに登録しました")
            st.experimental_rerun()  # 画面を更新して再描画

        # --------------------------
        # データ取得・表示
        # --------------------------
        rows = db.fetch_attendance_with_department()
        df_result = pd.DataFrame(
            rows, 
            columns=["employee_id", "date", "start_time", "end_time", "work_hours", "department"]
        )

        if df_result.empty:
            st.warning("データがありません")
            return

        st.subheader("結合データ")
        st.dataframe(df_result)

        st.subheader("部署別労働時間")
        summary = (
            df_result
            .groupby("department")["work_hours"]
            .sum()
            .reset_index()
        )

        st.dataframe(summary)
        st.bar_chart(summary.set_index("department"))

        st.subheader("長時間労働アラート")
        alert = df_result[df_result["work_hours"] > 10]
        if alert.empty:
            st.success("長時間労働は検出されませんでした")
        else:
            st.warning("長時間労働の可能性があります")
            st.dataframe(alert)