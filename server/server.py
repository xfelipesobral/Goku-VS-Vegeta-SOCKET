from funcoes import *
from players_sv import *

HOST = 'localhost'    
PORT = 5000            

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

lastPlayerID = 0

print("SERVIDOR INICIALIZADO! [IP: "+HOST+":"+str(PORT)+"]")

while True:
    data, ip = udp.recvfrom(1500)

    chave = data.decode()
    chave = chave.split('$')
    chave = chave[0]

    if(chave == "NOVOJOGADOR"):
        jogadores.append("teste")

    if(chave == "JOGADORES"):
        enviar(udp, "JOGADORES$"+jogadores[0], ip)

    #verificar(msg.decode(), cliente)
    #print (cliente, msg.decode())


    
udp.close()