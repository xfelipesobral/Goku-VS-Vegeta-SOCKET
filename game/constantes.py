#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game.universe import *
import random

'''
====================
 TELA E CONSTANTES
====================
'''

(LARGURA, ALTURA) = (800, 640)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_P1 = pg.image.load('images/crono_left.gif')
    IMG_P2 = pg.image.load('images/p2.png')
    IMG_BACKGROUND = pg.image.load('images/bg.png')
    IMG_LIFE = pg.image.load('images/life.png')
    IMG_DISCONNECT = pg.image.load('images/connect.png')

except:
    IMG_P1 = pg.Surface((100,100),pg.SRCALPHA)
    IMG_P2 = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BACKGROUND = pg.Surface((100,100),pg.SRCALPHA)
    IMG_LIFE = pg.Surface((100,100),pg.SRCALPHA)
    IMG_DISCONNECT = pg.Surface((100,100),pg.SRCALPHA)
    print("IMAGENS NÃO CARREGADAS!!!")

IMG_LIFE = pg.transform.scale(IMG_LIFE, (32, 32))
IMG_DISCONNECT = pg.transform.scale(IMG_DISCONNECT, (32, 32))

DX = 10
DY = 10

PAREDE_ESQUERDA = 0
PAREDE_DIREITA = LARGURA
PAREDE_CIMA = 0
PAREDE_BAIXO = ALTURA
CHAO = ALTURA - 60
PULO = CHAO+80

Y_LIFE = PAREDE_BAIXO - (IMG_LIFE.get_width()+10)
X_LIFE = PAREDE_ESQUERDA + IMG_LIFE.get_width()/2

X_LIFE2 = PAREDE_DIREITA - (IMG_LIFE.get_width()+IMG_LIFE.get_width()/2)