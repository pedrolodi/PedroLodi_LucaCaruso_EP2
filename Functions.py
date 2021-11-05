#Imports
import random

# Criando pecas:
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

#Iniciando Jogo de Dominó
def inicia_jogo(n_jogadores,pecas):
    #Criação de um dicionário com as listas de peças
    jog_mes_mon = {
        'jogadores':{},
        'monte':[], 
        'mesa':[]
    }

    #Criação de listas com as peças dos jogadores
    P1 = []
    P2 = []
    P3 = []
    P4 = []

    #Peças embaralhadas
    random.shuffle(pecas)

    i=0
    #Partida com 2 jogadores
    if n_jogadores == 2:
        while i<7:
            add_P1 = P1.append(pecas[0])
            del(pecas[0])
            add_P2= P2.append(pecas[0])
            del(pecas[0])
            i = i+1
        jog_mes_mon['jogadores'][1] = P1
        jog_mes_mon['jogadores'][2] = P2

    #Partida com 3 jogadores
    if n_jogadores == 3:
        while i<7:
            add_P1 = P1.append(pecas[0])
            del(pecas[0])
            add_P2= P2.append(pecas[0])
            del(pecas[0])
            add_P3= P3.append(pecas[i])
            del(pecas[0])
            i = i+1
        jog_mes_mon['jogadores'][1] = P1
        jog_mes_mon['jogadores'][2] = P2
        jog_mes_mon['jogadores'][3] = P3

    #Partida com 4 jogadores
    if n_jogadores == 4:
        while i<7:
            add_P1 = P1.append(pecas[0])
            del(pecas[0])
            add_P2= P2.append(pecas[0])
            del(pecas[0])
            add_P3= P3.append(pecas[0])
            del(pecas[0])
            add_P4= P4.append(pecas[0])
            del(pecas[0])
            i = i+1
        jog_mes_mon['jogadores'][1] = P1
        jog_mes_mon['jogadores'][2] = P2
        jog_mes_mon['jogadores'][3] = P3
        jog_mes_mon['jogadores'][4] = P4
        
    #Colocando as peças excedentes no monte
    jog_mes_mon['monte'] = pecas

    #Printando Mesa e Jogador com formatação
    pecas_jogador = jog_mes_mon['jogadores'][1]
    print('\033[1;32;40mJOGADOR 1:\033[m \033[0;32;40m{}\033[m'.format(pecas_jogador))
    print("")
    print('\033[1;36;40mMESA:\033 \033[0;36;40m{}\033[m'.format(jog_mes_mon['mesa']))

    return jog_mes_mon

#Adicionando Peças
def adiciona_na_mesa(peca,mesa):
    aux = []
    if mesa == []:
       mesa.append(peca)
    else:
        final = mesa [-1][-1]
        comeco = mesa [0][0]
        if comeco in peca:
            if comeco == peca[0]:
                aux.append(peca[::-1])
                mesa= aux + mesa
            elif comeco == peca[-1]:
                aux.append(peca)
                mesa = aux + mesa
        elif final in peca:
            if peca[0] == final:
                mesa.append(peca)
            elif peca[-1] == final: 
                mesa.append(peca[::-1])
        elif peca[0] == peca[1] and comeco in peca:
            mesa.append(peca)

        aux = []
        return mesa

#Soma peças
def soma_pecas(lista):
    soma = 0
    for peca in lista:
        soma = soma + peca[0]
        soma = soma + peca[1]
    return soma
