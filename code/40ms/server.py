import socket
import struct
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8000))
sock.listen()
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

while True:
    c,_ = sock.accept()
    v = time.perf_counter()
    while True:
        t = time.perf_counter()
        buf = c.recv(4096)
        u = time.perf_counter()
        print(' ', int(1000*(u-t)))
        if str(buf, 'utf-8').find("\r\n\r\n") != -1:
            buf = c.recv(4096) # get one more packet for the body
            break
    print(int(1000*(time.perf_counter() - v)))
    c.send(b'HTTP/1.1 200 OK\r\nContent-Length: 1\r\n\r\na\r\n')
    c.close()

