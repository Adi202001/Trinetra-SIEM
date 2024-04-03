import scapy.all as scapy

def analyze_pcap(pcap_file):
    # Open pcap file
    packets = scapy.rdpcap(pcap_file)

    # Dictionary to store source IPs and their corresponding MAC addresses
    arp_cache = {}

    # Iterate over each packet in the pcap file
    for packet in packets:
        # Check if the packet is ARP
        if packet.haslayer(scapy.ARP):
            arp_packet = packet[scapy.ARP]
            src_ip = arp_packet.psrc
            src_mac = arp_packet.hwsrc

            # Add or update ARP cache
            arp_cache[src_ip] = src_mac

    # Detect ARP spoofing
    arp_spoofing_detected = False
    for packet in packets:
        if packet.haslayer(scapy.ARP):
            arp_packet = packet[scapy.ARP]
            src_ip = arp_packet.psrc
            src_mac = arp_packet.hwsrc
            dst_ip = arp_packet.pdst

            # Check if source MAC does not match the one in ARP cache
            if src_ip in arp_cache and arp_cache[src_ip] != src_mac:
                print(f"ARP spoofing detected: {src_mac} ({src_ip}) is spoofing {arp_cache[src_ip]} ({src_ip})")

                # Optionally, you can add more logic here to handle the detection
                arp_spoofing_detected = True

    if not arp_spoofing_detected:
        print("No ARP spoofing detected.")

if __name__ == "__main__":
    pcap_file = "example.pcap"  # Change this to your pcap file name
    analyze_pcap(pcap_file)
