import scapy

packet = IP(dst="host3",ttl=25)

send(packet)
