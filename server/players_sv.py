#!/usr/bin/env python
# -*- coding: utf-8 -*-

jogadores = list()

class Jogador:
    def __init__(self, id, ip, x, y, hp):
        self.id = id
        self.ip = ip
        self.x = x
        self.y = y
        self.hp = hp

    def inserir(self):
        jogadores.append(self)

    def remover(self):
        jogadores.remove(self)
