# DF_Evil_Twin
##@A_Y_TR##آلقيـــــــــــــــآدهہ‌‏ آلزعيـــم####
# DF Evil Twin Attack Tool

🚀 **DF Evil Twin** is an advanced tool for performing an **Evil Twin Attack**, creating a **fake WiFi access point** with the same SSID as the target network to trick users into connecting and stealing their login credentials.

---

## 📌 Features  
✅ **Fake Login Page** to capture WiFi passwords.  
✅ **Deauthentication Attack** to disconnect users from the real WiFi.  
✅ **SSL Strip & Session Hijacking** to intercept encrypted sessions.  
✅ **Auto-send credentials to Telegram Bot.**  
✅ **Easy to use – fully automated execution.**  

---
Here’s the corrected and English-translated version of the setup and execution instructions for DF Evil Twin:


---

🔧 All Commands to Run DF Evil Twin

📌 1️⃣ Install Required Tools
```
sudo apt update && sudo apt upgrade -y
sudo apt install aircrack-ng hostapd dnsmasq apache2 php unzip git -y
```

---

📌 2️⃣ Clone the Tool from GitHub
```
git clone https://github.com/MohamedAbuAl-Saud/DF_Evil_Twin
cd DF_Evil_Twin
```

---

📌 3️⃣ Grant Execution Permissions to Important Files
```
sudo chmod +x install.sh
./install.sh
```

---

📌 4️⃣ Enable Monitor Mode for WiFi Adapter
```
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```
(Replace wlan0 with the correct adapter name if different.)

Verify if monitor mode is enabled:
```
iwconfig
```
If successful, you should see wlan0mon instead of wlan0.


---

📌 5️⃣ Run the Tool
```
sudo python3 df_evil_twin.py
```

---

📌 6️⃣ Enter the Required Information at Startup

1️⃣ Telegram Bot Token (for sending captured credentials).
2️⃣ Telegram Chat ID (for receiving credentials).
3️⃣ Target SSID (the network name to attack).
4️⃣ Target BSSID (MAC address of the target network).
5️⃣ Your Username (to log the attack session).


---

🔥 Attack Execution Process

Once the inputs are provided, the tool will:
1️⃣ Perform Deauthentication Attack to disconnect clients from the real network.
2️⃣ Create a Fake Access Point with the same SSID.
3️⃣ Host a Phishing Login Page to steal credentials.
4️⃣ Store and Send Captured Data to the Telegram bot.


---

🔧 Troubleshooting

1️⃣ "Monitor mode not enabled" issue
```
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```
2️⃣ "Apache server not running" issue

sudo service apache2 restart

3️⃣ "No packets being sent" issue
```
sudo iwconfig
```
Check the correct adapter name and update it in df_evil_twin.py.


---

🚀 After executing all the commands above, the tool should be fully operational!




---

## ⚙️ Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/MohamedAbuAl-Saud/DF_Evil_Twin
cd DF_Evil_Twin
sudo chmod +x install.sh
./install.sh
sudo apt update && sudo apt upgrade -y
sudo apt install aircrack-ng hostapd dnsmasq apache2 php unzip git -y
sudo airmon-ng check kill
sudo airmon-ng start wlan0
sudo python3 df_evil_twin.py
```
---------------------
The End ✨🌏
آلقيـــــــــــــــآدهہ‌‏ آلزعيـــم♕
DF♕

