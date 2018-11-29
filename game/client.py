import socket
#from game.players import *

def enviar(udp, data, destino):
    udp.sendto(data.encode(), destino)


HOST = 'localhost' 
PORT = 5000     

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

enviar(udp, "CONECTEI$jogo", dest)