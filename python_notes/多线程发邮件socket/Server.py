from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET , SOCK_DGRAM)

udpSerSock.bind(ADDR)

while True:
    print('waitint for message.....')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    print('接收的data:{}'.format(data))
    data = data.decode()
    udpSerSock.sendto(('[%s] %s' %(ctime(),data)).encode(), addr)
    print('....received from and returned to:', str(addr))

udpSerSock.close()