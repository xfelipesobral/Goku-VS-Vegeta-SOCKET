#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    dado = chave[1]
    chave = chave[0]

    if(chave == "CONECTEI"):
        print(ip)
        player = Jogador(lastPlayerID, ip, 350, 580, 0, 0, 100, 50)
        lastPlayerID += 1
        player.inserir()
        ipConectados.append(ip)
        enviar(udp, "CONECTEI$conectou", ip)
        stringInitPlayer(udp, ip, player)
        atualizarJogadores(udp, ipConectados, jogadores)

    if(chave == "ATUALIZAR_JOGADOR"):
        attJogador(udp, ipConectados, dado)
        print("["+str(ip[0])+":"+str(ip[1])+"] "+str(data))

    #verificar(msg.decode(), cliente)
    #print (cliente, msg.decode())

udp.close()