import scapy.all as scapy

def analyze_pcap(pcap_file):
    # Open pcap file
    packets = scapy.rdpcap(pcap_file)

    # Dictionary to store unique source IP-MAC mappings
    source_mappings = {}

    # Iterate over each packet in the pcap file
    for packet in packets:
        # Check if the packet has both IP and Ethernet layers
        if packet.haslayer(scapy.IP) and packet.haslayer(scapy.Ether):
            src_ip = packet[scapy.IP].src
            src_mac = packet[scapy.Ether].src

            # Add or update source IP-MAC mapping
            source_mappings[src_ip] = src_mac

    # Detect potential MITM activity
    mitm_detected = False
    for packet in packets:
        # Check if the packet has both IP and Ethernet layers
        if packet.haslayer(scapy.IP) and packet.haslayer(scapy.Ether):
            src_ip = packet[scapy.IP].src
            src_mac = packet[scapy.Ether].src
            dst_ip = packet[scapy.IP].dst
            dst_mac = packet[scapy.Ether].dst

            # Check if source IP does not match the expected MAC address
            if src_ip in source_mappings and source_mappings[src_ip] != src_mac:
                print(f"Potential MITM detected: {src_mac} ({src_ip}) is impersonating {source_mappings[src_ip]}")

                # Optionally, you can add more logic here to handle the detection
                mitm_detected = True

    if not mitm_detected:
        print("No potential MITM activity detected.")

if __name__ == "__main__":
    pcap_file = "net.pcap"  # Change this to your pcap file name
    analyze_pcap(pcap_file)
