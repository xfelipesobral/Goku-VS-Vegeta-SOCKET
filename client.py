from funcoes import *

HOST = 'localhost' 
PORT = 5000     

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

#udp.sendto (msg.encode(), dest)
enviar(udp, "NOVOJOGADOR$x", dest)
enviar(udp, "JOGADORES$x", dest)

while True:
    data, ip = udp.recvfrom(1500)

    data = data.decode()
    data = data.split('$')
    chave = data[0]

    if(chave == "JOGADORES"):
        print(data[1])

udp.close()
'''

'''