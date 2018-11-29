#!/usr/bin/env python
# -*- coding: utf-8 -*-
from game.dados import *
from game.players import *
import socket
import math
import random

'''
====================
	  FUNCOES
====================
'''
'''
## CLIENT
def enviar(udp, data, destino):
    udp.sendto(data.encode(), destino)

def initClient(jogo):
    HOST = 'localhost' 
    PORT = 5000     

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)

    enviar(udp, "CONECTEI$jogo", dest)

    while True:
        data = udp.recv(1024)

        data = data.decode()
        data = data.split('$')
        chave = data[0]

        if(chave == "CONECTEI"):
            if(data[1] != "conectou"):
                udp.close()
            else:
                print("CONECTADO")

        if(chave == "NEW_PLAYER"):
            initMain(data[1], jogo)

        if(chave == "BROADCAST_PLAYER"):
            atualizarJogador(data[1], jogo)
    
    udp.close()
'''
## MOVER JOGO

def mover_player(player):
	if player.x < 0 or player.x > LARGURA:
		return "POSICAO INVALIDA"
	else: 
		player.x = player.x + player.x

		if player.x > PAREDE_DIREITA:
			player.x = PAREDE_DIREITA
		elif player.x < PAREDE_DIREITA:
			player.x = PAREDE_ESQUERDA
		
		return player

def mover_jogo(jogo):
	for jogador in jogo.jogadores:
		if jogador.hp < 0:
			print("JOGO TERMINOU")
			
		mover_player(jogador)
 
	return jogo

## DESENHA JOGO

def desenha_jogador(j):
	TELA.blit(IMG_P1,(j.x - IMG_P1.get_width()/2, j.y - IMG_P1.get_height()/2))

def desenha_jogo(jogo):
	TELA.blit(IMG_BACKGROUND, (0,0))

	for jogador in jogo.jogadores:
		desenha_jogador(jogador)

	#fonte = pg.font.SysFont("monospace", 40)


## TRATA TECLA JOGO

def trata_tecla_player(player, tecla):
	if (tecla == pg.K_LEFT) or (tecla == pg.K_LEFT and pg.K_SPACE):
		player.dx = -DX
	elif (tecla == pg.K_RIGHT) or (tecla == pg.K_RIGHT and pg.K_SPACE):
		player.dx = DX
	
	return player

def trata_solta_tecla_player(player, tecla):
	
	return player

def trata_tecla(jogo, tecla):
	jogo.jogador = trata_tecla_player(jogo.jogador, tecla)
	return jogo

def trata_solta_tecla(jogo, tecla):
	jogo.jogador = trata_solta_tecla_player(jogo.jogador, tecla)
	return jogo

