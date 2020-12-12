import socket

s = socket.socket()

port = 8888

s.connect(('192.168.56.102', port))

file = open("sample.txt", "rb")
SendFile = file.read(1024)

while SendFile:
    data = s.recv(1024)
    print(data)
    
    s.send(SendFile)
    SendFile = file.read(1024)     
    
s.close()

