<?php
$domain = "https://wa-XXX.4jawaly.com/";
$params = [];
$params["token"] = "XXXXXXXX";
$params["phone"] = "19292439373";
$params["body"] = "test msg from example"; // نص الرسالة
$params["quotedMsgId"] = ""; // معرف الرسالة المستشهد بها

if (empty($params["token"])) {
    echo "token: It must not be a null value";
    exit();
}

if (empty($params["phone"])) {
    echo "phone: It must not be a null value";
    exit();
}

if (empty($params["body"])) {
    echo "body: It must not be a null value";
    exit();
}

$curl = curl_init();

curl_setopt_array($curl, array(
    CURLOPT_URL => $domain.'api/v1/message/text',
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => '',
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 0,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => 'POST',
    CURLOPT_POSTFIELDS => $params,
    CURLOPT_HTTPHEADER => array(
        'Accept: application/json'
    ),
));

$response = curl_exec($curl);
$httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
curl_close($curl);

if ($httpCode == 200) {
    $result = json_decode($response, true);
    $code = $result["code"];
    $message = "تم الارسال بنجاح";
    $id = $result["id"];

    echo "code: $code\n";
    echo "message: $message\n";
    echo "id: $id\n";
} else {
    $error = json_decode($response, true);
    $code = $error["code"];
    $message = $error["message"];

    echo "code: $code\n";
    echo "message: $message\n";
}

?>