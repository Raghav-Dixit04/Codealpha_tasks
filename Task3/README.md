
 🛡️ Network Intrusion Detection System (NIDS) Setup

This project is a **beginner-friendly implementation of a Network Intrusion Detection System (NIDS)** using **Snort**.  
It continuously monitors network traffic and detects suspicious activity based on custom rules. 

 🚀 Features
- Capture and analyze network traffic in real time  
- Detect suspicious packets using simple rules  
- Generate alerts for potential intrusions  
- Beginner-friendly configuration and examples  

## 🛠️ Tools Used
- [Snort](https://www.snort.org/) – Open-source intrusion detection system  
- [Suricata](https://suricata.io/) – Alternative IDS/IPS engine  

 ✅ Example Usage
Run Snort with your custom rules file:

```bash
sudo snort -A console -q -c rules.conf -i eth0
-A console → Show alerts in the terminal

-q → Quiet mode (less logs)

-c rules.conf → Use custom rules

-i eth0 → Monitor your network interface

👨‍💻 Author: Raghav Dixit
