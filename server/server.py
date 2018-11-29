from funcoes import *
from players_sv import *

HOST = 'localhost'    
PORT = 5000            

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

lastPlayerID = 0
ipConectados = list()

print("SERVIDOR INICIALIZADO! [IP: "+HOST+":"+str(PORT)+"]")


'''
    // ATUALIZAÇÕES

def atualizarJogadores():
    for jogador in jogadores:
        data = "BROADCAST_PLAYER$"+stringNewPlayer(jogador)
        enviar(udp, data, ipConectados)

def atualizarJogador(jogador):
    data = "BROADCAST_PLAYER$"+stringNewPlayer(jogador)
    enviar(udp, data, ipConectados)
'''

while True:
    data, ip = udp.recvfrom(1024)

    chave = data.decode()
    chave = chave.split('$')
    chave = chave[0]

    if(chave == "CONECTEI"):
        print(ip)
        player = Jogador(lastPlayerID, ip, 0, 0, 100)
        lastPlayerID += 1
        player.inserir()
        ipConectados.append(ip)
        enviar(udp, "CONECTEI$conectou", ip)
        stringInitPlayer(udp, ip, player)
        atualizarJogadores(udp, ipConectados, jogadores)


    
    if(chave == "JOGADORES"):
        enviar(udp, "JOGADORES$"+jogadores[0], ip)

    #verificar(msg.decode(), cliente)
    #print (cliente, msg.decode())

udp.close()

'''
+ quando conectar, cria novo jogador
+ servidor emite em broadcast todos jogadores
'''
