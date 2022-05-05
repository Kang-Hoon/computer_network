# 서버 소켓 세팅

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM) # Address Family & Socket Type
serverSock.bind(('', 8080))
serverSock.listen(1)

clientSock, addr = serverSock.accept()