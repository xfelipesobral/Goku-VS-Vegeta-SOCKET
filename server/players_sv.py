#!/usr/bin/env python
# -*- coding: utf-8 -*-

jogadores = list()

class Jogador:
    def __init__(self, id, ip, x, y, dx, dy, dmp, direct, hp, mp):
        self.id = id
        self.ip = ip
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.dmp = dmp
        self.direct = direct
        self.hp = hp
        self.mp = mp

    def inserir(self):
        jogadores.append(self)

    def remover(self):
        jogadores.remove(self)
