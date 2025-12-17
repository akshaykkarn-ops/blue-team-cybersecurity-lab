from scapy.all import sniff, TCP, UDP, ICMP
from collections import Counter
import matplotlib.pyplot as plt

protocols = []

def analyze_packet(packet):
    if packet.haslayer(TCP):
        protocols.append("TCP")
    elif packet.haslayer(UDP):
        protocols.append("UDP")
    elif packet.haslayer(ICMP):
        protocols.append("ICMP")
    else:
        protocols.append("Other")

print("[+] Capturing 100 packets...")
sniff(count=100, prn=analyze_packet)

protocol_count = Counter(protocols)

print("\n[+] Protocol Distribution:")
for proto, count in protocol_count.items():
    print(f"{proto}: {count}")

# Plot bar chart
# Plot bar chart
plt.bar(protocol_count.keys(), protocol_count.values())
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")
plt.title("Network Protocol Distribution")

# Save instead of show
plt.savefig("protocol_distribution.png")
plt.close()

print("[+] Protocol distribution chart saved as protocol_distribution.png")
