import requests

# REST APIのエンドポイントURLを指定
url = "http://localhost:15520/api/input"


def call_yukarinet_connector(message):
    # 必要なヘッダーを指定
    headers = {
    }

    # パラメータを指定（必要に応じて）
    params = {
        "text": message
    }

    # GETリクエストを送信してレスポンスを取得
    response = requests.get(url, headers=headers, params=params)

    if (response.status_code != 200):
        print("Yukarinet-Connector API is failed.", response)

    return
