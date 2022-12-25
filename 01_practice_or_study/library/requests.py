"""requests ライブラリの練習モジュール(外部API空の取得)"""
import requests


# 天気予報API(今回の外部API対象Webサイト)
url = 'https://weather.tsukumijima.net/api/forecast/?city=110010'

# GETメソッドでGET
response = requests.get(url)

# 値の確認

print(f"レスポンスオブジェクト:{response}")

print(f"レスポンスのステータスコード:{response.status_code}")

print(f"レスポンスボディ:{response.json()}")

print(f"レスポンスのヘッダー情報:{response.headers}")

print(f"レスポンスの値の取り出し方:{response.json()['title']}")
