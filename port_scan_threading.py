#!/usr/bin/env python

# https://securitylair.wordpress.com/2014/02/21/simple-port-scanner-in-python-with-scapy-2/
 
import time
import Queue
import threading
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
ip = "34.237.72.89"
ports = range(0, 1000)
closed = 0
 
class Scanner(threading.Thread):
    """ Scanner Thread class """
    def __init__(self, test_port_queue, open_port_queue, lock):
        super(Scanner, self).__init__()
        self.test_port_queue = test_port_queue
        self.open_port_queue = open_port_queue
        self.lock = lock
 
    def run(self):
        global closed
        src_port = RandShort()
        port = self.test_port_queue.get()
        p = IP(dst=ip)/TCP(sport=src_port, dport=port, flags='S')
        resp = sr1(p, timeout=2)
        if str(type(resp)) == "<type 'NoneType'>":
            with self.lock:
                closed += 1
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:
                send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags='AR'), timeout=1)
                with self.lock:
#                    print "[*] %d open" % port
                    self.open_port_queue.put(port)
            elif resp.getlayer(TCP).flags == 0x14:
                with self.lock:
                    closed += 1
        self.test_port_queue.task_done()

 
def is_up(ip):
    p = IP(dst=ip)/ICMP()
    resp = sr1(p, timeout=10)
    if resp == None:
        return False
    elif resp.haslayer(ICMP):
        return True


def get_open_ports(ip, max_port=1024):
    conf.verb = 0

    lock = threading.Lock()
    test_port_queue = Queue.Queue()
    open_port_queue = Queue.Queue()

    if is_up(ip):
        print "Host %s is up, start scanning" % ip
        for port in range(0, max_port):
            test_port_queue.put(port)
            scan = Scanner(test_port_queue, open_port_queue, lock)
            scan.start()
        test_port_queue.join()
    else:
        print "IP %s not up" % ip

    return list(open_port_queue.queue)
        

if __name__ == '__main__':
    open_ports = get_open_ports("34.237.72.89", max_port=90)
    print "Open ports: %s" % open_ports
    #conf.verb = 0
    #start_time = time.time()
    #ports = range(1, 1024)
    #lock = threading.Lock()
    #queue = Queue.Queue()
    #queue2 = Queue.Queue()
    #if is_up(ip):
    #    print "Host %s is up, start scanning" % ip
    #    for port in ports:
    #        queue.put(port)
    #        scan = Scanner(queue, queue2, lock)
    #        scan.start()
    #    queue.join()
    #    duration = time.time()-start_time
    #    print "%s Scan Completed in %fs" % (ip, duration)
    #    print "%d closed ports in %d total port scanned" % (closed, len(ports))
    #else:
    #    print "Host %s is Down" % ip
