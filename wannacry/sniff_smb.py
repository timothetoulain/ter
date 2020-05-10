#run on linux
#print all dns requests for the given domains
from scapy.all import *
import sys 

try:
	interface = raw_input("[*] Enter Desired Interface: ")
except KeyboardInterrupt:
	print ("[*] User Requested Shutdown...")
	print ("[*] Exiting...")
	sys.exit(1)
 
def querysniff(pkt):
	if IP in pkt:
		ip_src = pkt[IP].src
		ip_dst = pkt[IP].dst   
		print ("\nTraffic detected on port 445:\nsrc: "+str(ip_src)+" dest: "+str(ip_dst))
		



#detect connection to samba (must change port to 445)
sniff(iface = interface,filter = "port 443", prn = querysniff, store = 0)

print ("\n[*] Shutting Down...")