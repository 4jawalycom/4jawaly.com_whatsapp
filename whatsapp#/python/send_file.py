import requests

domain = "https://wa-XXX.4jawaly.com/"
params = {
    "token": "XXXXXXXXX",
    "phone": "19292439373",
    "body": "https://cdn-dev.4jawaly.com/spam-regulation.pdf",
    "quotedMsgId": "",
    "filename": "filename.pdf"
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

url = f"{domain}api/v1/message/file"
headers = {"Accept": "application/json"}

response = requests.post(url, headers=headers, data=params)
result = response.json()

code = result["code"]
message = "تم الارسال بنجاح" if response.status_code == 200 else result["message"]
id = result["id"]

print(f"code: {code}")
print(f"message: {message}")
print(f"id: {id}")
