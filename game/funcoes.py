#!/usr/bin/env python
# -*- coding: utf-8 -*-
from game.dados import *
import math
import random

'''
====================
	  FUNCOES
====================
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
	if jogo.p1.hp < 0 or jogo.p2.hp < 0:
		print("JOGO TERMINOU")
	
	mover_player(jogo.p1)
	mover_player(jogo.p2)
 
	return jogo

## DESENHA JOGO

def desenha_p1(p1):
	TELA.blit(IMG_P1,(p1.x - IMG_P1.get_width()/2, p1.y - IMG_P1.get_height()/2))

def desenha_p2(p2):
	TELA.blit(IMG_P2,(p2.x - IMG_P2.get_width()/2, p2.y - IMG_P2.get_height()/2))

def desenha_jogo(jogo):
	TELA.blit(IMG_BACKGROUND, (0,0))

	desenha_p1(jogo.p1)
	desenha_p2(jogo.p2)

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
	jogo.p1 = trata_tecla_player(jogo.p1, tecla)
	jogo.p2 = trata_tecla_player(jogo.p2, tecla)
	return jogo

def trata_solta_tecla(jogo, tecla):
	jogo.p1 = trata_solta_tecla_player(jogo.p1, tecla)
	jogo.p2 = trata_solta_tecla_player(jogo.p2, tecla)
	return jogo

