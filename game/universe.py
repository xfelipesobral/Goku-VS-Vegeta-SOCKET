#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.oocities.org/saiyangohan71486/sprites.html

import pygame as pg
import sys, os
import threading
from game.players import *

COR_BRANCO = (255, 255, 255)

estado = None

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

    global estado

    pg.init()
    estado = inic
    clock = pg.time.Clock()

    '''
    ## SOCKET ---
    '''

    def updateSocket(udp):
        global estado

        while True:
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

            if(chave == "KICK"):
                udp.close()
                sys.exit(0)
    '''
    ## SOCKET --/
    '''

    socketX = threading.Thread(target=updateSocket, args=(udp, ))

    socketX.start()

    while True:
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

        try:
            enviarJogador(estado.jogador)
            #if(estado.jogador.dx != 0 or estado.jogador.dy != 0):
            #    enviarJogador(estado.jogador)

            if(len(jogo.poderes) != 0):
                enviarPoder(estado.poderes)

               
        except:
            pass


        estado = quando_tick(estado)

        desenha_tela()

        clock.tick(frequencia)