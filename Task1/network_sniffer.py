from scapy.all import sniff, IP, TCP, UDP, ICMP
import csv
import sys
from scapy.config import conf

# Check if npcap/pcap is available
if not conf.use_pcap:
    print("⚠️ Warning: No Npcap/WinPcap found. Please install Npcap from https://nmap.org/npcap/")
    sys.exit(1)

# File to save captured packets
OUTPUT_FILE = "captured_packets.csv"

# Function to handle each packet
def capture_packet(packet):
    # Default values
    src_ip = dst_ip = protocol = src_port = dst_port = payload = "N/A"

    # Check if packet has IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Detect protocol name
        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = "Other"

    # Get some payload data if available
    if packet.haslayer("Raw"):
        payload = packet["Raw"].load[:30]  # first 30 bytes only

    # Print results on screen
    print(f"\nPacket: {protocol} | {src_ip}:{src_port} --> {dst_ip}:{dst_port}")
    print(f"Payload: {payload}")

    # Save to CSV
    with open(OUTPUT_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([protocol, src_ip, src_port, dst_ip, dst_port, payload])

# Create CSV file with headers
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Protocol", "Source IP", "Source Port", "Destination IP", "Destination Port", "Payload"])

print(" Starting network sniffer... (Press Ctrl+C to stop)")
sniff(prn=capture_packet, count=10)  # Capture 10 packets only
print(f"\n Packets saved to {OUTPUT_FILE}")
