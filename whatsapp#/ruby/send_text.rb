require 'net/http'
require 'json'

domain = 'https://wa-XXX.4jawaly.com/'
token = 'XXXXXXX'
phone = '19292439373'
body = 'test msg from ruby'
quoted_msg_id = ''

# Check if required fields are empty
if token.nil? || token.empty?
  puts 'token: It must not be a null value'
  exit
end

if phone.nil? || phone.empty?
  puts 'phone: It must not be a null value'
  exit
end

if body.nil? || body.empty?
  puts 'body: It must not be a null value'
  exit
end

uri = URI(domain + 'api/v1/message/text')
params = {
  token: token,
  phone: phone,
  body: body,
  quotedMsgId: quoted_msg_id
}

response = Net::HTTP.post(uri, params.to_json, 'Content-Type' => 'application/json')

if response.code.to_i == 200
  result = JSON.parse(response.body)
  code = result['code']
  message = result['message']
  id = result['id']

  puts "code: #{code}"
  puts "message: #{message}"
  puts "id: #{id}"
else
  error = JSON.parse(response.body)
  code = error['code']
  message = error['message']

  puts "Error: #{code}"
  puts "message: #{message}"
end
