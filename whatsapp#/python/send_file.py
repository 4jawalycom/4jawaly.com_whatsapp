import requests

domain = "https://wa-XXXX.4jawaly.com/"#log in user.4jawaly.com -> whatsapp -> ارسال رسالة -> API Docs
params = {
    "token": "XXXXXX", #log in user.4jawaly.com -> whatsapp -> ارسال رسالة -> API Docs
    "phone": "19292439373", 
    "body": "https://cdn-dev.4jawaly.com/spam-regulation.pdf", #PDF ,xlsx  url
    "quotedMsgId": "", #Quoted message ID from the message list. Example: false_17472822486@c.us_DF38E6A25B42CC8CCE57EC40F. " تستخدم للرد على رسالة محددة مرسلة سابقا
    "filename": "filename.pdf" #.pdf ,.xlsx
}

# Check if required fields are empty
if not params["token"]:
    print("token: It must not be a null value")
    exit()

if not params["phone"]:
    print("phone: It must not be a null value")
    exit()

if not params["body"]:
    print("body: It must not be a null value")
    exit()

url = domain + "api/v1/message/file"

response = requests.post(url, json=params, headers={"Accept": "application/json"})
http_code = response.status_code

if http_code == 200:
    result = response.json()
    code = result["code"]
    message = "تم الارسال بنجاح"
    id = result["id"]

    print(f"code: {code}")
    print(f"message: {message}")
    print(f"id: {id}")
else:
    error = response.json()
    code = error["code"]
    message = error["message"]

    print(f"code: {code}")
    print(f"message: {message}")
