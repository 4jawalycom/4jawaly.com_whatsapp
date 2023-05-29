require 'net/http'
require 'json'

domain = "https://wa-XXX.4jawaly.com/"
params = {
  "token" => "XXXXXXXXX",
  "phone" => "19292439373",
  "body" => "https://cdn-dev.4jawaly.com/spam-regulation.pdf",
  "quotedMsgId" => "",
  "filename" => "filename.pdf"
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
if response.code == "200"
  message = "تم الارسال بنجاح"
else
  message = result["message"]
end
id = result["id"]

puts "code: #{code}"
puts "message: #{message}"
puts "id: #{id}"
