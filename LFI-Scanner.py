

import time
import requests

import  signal
import sys


print """


 __        ________  ______         ______                                                              
/  |      /        |/      |       /      \                                                             
$$ |      $$$$$$$$/ $$$$$$/       /$$$$$$  |  _______   ______   _______   _______    ______    ______  
$$ |      $$ |__      $$ |        $$ \__$$/  /       | /      \ /       \ /       \  /      \  /      \ 
$$ |      $$    |     $$ |        $$      \ /$$$$$$$/  $$$$$$  |$$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$ |      $$$$$/      $$ |         $$$$$$  |$$ |       /    $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ |_____ $$ |       _$$ |_       /  \__$$ |$$ \_____ /$$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$/ $$ |      
$$       |$$ |      / $$   |      $$    $$/ $$       |$$    $$ |$$ |  $$ |$$ |  $$ |$$       |$$ |      
$$$$$$$$/ $$/       $$$$$$/        $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/ $$/   $$/  $$$$$$$/ $$/       
                                                                                                        
                                                                                                        
                                                                                                        




          _       _         ___        ___   ___  
    ____ (_)     | |       / _ \      / _ \ / _ \ 
   / __ \ _ _ __ | |___  _| | | |_  _| (_) | | | |
  / / _` | | '_ \| __\ \/ / | | \ \/ /> _ <| | | |
 | | (_| | | | | | |_ >  <| |_| |>  <| (_) | |_| |
  \ \__,_|_|_| |_|\__/_/\_\\___//_/\_\\___/ \___/ 
   \____/                                         
                                                  


 
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
