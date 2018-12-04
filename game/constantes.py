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
    IMG_GOKU_PARADO = pg.image.load('images/goku/parado.png')
    IMG_GOKU_ANDANDO = pg.image.load('images/goku/andando.png')
    IMG_GOKU_ATIRANDO = pg.image.load('images/goku/atirando.png')
    IMG_GOKU_KI = pg.image.load('images/goku/ki.png')
    IMG_GOKU_TIRO = pg.image.load('images/goku/tiro.png')

    IMG_VEGETA_PARADO = pg.image.load('images/vegeta/parado.png')
    IMG_VEGETA_ANDANDO = pg.image.load('images/vegeta/andando.png')
    IMG_VEGETA_ATIRANDO = pg.image.load('images/vegeta/atirando.png')
    IMG_VEGETA_KI = pg.image.load('images/vegeta/ki.png')
    IMG_VEGETA_TIRO = pg.image.load('images/vegeta/tiro.png')

    IMG_P1 = pg.image.load('images/goku/parado.png')
    IMG_P2 = pg.image.load('images/p2.png')
    IMG_BACKGROUND = pg.image.load('images/bg.png')
    IMG_LIFE = pg.image.load('images/life.png')
    IMG_DISCONNECT = pg.image.load('images/connect.png')

    IMG_KI = pg.image.load('images/ki.png')

except:
    IMG_P1 = pg.Surface((100,100),pg.SRCALPHA)
    IMG_P2 = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BACKGROUND = pg.Surface((100,100),pg.SRCALPHA)
    IMG_LIFE = pg.Surface((100,100),pg.SRCALPHA)
    IMG_DISCONNECT = pg.Surface((100,100),pg.SRCALPHA)
    print("IMAGENS NÃO CARREGADAS!!!")

IMG_LIFE = pg.transform.scale(IMG_LIFE, (32, 32))
IMG_DISCONNECT = pg.transform.scale(IMG_DISCONNECT, (32, 32))
IMG_KI = pg.transform.scale(IMG_KI, (32, 32))

#IMG_GOKU_ANDANDO_V = pg.transform.flip(IMG_GOKU_ANDANDO, True, False)
#IMG_VEGETA_ANDANDO_V = pg.transform.flip(IMG_VEGETA_ANDANDO, True, False)

'''
### IMAGENS DOS PERSONAGENS
'''
IMG_GOKU = [IMG_GOKU_PARADO, IMG_GOKU_ANDANDO, IMG_GOKU_KI, IMG_GOKU_ATIRANDO, IMG_GOKU_TIRO]
IMG_VEGETA = [IMG_VEGETA_PARADO, IMG_VEGETA_ANDANDO, IMG_VEGETA_KI, IMG_VEGETA_ATIRANDO, IMG_VEGETA_TIRO]

IMG_P1 = pg.transform.scale(IMG_P1, (32, 96))
DX = 15
DY = 10

KI_UP = 2

PAREDE_ESQUERDA = 0
PAREDE_DIREITA = LARGURA
PAREDE_CIMA = 0
PAREDE_BAIXO = ALTURA
CHAO = ALTURA - 60
PULO = CHAO+80

Y_LIFE = PAREDE_BAIXO - (IMG_LIFE.get_width()+10)
X_LIFE = PAREDE_ESQUERDA + IMG_LIFE.get_width()/2

X_LIFE2 = PAREDE_DIREITA - (IMG_LIFE.get_width()+IMG_LIFE.get_width()/2)