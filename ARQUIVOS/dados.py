#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes import *
from namedlist import namedlist

p1 = Jogador()
p2 = Jogador()

Jogo = namedlist("Jogo", "p1, p2, game_over, game_ganho")

JOGO_INICIAL = Jogo(p1, p2, False, False)

def jogo_inicial():
    p1.set_posicao(p1.PAREDE_ESQUERDA)
    p2.set_posicao(p2.PAREDE_DIREITA)

    return Jogo(p1, p2, False, False)