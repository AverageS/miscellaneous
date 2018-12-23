from scapy.all  import *

packets = rdpcap('key.pcap')
s = b''
# Let's iterate through every packet
for packet in packets:
    try:
        packet[TCP]
    except:
        pass
    else:
        if packet[TCP].payload:
            s += packet[TCP].payload.load
    try:
        packet[UDP]
    except:
        pass
    else:
        if packet[UDP].payload:
            s += packet[UDP].payload.load

print(s)
