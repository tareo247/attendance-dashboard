# 勤怠分析ダッシュボード

CSVの勤怠データを分析するStreamlitアプリです。
Excelで行われがちな勤怠分析を **Python + SQLite + Streamlit** で自動化しました。

## Demo

https://attendance-dashboard-39mfvauw28dn5q8h9wcjbt.streamlit.app/

## 技術

| 技術 | 用途 |
|-----|-----|
| Python | アプリケーション |
| pandas | データ処理 |
| SQLite | データ保存 |
| Streamlit | ダッシュボード |
| Git / GitHub | バージョン管理 |

## アーキテクチャ

CSV
↓
pandas
↓
SQLite
↓
Streamlit Dashboard

## 主な機能

### CSVインポート
勤怠CSVを読み込み、SQLiteに保存します。

### 労働時間計算
出勤時間と退勤時間から労働時間を算出します。

### 残業時間分析
社員ごとの残業時間を集計します。

### ダッシュボード
Streamlitを使い残業状況をグラフで可視化します。

## 作成背景

社内SEとして業務に関わる中で
Excelによる手作業が多いことに課題を感じました。

そのため
Pythonとデータベースを用いて
勤怠データを自動分析するツールを作成しました。