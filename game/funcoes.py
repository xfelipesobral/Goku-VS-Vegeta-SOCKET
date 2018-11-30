#!/usr/bin/env python
# -*- coding: utf-8 -*-
from game.dados import *
import socket
import math
import random

'''
====================
	  FUNCOES
====================
'''

'''
# MOVER_JOGO
'''

def mover_player(player):
	if player.x < 0 or player.x > LARGURA:
		return "POSICAO INVALIDA"
	else: 
		player.x = player.x + player.dx

		'''
		if player.x > PAREDE_DIREITA:
			player.x = PAREDE_DIREITA
		elif player.x < PAREDE_DIREITA:
			player.x = PAREDE_ESQUERDA
		'''
		
		return player

def mover_jogo(jogo):
	'''
	for jogador in jogo.jogadores:
		if jogador.hp < 0:
			print("JOGO TERMINOU")
			
		mover_player(jogador)'''

	try:
		'''for jogador in jogo.jogadores:
			if jogador.hp < 0:
				print("JOGO TERMINOU")
				
			mover_player(jogador)'''
		mover_player(jogo.jogador)
		#print(jogo.jogador.x)
	except:
		return jogo
 
	return jogo

'''
# DESENHA_JOGO
'''

def desenha_jogador(j):
	TELA.blit(IMG_P1,(j.x - IMG_P1.get_width()/2, j.y - IMG_P1.get_height()/2))

def desenha_jogo(jogo):
	TELA.blit(IMG_BACKGROUND, (0,0))

	for jogador in jogo.jogadores:
		desenha_jogador(jogador)

	#fonte = pg.font.SysFont("monospace", 40)


'''
# TRATA_TECLA
'''

def trata_tecla_player(player, tecla):
	if (tecla == pg.K_LEFT) or (tecla == pg.K_LEFT and pg.K_SPACE):
		player.dx = -DX
	elif (tecla == pg.K_RIGHT) or (tecla == pg.K_RIGHT and pg.K_SPACE):
		player.dx = DX
	
	return player

def trata_solta_tecla_player(player, tecla):
	if(tecla == pg.K_RIGHT or tecla == pg.K_LEFT):
		player.dx = 0
	return player

def trata_tecla(jogo, tecla):
	jogo.jogador = trata_tecla_player(jogo.jogador, tecla)
	return jogo

def trata_solta_tecla(jogo, tecla):
	jogo.jogador = trata_solta_tecla_player(jogo.jogador, tecla)
	return jogo

