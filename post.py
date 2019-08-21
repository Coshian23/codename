# !/usr/bin/env python
# coding: utf-8
import json
from requests_oauthlib import OAuth1Session
import codename

def lambda_handler(event, context):

    # boardgamenumber twitter account
    CK = "arLDadWJYgNEWKC2fSbOZkN0m"  # Consumer Key
    CS = "tR4X1sVfh1FEcka1AC2KNi1zc1OVX5IWVhpOkuG4VuzWlEGsg2"  # Consumer Secret
    AT = "890841149719552000-Qu94hUrO2vHVKEKV4ZnmT0K2NTIkw33"  # Access Token
    AS = "BzNrsmMLCXLmZ9JPDee6P4oGCHYhVgTzdznPKIxWBc9cK"  # Accesss Token Secert

    url_media = "https://upload.twitter.com/1.1/media/upload.json"
    url_text = "https://api.twitter.com/1.1/statuses/update.json"

    # コードネーム画像作成
    codename

    # OAuth認証 セッションを開始
    twitter = OAuth1Session(CK, CS, AT, AS)

    # 画像投稿
    files = {"media": open(codename.fname, 'rb')}
    req_media = twitter.post(url_media, files=files)

    # レスポンスを確認
    if req_media.status_code != 200:
        print("画像アップデート失敗: %s", req_media.text)
        exit()

    # Media ID を取得
    media_id = json.loads(req_media.text)['media_id']
    print("Media ID: %d" % media_id)

    # Media ID を付加してテキストを投稿
    text = codename.date.strftime("%Y/%m/%d") + "のお題\n#コードネーム\n#ボードゲーム"
    params = {'status': text, "media_ids": [media_id]}
    print(text)
    req_media = twitter.post(url_text, params=params)

    # 再びレスポンスを確認
    if req_media.status_code != 200:
        print("テキストアップデート失敗: %s", req_text.text)
        exit()

    print("OK")

lambda_handler("","")