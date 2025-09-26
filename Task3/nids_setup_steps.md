
🛡️ NIDS Setup Guide (Beginner Friendly)

This guide will help you set up a **Network Intrusion Detection System (NIDS)** using **Snort** with step-by-step instructions.  

🔹 Step 1: Install Snort
On linux, update your system and install Snort:

```bash
sudo apt update
sudo apt install snort -y
During installation, it may ask:

Network interface → usually eth0 (check with ip a)

Home network → for most setups, 192.168.1.0/24

Verify installation:

bash
snort -V

🔹 Step 2: Prepare a Custom Rules File
We will use the file rules.conf (included in this repo).
This file contains beginner-friendly rules to detect traffic like Ping, FTP, SSH, HTTP, DNS, and suspicious scans.

🔹 Step 3: Run Snort with Custom Rules
Use Snort with your rules file:

bash
sudo snort -A console -q -c rules.conf -i eth0

Explanation of options:
-A console → Show alerts in the terminal

-q → Quiet mode (fewer logs)

-c rules.conf → Use custom rule file

-i eth0 → Listen on interface eth0

🔹 Step 4: Generate Test Traffic
Open another terminal and run some simple commands to trigger rules:

bash
# ICMP traffic
ping google.com

# HTTP traffic
curl http://example.com

# Telnet (if installed)
telnet 192.168.1.1

# FTP connection (if server available)
ftp 192.168.1.1
Snort should generate alerts in your first terminal.

🔹 Step 5: Save Alerts to Log File 
To log alerts into a file instead of console:

bash
sudo snort -A fast -c rules.conf -i eth0 -l /var/log/snort/

Check logs with:
bash
cat /var/log/snort/alert
