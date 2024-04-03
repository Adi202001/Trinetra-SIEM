import scapy.all as scapy

def analyze_pcap(pcap_file):
    # Open pcap file
    packets = scapy.rdpcap(pcap_file)

    # Dictionary to store source IPs and their count
    src_ip_count = {}

    # Iterate over each packet in the pcap file
    for packet in packets:
        # Check if the packet is ICMP
        if packet.haslayer(scapy.ICMP):
            # Get the source IP
            src_ip = packet[scapy.IP].src

            # Increment count for source IP
            src_ip_count[src_ip] = src_ip_count.get(src_ip, 0) + 1

    # Check for ICMP flood (source IPs with high count)
    flood_threshold = 100  # Adjust as needed
    icmp_flood_detected = False
    for src_ip, count in src_ip_count.items():
        if count > flood_threshold:
            print(f"ICMP flood detected from {src_ip} with {count} packets.")
            icmp_flood_detected = True

    if not icmp_flood_detected:
        print("No ICMP flood detected.")

if __name__ == "__main__":
    pcap_file = "net.pcap"  # Change this to your pcap file name
    analyze_pcap(pcap_file)
