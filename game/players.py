#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import socket

'''
##  CONEXAO
'''

HOST = 'localhost' 
PORT = 5000     

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

def enviar(data):
    global udp
    global dest
    udp.sendto(data.encode(), dest)

enviar("CONECTEI$jogo")

'''
##  FUNCOES
'''

class Jogador:
    def __init__(self, id, ip, x, y, hp):
        self.id = id
        self.ip = ip
        self.x = x
        self.y = y
        self.hp = hp

def criarJogador(data):
    data = json.loads(data)
    jogador = Jogador(int(data["id"]), data["ip"], int(data["x"]), int(data["y"]), int(data["hp"]))
    return jogador

def initMain(data, jogo):
    jogo.jogador = criarJogador(data)
    print("PERSONAGEM CRIADO!")

def att(player, dados):
    player.x = dados["x"]
    player.y = dados["y"]
    player.hp = dados["hp"]

    return player

def atualizarJogador(data, jogo):
    verif = True

    player = json.loads(data)

    if(jogo.jogador == player["id"]):
        jogador = att(jogador, player)

    for jogador in jogo.jogadores:

        if(jogador.id == player["id"]):
            jogador = att(jogador, player)
            verif = False
        
    if(verif):
        jogo.jogadores.append(criarJogador(data))

def objToJson(obj):
    return json.dumps(obj.__dict__)

def enviarJogador(jogador):
    data = "ATUALIZAR_JOGADOR$"+str(objToJson(jogador))
    enviar(data)

'''
def testJSON():
    joao = Jogador(0, ["127.0.0.1", 5000], 0, 0, 1000)
    joaoJSON = json.dumps(joao.__dict__)

    novo = criarJogador(joaoJSON)

    print(novo.ip)
testJSON()
'''
