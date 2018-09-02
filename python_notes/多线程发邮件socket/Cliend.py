from socket import *

HOST = 'localhost'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('> ')
    if not data :
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZ)
    data = data.decode()

    print(type(data))
    if not data :
        break
    print('data:{}'.format(data))
udpCliSock.close();