from scapy.all import *

for i in range(1,255):
	packet = IP(dst="eos-spine-1",src="10.0.0." + str(i),ttl=25)
	send(packet)
	print("victim sees 10.0.0." + str(i))

