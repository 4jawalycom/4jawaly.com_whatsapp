import requests

domain = "https://wa-XXX.4jawaly.com/"
params = {
    "token": "XXXXXXXX",
    "phone": "19292439373",
    "body": "https://i0.wp.com/www.4jawaly.com/wp-content/uploads/2019/05/itservice2_pic2.png",
    "quotedMsgId": "",
    "caption": "الرسالة اسفل الصورة",
    "filename": "photo_name.png"
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
