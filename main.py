import streamlit as st
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from google.auth.transport.requests import Request

# Streamlitアプリの設定
st.title('Google Calendar Events')

# 認証情報とスコープの設定
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
creds = None

# token.jsonが存在すれば、既存のトークンを使用
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

# トークンがない場合は、ユーザー認証フローを実行
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'secret.json', SCOPES)  # ここにダウンロードした認証情報ファイルのパスを指定
        creds = flow.run_local_server(port=0)
    # 新しいトークンを保存
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

try:
    # Google Calendar APIの呼び出し
    service = build('calendar', 'v3', credentials=creds)

    # APIを使用してカレンダーイベントを取得
    events_result = service.events().list(calendarId='primary', maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        st.write('近日中のイベントはありません。')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        st.write(start, event['summary'])

except HttpError as error:
    st.write('Google Calendar APIの呼び出し中にエラーが発生しました: %s' % error)
