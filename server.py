from socket import *
import random

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print('Sunucu hazir bekliyor')

while 1:
     connectionSocket, addr = serverSocket.accept()
     print('Yeni istemci baglandi')

     connectionSocket.send(b"Hosgeldiniz, isminiz nedir?")

     #sentence = connectionSocket.recv(1024)

     #capitalizedSentence = sentence.upper()
     #connectionSocket.send(capitalizedSentence)

     modifiedSentence = connectionSocket.recv(1024)
     print('Istemciye cevap gonderildi', modifiedSentence.decode())


     
     ilk_sayi = random.randint(0, 9)
     ikinci_sayi = random.randint(0, 9)
     operator = random.randint(0, 3)
     cevap = 0
     operotorstr = ""

     if operator == 0: # +
          cevap = ilk_sayi + ikinci_sayi
          operotorstr = "+"
     elif operator == 1: # -
          cevap = ilk_sayi - ikinci_sayi
          operotorstr = "-"
     elif operator == 2: # *
          cevap = ilk_sayi * ikinci_sayi
          operotorstr = "*"
     elif operator == 3: # /
          cevap = ilk_sayi / ikinci_sayi
          operotorstr = "/"

     strifade = ("Hosgeldin " + modifiedSentence.decode() + ". Yandaki sorunun cevabi nedir?: " + str(ilk_sayi) + " " + operotorstr + " " + str(ikinci_sayi) + " = ?")
     connectionSocket.send(strifade.encode())

     modifiedSentence = connectionSocket.recv(1024)
     print('Istemciye cevap gonderildi', modifiedSentence.decode())




     if str(cevap) == modifiedSentence.decode():
          strifaaade = "Dogru cevap: " + str(cevap) + ", Verdigin cevap: " + modifiedSentence.decode() + ", Tebrikler Dogru!"
     else:
          strifaaade = "Dogru cevap: " + str(cevap) + ", Verdigin cevap: " + modifiedSentence.decode() + ", Maalesef Yanlis!"
     


     connectionSocket.send(strifaaade.encode())
     modifiedSentence = connectionSocket.recv(1024)
     print('Istemciye cevap gonderildi', modifiedSentence.decode())

     



     connectionSocket.close()
     print('Istemci ile baglanti sonlandirildi')
     break
