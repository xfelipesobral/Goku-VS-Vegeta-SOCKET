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

def objToJson(obj):
    return json.dumps(obj.__dict__)

'''
====================
	  JOGADOR
====================
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

def criarJogador(data):
    data = json.loads(data)
    jogador = Jogador(int(data["id"]), data["ip"], int(data["x"]), int(data["y"]), int(data["dx"]), int(data["dy"]), int(data["dmp"]), int(data["direct"]), int(data["hp"]), int(data["mp"]))
    return jogador

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

def enviarJogador(jogador):
    data = "ATUALIZAR_JOGADOR$"+str(objToJson(jogador))
    enviar(data)


'''
====================
	  PODER
====================
'''
class Poder:
    def __init__(self, id_dono, x, x_f, y, direct):
        self.id_dono = id_dono
        self.x = x
        self.x_f = x_f
        self.y = y 
        self.dx = 25
        self.dano = 30
        self.custo = 15
        self.direct = direct

def criarPoder(data):
    data = json.loads(data)
    poder = Poder(int(data["id_dono"]), int(data["x"]), int(data["x_f"]), int(data["y"]), int(data["direct"]))
    return poder

def enviarPoder(poder):
    data = "ATUALIZAR_PODER$"+str(json.dumps(poder.__dict__))
    enviar(data)

def soltarPoder(poderes, jogador):
	x_f = 0
	direct = -1
	if(jogador.direct == 1):
		x_f = 640
		direct = 1

	if(jogador.mp>15):
		novo = Poder(jogador.id, jogador.x+(32*direct), x_f, jogador.y, direct)
		novo.dx = novo.dx * novo.direct
		enviarPoder(novo)
		poderes.append(novo)
			
	return poderes

def atualizarPoder(data, jogo):
    if(jogo.jogador.mp > 15):
        novo = criarPoder(data)
        novo.dx = novo.dx * novo.direct
        jogo.poderes.append(novo)


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
