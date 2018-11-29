import json

class Jogador:
    def __init__(self, id, ip, x, y, hp):
        self.id = id
        self.ip = ip
        self.x = x
        self.y = y
        self.hp = hp

def criarJogador(data):
    data = json.loads(data)
    jogador = Jogador(data["id"], data["ip"], data["x"], data["y"], data["hp"])
    return jogador

def initMain(data, jogo):
    jogo.jogador = criarJogador(data)

def atualizarJogador(data, jogo):
    verif = True

    for jogador in jogo.jogadores:
        if(jogador.id == data["id"]):
            data = json.loads(data)
            jogador.x = data["x"]
            jogador.y = data["y"]
            jogador.hp = data["hp"]
            verif = False
        
    if(verif):
        jogo.jogadores.append(criarJogador(data))
    

'''
def testJSON():
    joao = Jogador(0, ["127.0.0.1", 5000], 0, 0, 1000)
    joaoJSON = json.dumps(joao.__dict__)

    novo = criarJogador(joaoJSON)

    print(novo.ip)
testJSON()
'''
