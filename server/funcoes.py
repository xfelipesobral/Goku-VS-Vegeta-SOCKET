import socket

def enviar(udp, data, destino):
        if type(destino) is list:
                for ip in destino:
                        udp.sendto(data.encode(), ip)
        else:
                udp.sendto(data.encode(), destino)

def iptoint(ip):
        return(ip.replace('.',''))

'''
        @ id_1#ip_127.0.0.1_455#x_0#y_0#hp_100
        split('#')

        data[0] -> id_1 @ split('_') @ data[0] -> id / data[1] -> 1
        data[1] -> ip_127.0.0.1_455
        data[2] -> x_0
        data[3] -> y_0
        data[4] -> hp_100
'''
def stringNewPlayer(player):
        data = "id_"+str(player.id)+"#ip_"+str(player.ip[0])+"_"+str(player.ip[1])+"#x_"+str(player.x)+"#y_"+str(player.y)+"#hp_"+str(player.hp)        
        return data

























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