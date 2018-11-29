#!/usr/bin/python

import pygame as pg
import sys, os
import _thread
from game.client import *
from game.players import *

COR_BRANCO = (255, 255, 255)

#_thread.start_new_thread(initClient, ())

def big_bang(inic, tela,
             quando_tick=lambda e: e, \
             frequencia=30, \
             desenhar=lambda e: pg.Surface((0,0)), \
             quando_tecla=lambda e, k: e, \
             quando_solta_tecla=lambda e, k: e, \
             quando_mouse=lambda e, x, y, ev: e, \
             parar_quando=lambda e: False):

    def desenha_tela():
        tela.fill(COR_BRANCO)
        desenhar(estado)


    '''
    ############# CONTINUAR DAQUI ###################
    '''

    def updateSocket(udp, estado):
        data = udp.recv(1024)

        data = data.decode()
        data = data.split('$')
        chave = data[0]

        if(chave == "CONECTEI"):
            if(data[1] != "conectou"):
                udp.close()
            else:
                print("CONECTADO")

            if(chave == "NEW_PLAYER"):
                initMain(data[1], estado)

            if(chave == "BROADCAST_PLAYER"):
                atualizarJogador(data[1], estado)

    pg.init()
    estado = inic
    clock = pg.time.Clock()

    while True:
        _thread.start_new_thread(updateSocket, (udp, estado))
        pg.display.flip()

        if parar_quando(estado):
            print(estado)
            sys.exit(0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(estado)
                sys.exit(0)

            if event.type == pg.KEYDOWN:
                estado = quando_tecla(estado, event.key)
                desenha_tela()
            elif event.type == pg.KEYUP:
                estado = quando_solta_tecla(estado, event.key)

            elif event.type in [pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEMOTION]:
                x, y = pg.mouse.get_pos()
                estado = quando_mouse(estado, x, y, event.type)
                desenha_tela()

        estado = quando_tick(estado)

        desenha_tela()

        clock.tick(frequencia)