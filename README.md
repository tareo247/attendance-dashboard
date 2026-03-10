# 勤怠分析ダッシュボード

勤怠CSVを自動集計し、残業時間を可視化するダッシュボードアプリです。<br>
Excelで行われがちな勤怠分析を **Python + SQLite + Streamlit** で自動化しました。

## Demo

https://attendance-dashboard-39mfvauw28dn5q8h9wcjbt.streamlit.app/

※ サンプルCSVをアップロードすると残業時間のダッシュボードが表示されます

## 技術

| 技術 | 用途 |
|-----|-----|
| Python | アプリケーション |
| pandas | データ処理 |
| SQLite | データ保存 |
| Streamlit | ダッシュボード |
| Git / GitHub | バージョン管理 |

## アーキテクチャ
```
CSV
│
▼
pandas
│
▼
SQLite
│
▼
Streamlit Dashboard
```
## 主な機能

### CSVインポート
勤怠CSVを読み込み、SQLiteに保存します。

### 労働時間計算
出勤時間と退勤時間から労働時間を算出します。

### 残業時間分析
社員ごとの残業時間を集計します。

### ダッシュボード
Streamlitを使い残業状況をグラフで可視化します。

## 改善効果

Excelで行っていた勤怠集計を自動化し、

- CSV取込
- 労働時間計算
- 残業時間分析

をPythonで実装しました。

## 作成背景
社内SEとして業務に関わる中で<br>
Excelによる手作業が多いことに課題を感じました。<br>
<br>
そのため<br>
Pythonとデータベースを用いて<br>
勤怠データを自動分析するツールを作成しました。<br>