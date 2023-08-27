from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# ダウンロードしたjsonファイルをドライブにアップデートした際のパス
json = './apartment-analysis-397211-65c94c00b8e1.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)

gc = gspread.authorize(credentials)

# 書き込み先のスプレッドシートキーを追加
SPREADSHEET_KEY = '1OXCoX4FPhlAt79alQ1vl4LMF4dHN0IgwuFBhZbxMNBA'

# 共有設定したスプレッドシートの1枚目のシートを開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1


# 取得したデータをスプレッドシートに記入する関数
def write_to_spreadsheet(data):
    worksheet.append_rows(data)  # 一度にすべての行を追加
