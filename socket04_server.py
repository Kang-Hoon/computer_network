from socket import *

host = '127.0.0.1' #localhost IP
port = 1234

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
data_string = data.decode('utf-8')

if (data_string.isupper == True):
    data_string2 = data_string.lower()
elif (data_string.isupper == True):
    data_string2 = data_.upper()
    
print('받은 데이터 : ', data_string2)

connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')

