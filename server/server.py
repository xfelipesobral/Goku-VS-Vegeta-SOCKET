#!/usr/bin/env python
# -*- coding: utf-8 -*-

from funcoes import *

HOST = 'localhost'    
PORT = 5000            

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

lastPlayerID = 0
ipConectados = list()

atualizacoes = 0

print("SERVIDOR INICIALIZADO! [IP: "+HOST+":"+str(PORT)+"]")

while True:
    data, ip = udp.recvfrom(1024)

    chave = data.decode()
    chave = chave.split('$')
    dado = chave[1]
    chave = chave[0]

    if(chave == "CONECTEI"):
        if(lastPlayerID>1):
            enviar(udp, "KICK$SERVIDOR_CHEIO", ip)
        else:
            print(ip)
            if(lastPlayerID == 0):
                player = Jogador(lastPlayerID, ip, 100, 565, 0, 0, 0, 1, 100, 50)
            else:
                player = Jogador(lastPlayerID, ip, 700, 565, 0, 0, 0, -1, 100, 50)
            lastPlayerID += 1
            player.inserir()
            ipConectados.append(ip)
            enviar(udp, "CONECTEI$conectou", ip)
            stringInitPlayer(udp, ip, player)
            atualizarJogadores(udp, ipConectados, jogadores)

    if(chave == "ATUALIZAR_JOGADOR"):
        attJogador(udp, ipConectados, dado)
        #print(atualizacoes)
        atualizacoes += 1

    if(chave == "ATUALIZAR_PODER"):
        data = "BROADCAST_PODER$"+dado

        for ipX in ipConectados:
            if(ipX != ip):
                print(ipX)
                enviar(udp, data, ipX)

    #verificar(msg.decode(), cliente)
    #print (cliente, msg.decode())

udp.close()