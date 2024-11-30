#module scanner des hotes actifs sur le reseaux et affichage des adresse ip + mac:
import socket 
from scapy.all import *

network="192.168.1.0"

def get_mac(addr):
    frame=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=addr)
    reponse=srp1(frame,verbose=False,timeout=2)
    if reponse:
      return reponse.hwsrc

net=network.split('.')
a='.'
ip=net[0]+a+net[1]+a+net[2]+a
for i in range(1, 5):
    dest=ip+str(i)   
    p=IP(dst=dest)/ICMP()
    rep=sr1(p,verbose=0,timeout=2)
    if rep: 
      if rep.type==0:
        adresseip=rep.src
        print(adresseip)
        mac=get_mac(adresseip)
        print(mac)
        hostname=socket.gethostbyaddr(adresseip)
        print(hostname)
        
        

  
  


