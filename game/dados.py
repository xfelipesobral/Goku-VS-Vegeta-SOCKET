#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game.constantes import *
from game.namedlist import namedlist
#from server.players_sv import jogadores

'''
====================
	 DEF. DADOS
====================
'''

P1 = namedlist("P1", "x, y, dx, dy, hp")
P1_PADRAO = P1(PAREDE_ESQUERDA, PAREDE_BAIXO, 0, 0, 100)

P2 = namedlist("P2", "x, y, dx, dy, hp")
P2_PADRAO = P2(PAREDE_DIREITA, PAREDE_BAIXO, 0, 0, 100)

Jogo = namedlist("Jogo", "jogador, jogadores, poderes, game_ganho")

JOGO_INICIAL = Jogo(None, [], [], [False])
JOGO_FINAL = Jogo(None, None, None, [True])

