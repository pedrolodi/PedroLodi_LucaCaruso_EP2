#IMPORTANDO FUNÇÕES E BIBLIOTECAS
from random import *
from Functions import *

# Criando pecas
pecas = cria_pecas()

#COMEÇANDO JOGO
n_jogadores = int(input('Quantos jogadores? '))
jogo_invalido = True
while jogo_invalido == True:
    if n_jogadores < 2 or n_jogadores > 4:
        print('Número inválido, tente novamente')
        n_jogadores = int(input('Quantos jogadores? '))
    else:
        jogo_invalido = False

inicio_jogo = inicia_jogo(n_jogadores, pecas)


