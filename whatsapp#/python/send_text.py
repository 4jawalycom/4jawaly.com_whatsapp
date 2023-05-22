# -*- coding: utf-8 -*-

import requests

domain = "https://wa-XXX.4jawaly.com/"
params = {
    "token": "XXXXXXXXX",
    "phone": "19292439373",
    "body": "test msg from python",
    "quotedMsgId": ""
}

if not params["token"]:
    print("token: It must not be a null value")
    exit()

if not params["phone"]:
    print("phone: It must not be a null value")
    exit()

if not params["body"]:
    print("body: It must not be a null value")
    exit()

url = domain + 'api/v1/message/text'
headers = {'Accept': 'application/json'}

response = requests.post(url, json=params, headers=headers)
http_code = response.status_code

if http_code == 200:
    result = response.json()
    code = result["code"]
    message = "تم الارسال بنجاح"
    id = result["id"]

    print("code:", code)
    print("message:", message)
    print("id:", id)
else:
    error = response.json()
    code = error["code"]
    message = error["message"]

    print("code:", code)
    print("message:", message)
