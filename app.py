import streamlit as st
import pandas as pd

st.title("勤怠分析ダッシュボード")

uploaded_file = st.file_uploader("CSVアップロード")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("データ")

    st.dataframe(df)

    st.subheader("部署別労働時間")

    result = df.groupby("department")["work_hours"].sum()

    st.bar_chart(result)