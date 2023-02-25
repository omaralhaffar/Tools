import subprocess as sub
import termcolor as color
import optparse as pars
import scapy.all as scap


# This is reader To use
paser = pars.OptionParser()
paser.add_option("-i", dest="ipaddress")
options, arguments = paser.parse_args()

# check if everthing is good
if not options.ipaddress:
    sub.call("clear", shell=True)
    print("\t")
    color.cprint("|-------------------------------------------------------------------|", "yellow")
    color.cprint("|                Please inter your ip address with in your range    |", "red")
    color.cprint("|-------------------------------------------------------------------|", "yellow")
    print("|\t                                                            |")
    color.cprint("|-------------------------------------------------------------------|", "yellow")
    color.cprint("|                 exaple = 192.168.50.1/24\t                    |", "red")
    color.cprint("|-------------------------------------------------------------------|", "yellow")
    sub.call("sleep 2", shell=True)

# The end of the reader


send = scap.arping(options.ipaddress)
