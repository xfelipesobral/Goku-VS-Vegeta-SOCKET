import socket
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5009            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use Q\n')
msg = input()
while (msg != 'Q'):
    tcp.send (msg)
    msg = input()
tcp.close()
