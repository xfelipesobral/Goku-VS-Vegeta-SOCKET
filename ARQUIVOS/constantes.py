#!/usr/bin/env python
# -*- coding: utf-8 -*-

from universe import *
import random

'''
====================
 TELA E CONSTANTES
====================
'''

(LARGURA, ALTURA) = (800, 600)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_VACA = pg.image.load('img/vaca.png')
    ## PERSONAGENS

except:
    IMG_VACA = pg.Surface((100,100),pg.SRCALPHA)
    print("IMAGENS NÃO CARREGADAS!!!")

## CONSTANTES DE VACA ##
IMG_VACA = pg.transform.scale(IMG_VACA, (50, 50))
Y_VACA = 600 - IMG_VACA.get_width()/2
DX = 20 # VELOCIDADE VACA
DV = 30 # VELOCIDADE TIRO DA VACA
IMG_BALA_V = pg.transform.scale(IMG_BALA_V, (10,20))
IMG_MUNICAO = pg.transform.scale(IMG_MUNICAO, (25, 25))

## CONSTANTES PLAYER 1 ##
Y_P1 = 600 - IMG_P1.get_width()/2

## CONSTANTES PLAYER 2 ##
Y_P2 = img_p2.get

## CONSTANTES DE ZUMBI ##
DZ = 3 # VELOCIDADE ZUMBI
DZZ = 5 # VELOCIDADE TIRO ZUMBI
DESLOCAMENTO_ZUMBI = 80 # REPRESENTA O DESLOCAMENTO DO ZUMBI NA LINHA Y
IMG_ZUMBI = pg.transform.scale(IMG_ZUMBI, (50, 50))
IMG_ZUMBI_V = pg.transform.flip(IMG_ZUMBI, True, False)
IMG_BALA_Z = pg.transform.scale(IMG_BALA_Z,(10,20))

## CONSTANTES FENO ##
IMG_FENO = pg.transform.scale(IMG_FENO, (50,50))
IMG_FENO = pg.transform.rotate(IMG_FENO, 90)

## CONSTANTES GERAIS ##
PAREDE_ESQUERDA = 0 + IMG_VACA.get_width()/2
PAREDE_DIREITA = LARGURA - IMG_VACA.get_width()/2
PAREDE_CIMA = 0
PAREDE_BAIXO = ALTURA
