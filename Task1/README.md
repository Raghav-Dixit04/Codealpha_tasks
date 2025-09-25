Task 1: Basic Network Sniffer

 📌 Objective
Build a beginner-friendly Python program to capture network traffic, analyze it, and save results for offline review.

- Written in Python using **Scapy**
- Captures:
  - Source & Destination IP
  - Protocol (TCP, UDP, ICMP)
  - Port numbers (if available)
  - First 30 bytes of payload
- Displays results in terminal
- Saves results to `captured_packets.csv` automatically

## ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install scapy

    Install Npcap

(important for Windows users)

Open Command Prompt as Administrator and run:

python network_sniffer.py
