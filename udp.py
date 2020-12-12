import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_IP_ADDRESS = "192.168.56.102"
UDP_PORT_NO = 7777
Message = "Hello, server"

s.sendto(Message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
