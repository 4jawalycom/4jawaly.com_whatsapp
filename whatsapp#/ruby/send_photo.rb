require 'net/http'
require 'json'

domain = "https://wa-XXX.4jawaly.com/"
params = {
  "token" => "XXXXXXXX",
  "phone" => "19292439373",
  "body" => "https://i0.wp.com/www.4jawaly.com/wp-content/uploads/2019/05/itservice2_pic2.png",
  "quotedMsgId" => "",
  "caption" => "الرسالة اسفل الصورة",
  "filename" => "photo_name.png"
}

if params["token"].empty?
  puts "token: It must not be a null value"
  exit
end

if params["phone"].empty?
  puts "phone: It must not be a null value"
  exit
end

if params["body"].empty?
  puts "body: It must not be a null value"
  exit
end

url = "#{domain}api/v1/message/file"
headers = { "Accept" => "application/json" }

uri = URI(url)
http = Net::HTTP.new(uri.host, uri.port)
request = Net::HTTP::Post.new(uri.path, headers)
request.set_form_data(params)

response = http.request(request)
result = JSON.parse(response.body)

code = result["code"]
message = response.code == "200" ? "تم الارسال بنجاح" : result["message"]
id = result["id"]

puts "code: #{code}"
puts "message: #{message}"
puts "id: #{id}"
