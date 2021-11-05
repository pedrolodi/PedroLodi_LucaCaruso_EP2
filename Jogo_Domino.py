#IMPORTANDO FUNÇÕES E BIBLIOTECAS
from random import *
from Functions import *

################################## JOGO ################################## 
jogar = input('\033[1;33;40mGOSTARIA DE JOGAR DOMINÓ (S/N)? \033[m')
if (jogar == 's') or (jogar == 'S'):

    #REGRAS
    print("")
    print("\033[1;33;41mREGRAS:\033[m")
    print('\033[0;33;40m1) Na vez de um jogador, esse deve observar as peças posicionadas nas pontas da montagem sobre a mesa e seus valores;\033m')
    print('2) O jogador deve escolher uma peça de sua posse que tenha um dos números de alguma das pontas das peças da mesa;')
    print('3) Se tiver uma peça possível, então, o jogador deve colocar a peça na mesa e está encerrada sua jogada nessa rodada;')
    print('4) Caso o jogador não tenha peças possíveis para a mesa, então, se houver monte, deve pegar uma do monte.')
    print('5) O passo 44 deve ser repetido até que o jogador tenha uma peça que cumpra o passo 22.')
    print('6) Caso o jogador não tenha peça possível e também esgotado o monte, então, esse deve passar sua vez para o próximo jogador.')
    print("")
    print("\033[1;33;41mQUEM GANHA?\033[m")
    print('\033[0;33;40m1) O jogador vitorioso é aquele que conseguir colocar todas suas peças na mesa, respeitando as regras dos valores das pontas, antes dos demais jogadores;\033m')
    print('\033[0;33;40m2) Existe a possibilidade de nenhum jogador colocar peças em toda uma rodada, isso porque o jogo pode estar fechado e sem monte. Nesse caso, o jogo está encerrado;\033m')
    print('\033[0;33;40mPara efeito de vitória, os participantes devem contar os valores das faces das peças em sua posse;\033m')
    print('\033[0;33;40mGanha o jogador que tiver a menor contagem de pontos, sendo possível empate.\033m')
    print("")

    # CRIANDO PEÇAS
    pecas = cria_pecas()

    #COMEÇANDO JOGO
    n_jogadores = int(input('\033[1;33;40mQUANTOS JOGADORES(2-4)? \033[m'))
    jogo_invalido = True
    while jogo_invalido == True:
        if n_jogadores < 2 or n_jogadores > 4:
            print('\033[1;31;40mNúmero inválido, tente novamente!\033[m')
            print('')
            n_jogadores = int(input('\033[1;33;40mQUANTOS JOGADORES(2-4)? \033[m'))
        else:
            jogo_invalido = False

    jogo = inicia_jogo(n_jogadores, pecas)
    jogador_da_vez = randint(0, (n_jogadores -1))
    
    ganhador = 0
    continuar = 1
    while continuar == 1:
        for jogador in jogo['jogadores']:
            if jogador == []:
                ganhador = jogador
                continuar = 0
        if posicoes_possiveis != []:
            print('')
            print('JOGADOR 1:{}'.format(jogo['jogadores'][1]))
            print('POSIÇÕES POSSÍVEIS: {}'.format(posicoes_possiveis(jogo['mesa'],jogo['jogadores'][1])))
            jogada = int(input('QUAL PEÇA VOCÊ QUER JOGAR? '))
            print('MESA: {}'.format(jogo['mesa']))
            print('')
            adiciona_na_mesa(jogo['jogadores'][1][jogada],jogo['mesa'])
            del(jogo['jogadores'][1][jogada])
            print(jogo['jogadores'][1])
            print('')
            print('MESA: {}'.format(jogo['mesa']))
        else:
            jogo['jogadores'][1].append(jogo['monte'][0])
            del(jogo['monte'][0])

        
        
            



