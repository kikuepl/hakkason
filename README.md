
# Hakkason Project

Google Calendar APIを使用して、ユーザーのGoogleカレンダーから予定を表示するStreamlitアプリです。

## 前提条件

- Python 3.6 以上がインストールされていること
- Google Cloud Platform アカウントがあり、Google Calendar APIが有効になっていること
- OAuth 2.0 クライアントIDが作成され、認証情報ファイル(`secret.json`)がプロジェクトディレクトリに配置されていること

## インストール方法

以下の手順に従って、このアプリケーションをローカルマシンにインストールしてください。

1. リポジトリをクローンする:

```bash
git clone https://github.com/kikuepl/hakkason
```

2. プロジェクトディレクトリに移動する:

```bash
cd hakkason
```

3. 必要なPythonライブラリをインストールする:

```bash
pip install -r requirements.txt
```

## 実行方法

以下のコマンドを実行して、Streamlitアプリを起動します。

```bash
streamlit run main.py
```

ブラウザが自動的に開き、アプリケーションが表示されます。初回起動時には、Googleアカウントでのログインと、アプリケーションへのカレンダーへのアクセス許可が求められます。
