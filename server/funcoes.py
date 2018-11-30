#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json

def enviar(udp, data, destino):
	if type(destino) is list:
		for ip in destino:
			udp.sendto(data.encode(), ip)
	else:
		udp.sendto(data.encode(), destino)

def iptoint(ip):
	return(ip.replace('.',''))

def stringNewPlayer(player):
	data = json.dumps(player.__dict__)
	return data

def atualizarJogadores(udp, ipConectados, jogadores):
	for jogador in jogadores:
		data = "BROADCAST_PLAYER$"+stringNewPlayer(jogador)
		enviar(udp, data, ipConectados)
		

def atualizarJogador(udp, ipConectados, jogador):
	data = "BROADCAST_PLAYER$"+stringNewPlayer(jogador)
	enviar(udp, data, ipConectados)

def attJogador(udp, ip, jogador):
	data = "BROADCAST_PLAYER$"+jogador
	enviar(udp, data, ip)

def stringInitPlayer(udp, ip, player):
	data = "NEW_PLAYER$"+stringNewPlayer(player)
	enviar(udp, data, ip)

























'''
def verificar(mensagem, origem):
	val = mensagem.split('$')

	if(val[0]=='TESTECONEXAO'):
		return true
'''

'''
def verificar(msg, origin):
    x = msg[0]

    if(x=='TESTE_CONEXAO'):
	print("["+origin[0]+str(origin[1])+"] OK!")
'''