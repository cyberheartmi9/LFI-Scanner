

import time
import requests

import  signal
import sys


print """



  _      ______ _____    _____                                 
 | |    |  ____|_   _|  / ____|                                
 | |    | |__    | |   | (___   ___ __ _ _ __  _ __   ___ _ __ 
 | |    |  __|   | |    \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |____| |     _| |_   ____) | (_| (_| | | | | | | |  __/ |   
 |______|_|    |_____| |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                               
                                                               


        ##################################################
        ##                                              ##
        ##                                              ##
        ##                                              ##
        ##   Author @intx0x80                           ##
        ##                                              ##
        ##      LFI Scanner                             ##
        ##                                              ##
        ##################################################

"""
def signal_handler(signal, frame):

    print "\n[-] Exiting"

    exit()

signal.signal(signal.SIGINT, signal_handler)



url=raw_input("Enter URL Address    ")






f=open('Payloads.txt','r')

for i in f.readlines():

    ur=requests.get(url+'{}'.format(i))
    if "root"in ur.content:
                print '#########################################'
                print   ' [Detect LFI]------->   '+'  Payload is  '+str(i)
                print '##########################################'
                time.sleep(2)

print "\n Not Vulnerable To  [LFI] "

print "\nScanning....... complete"




__author__ = 'Abdo sniper'
