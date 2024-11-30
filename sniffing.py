from scapy.all import sniff

def packet_callback(packet):
    """This function will be called for every packet captured."""
    print(packet.summary())  # Print a summary of the packet

# Capture packets
# Replace 'eth0' with the appropriate network interface (on Windows, it could be something like 'Wi-Fi')
# 'count' specifies how many packets to capture. You can set it to 0 to capture indefinitely.
sniff( count=10, prn=packet_callback, store=0)  # Capture 10 packets

