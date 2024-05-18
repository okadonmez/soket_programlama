from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 



modifiedSentence = clientSocket.recv(1024)

print ('Sunucudan gelen mesaj: ', modifiedSentence.decode())


sentence = input()

clientSocket.send(sentence.encode())


modifiedSentence = clientSocket.recv(1024)

print ('Sunucudan gelen mesaj: ', modifiedSentence.decode())


sentence = input()

clientSocket.send(sentence.encode())


modifiedSentence = clientSocket.recv(1024)

print ('Sunucudan gelen mesaj: ', modifiedSentence.decode())


clientSocket.close()