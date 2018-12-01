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

		if player.x > PAREDE_DIREITA:
			player.x = PAREDE_DIREITA
		elif player.x < PAREDE_ESQUERDA:
			player.x = PAREDE_ESQUERDA	

		return player

def pular(player):
	if player.dy == 0:
		pass
	else:
		while player.y < PULO:
			player.y = player.y + player.dy
		
		return player

def descer(player):
	if player.dy == 0:
		pass
	else:
		while player.y > CHAO:
			player.y = player.y - player.dy
		
		return player
			

def mover_jogo(jogo):

	try:
		mover_player(jogo.jogador)
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

	fonte = pg.font.SysFont("monospace", 40)


	try:
		TELA.blit(IMG_LIFE, (X_LIFE, Y_LIFE))
		textoP1= fonte.render(str(jogo.jogadores[0].hp), 1, (255, 255, 255))
		TELA.blit(textoP1, (X_LIFE+32, Y_LIFE-5))		
	except: 
		TELA.blit(IMG_DISCONNECT, (X_LIFE+32, Y_LIFE))

	try:
		TELA.blit(IMG_LIFE, (X_LIFE2, Y_LIFE))
		textoP2 = fonte.render(str(jogo.jogadores[1].hp), 1, (255, 255, 255))
		TELA.blit(textoP2, (X_LIFE2-72, Y_LIFE-5))
	except: 
		TELA.blit(IMG_DISCONNECT, (X_LIFE2-32, Y_LIFE))
	
	
	

	


'''
# TRATA_TECLA
'''

def trata_tecla_player(player, tecla):
	if (tecla == pg.K_LEFT) or (tecla == pg.K_LEFT and pg.K_SPACE):
		player.dx = -DX
	elif (tecla == pg.K_RIGHT) or (tecla == pg.K_RIGHT and pg.K_SPACE):
		player.dx = DX
	elif (tecla == pg.K_UP):
		print("PULAR")
		#player.dy = DY
		#pular(player)
		
	
	
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

