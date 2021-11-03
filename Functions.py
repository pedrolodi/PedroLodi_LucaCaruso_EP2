# Criando pecas:
import random
def cria_pecas():
    pecas = []
    for i in range(0, 7):
        for j in range(0, 7):
            if [i, j] not in pecas and [j, i] not in pecas:
                pecas.append([i, j])
    random.shuffle(pecas)
    return pecas

# Quem ganhou:
def verifica_ganhador(jogadores):
    for jogador in jogadores:
        if jogadores[jogador] == []:
            return jogador

    return -1

# Possiveis posicoes
def posicoes_possiveis(mesa, pecas):
    posicoes = []
    for peca in pecas:
        if mesa == []:
            posicoes.append(pecas.index(peca))
        elif len(mesa) > 0:
            if peca[0] == mesa[0][0] or peca[1] == mesa[0][0]:
                posicoes.append(pecas.index(peca))
            elif peca[0] == mesa[len(mesa)-1][1] or peca[1] == mesa[len(mesa)-1][1]:
                posicoes.append(pecas.index(peca))
    return posicoes 
            
