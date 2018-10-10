#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *

class Jogador:
    def __init__(self):
        self.sprite = None
        self.PAREDE_DIREITA = LARGURA - self.sprite.get_width()/2
        self.PAREDE_ESQUERDA = 0 + self.sprite.get_width()/2
        self.x = 0
        self.y = ALTURA - self.sprite.get_width()/2
        self.dx = 10
        self.vida = 100
        
    
    def set_posicao(self, x):
        self.x = x

    def set_velocidade(self, dx):
        self.dx = dx

    def mover(self):
        if self.x < 0 or self.x > LARGURA:
            return "PLAYER INVÁLIDO"
        else:
            self.x = self.x + self.dx

            if self.x > self.PAREDE_DIREITA:
                self.x = self.PAREDE_DIREITA
            elif self.x < self.PAREDE_ESQUERDA:
                self.x = self.PAREDE_ESQUERDA


            
