#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game.constantes import *

'''
====================
	 DEF. DADOS
====================
'''

from namedlist import namedlist

P1 = namedlist("P1", "x, y, dx, dy, hp")
P1_PADRAO = P1(PAREDE_ESQUERDA, PAREDE_BAIXO, 0, 0, 100)

P2 = namedlist("P1", "x, y, dx, dy, hp")
P2_PADRAO = P2(PAREDE_DIREITA, PAREDE_BAIXO, 0, 0, 100)

Jogo = namedlist("Jogo", "p1, p2, game_ganho")

JOGO_INICIAL = Jogo(P1_PADRAO, P2_PADRAO, False)

