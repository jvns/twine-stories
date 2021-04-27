import socket
s = socket.socket()
s.connect(("127.0.0.1", 8081))
s.send(b"GET / HTTP/1.1\r\n")
s.send(b"Host: example.com\r\n\r\n")
print(str(s.recv(4096)))
