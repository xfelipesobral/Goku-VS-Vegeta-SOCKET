import socket

def enviar(udp, data, destino):
        udp.sendto(data.encode(), destino)

def iptoint(ip):
        return(ip.replace('.',''))
























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