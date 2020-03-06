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
		#print ("src: "+str(ip_src)+" dest: "+str(ip_dst))
		if pkt.haslayer(DNS):
			if pkt.getlayer(DNS).qd.qname in domains:
				print("-----------------detected--------------------\n")
				print (str(ip_src) + " -> " + str(ip_dst) + " : " + "(" + pkt.getlayer(DNS).qd.qname + ")")


#these are the known domains that wannacry tries to reach, github.com. was added for testing
domains=("iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com.",
	"ifferfsodp9ifjaposdfjhgosurijfaewrwergwea.com.",
	"ayylmaotjhsstasdfasdfasdfasdfasdfasdfasdf.com.",
	"iuqssfsodp9ifjaposdfjhgosurijfaewrwergwea.com.",
	"iuqerfsodp9ifjaposdfjhgosurijfaewrwergweb.com.",
	"github.com.")

sniff(iface = interface,prn = querysniff, store = 0)

#the following line can be used to detect connection to samba
#sniff(iface = interface,filter = "port 445", prn = querysniff, store = 0)

print ("\n[*] Shutting Down...")