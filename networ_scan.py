import scapy.all as scap
import optparse as pars
import termcolor as color
import subprocess as sub
import time
sub.call("clear", shell=True)

def reader():
   addop = pars.OptionParser()
   addop.add_option('-i', dest="ip_address", help="-i == ipaddress within your range")
   option, argument = addop.parse_args()
   if not option.ip_address:
       color.cprint("Plese check if you have your ip address insert", 'red')
       exit()
   return option

option = reader()


def arp_packet():
    arp_ip = scap.ARP(pdst=option.ip_address)
    arp_mac = scap.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_full = arp_mac/arp_ip
    return arp_full
arp_full = arp_packet()

def send_arp_packet():
    send2 = scap.srp(arp_full, timeout=1, verbose=False)[0]
    return send2

send = send_arp_packet()

color.cprint("Ip Address \t\t Mac Adress", 'red')
color.cprint("-" * 50, 'red')


def read_arp_packet():
    for answer in send:
        read_arp_amc = answer[1].hwsrc
        read_arp_ip = answer[1].psrc
        arp_p = color.cprint(read_arp_ip + "\t\t" + read_arp_amc, "green")

read_arp_packet()


try:
   while True:
     time.sleep(30)
     sub.call("python3 networ_scan.py -i  " + option.ip_address, shell=True )

except KeyboardInterrupt:
    color.cprint("exitting",'red')
 



 