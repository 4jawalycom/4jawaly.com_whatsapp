<?php
$domain = "https://wa-XXX.4jmawaly.com/";
$params = [];
$params["token"] = "XXXXXXXXXX";
$params["phone"] = "9665000000";
$params["body"] = "test msg "; // نص الرسالة
$params["quotedMsgId"] = ""; // معرف الرسالة المستشهد بها

if (empty($params["token"])) {
    echo "يجب ألا يكون الحقل (Token) فارغًا";
    exit();
}

if (empty($params["phone"])) {
    echo "يرجى تحديد رقم الهاتف";
    exit();
}

if (empty($domain) || !preg_match('/^https:\/\/wa-\d+\.4jawaly\.com\/$/', $domain)) {
    echo "يرجى تحديد النطاق الصحيح (https://wa-youserver_number.4jmawaly.com/)";
    exit();
}

if (empty($params["body"])) {
    echo "نص الرسالة فارغ";
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
