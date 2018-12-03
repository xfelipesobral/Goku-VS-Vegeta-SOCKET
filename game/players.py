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
    def __init__(self, id, ip, x, y, dx, dy, dmp, direct, hp, mp):
        self.id = id
        self.ip = ip
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.dmp = dmp
        self.direct = direct
        self.hp = hp
        self.mp = mp

class Poder:
    def __init__(self, id_dono, x, y):
        self.id_dono = id_dono
        self.x = x
        self.y = y 
        self.dx = 25
        self.dano = 30
        self.custo = 15
        self.status = 0

        # 0 -> Novo / 1 -> Caminhando / 2 -> Colidiu / 3 -> Excluir

def criarJogador(data):
    data = json.loads(data)
    jogador = Jogador(int(data["id"]), data["ip"], int(data["x"]), int(data["y"]), int(data["dx"]), int(data["dy"]), int(data["dmp"]), int(data["direct"]), int(data["hp"]), int(data["mp"]))
    return jogador

def criarPoder(data):
    data = json.loads(data)
    poder = Poder(int(data["id_dono"]), int(data["x"]), int(data["y"]))
    return poder

def initMain(data, jogo):
    jogo.jogador = criarJogador(data)
    print("PERSONAGEM CRIADO!")

def att(player, dados):
    player.x = dados["x"]
    player.y = dados["y"]
    player.hp = dados["hp"]
    player.dmp = dados["dmp"]
    player.dx = dados["dx"]
    player.dy = dados["dy"]
    player.mp = dados["mp"]
    player.direct = dados["direct"]

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

def atualizarPoder(data, jogo):
     # 0 -> Novo / 1 -> Caminhando / 2 -> Colidiu / 3 -> Excluir

    dados = json.loads(data)

    if dados["status"] == 0:
        jogo.poderes.append(criarPoder(data))

    for poder in jogo.poderes:
        poder.status = dados["status"]
        if(poder.status == 1 and poder.stauts == 2):
            poder.x = dados["x"]
        elif(poder.status == 3):
            jogo.poderes.remove(poder)

    
def objToJson(obj):
    return json.dumps(obj.__dict__)

def enviarJogador(jogador):
    data = "ATUALIZAR_JOGADOR$"+str(objToJson(jogador))
    enviar(data)

def enviarPoderes(poderes):
    json_p = []
    for poder in poderes:
        json_p.append(json.dumps(poder.__dict__))

    data = "ATUALIZAR_PODERES$"+str(json.dumps(json_p))
    enviar(data)

'''
def testJSON():
    joao = Jogador(0, ["127.0.0.1", 5000], 0, 0, 1000)
    joaoJSON = json.dumps(joao.__dict__)

    novo = criarJogador(joaoJSON)

    print(novo.ip)
testJSON()
'''


'''

ATUALIZA O SERVIDOR QUANDO É LANÇADO
ATUALIZA O SERVIDOR QUANDO CHEGA NO FINAL OU QUANDO BATE NO PERSONAGEM

'''