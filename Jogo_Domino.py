#IMPORTANDO FUNÇÕES E BIBLIOTECAS
from math import fabs
from random import *
from Functions import *
from Automatizacao import *

################################## JOGO ################################## 
jogar = input('\033[1;33;40mGOSTARIA DE JOGAR DOMINÓ (S/N)? \033[m')

while jogar == 's' or jogar == 'S':
    if (jogar == 's') or (jogar == 'S'):

        #REGRAS
        print("")
        print("\033[1;33;41mREGRAS:\033[m")
        print('\033[0;33;40m1) Na vez de um jogador, esse deve observar as peças posicionadas nas pontas da montagem sobre a mesa e seus valores;\033m')
        print('2) O jogador deve escolher uma peça de sua posse que tenha um dos números de alguma das pontas das peças da mesa;')
        print('3) Se tiver uma peça possível, então, o jogador deve colocar a peça na mesa e está encerrada sua jogada nessa rodada;')
        print('4) Caso o jogador não tenha peças possíveis para a mesa, então, se houver monte, deve pegar uma do monte.')
        print('5) O passo 4 deve ser repetido até que o jogador tenha uma peça que cumpra o passo 2.')
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

        #QUANTOS JOGADORES?
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
        
        #JOGO
        #LOOP ATÉ VITÓRIA OU EMPATE
        continuar = True
        while continuar == True:   
            if posicoes_possiveis(jogo['mesa'],jogo['jogadores'][1]) != []:
                print('')
                print('\033[1;32;40mJOGADOR 1: {}\033[m'.format(formata_pecas(jogo['jogadores'][1])))
                print('\033[0;33;40mPOSIÇÕES POSSÍVEIS: {}\033[m'.format(posicoes_possiveis(jogo['mesa'],jogo['jogadores'][1])))
                print('')
                print('\033[1;36;40mMESA: {}\033[m'.format(formata_pecas(jogo['mesa'])))
                jogada = int(input('\033[1;33;40mQUAL PEÇA VOCÊ QUER JOGAR? \033[m'))

                if jogada in posicoes_possiveis(jogo['mesa'],jogo['jogadores'][1]):
                    adiciona_na_mesa(jogo['jogadores'][1][jogada],jogo['mesa'])
                    del(jogo['jogadores'][1][jogada])
                    print('JOGADA JOGADOR 1:')
                    print('\033[1;36;40mMESA: {}\033[m'.format(formata_pecas(jogo['mesa'])))
                    print('')
                    bot(jogo, n_jogadores, jogo['mesa'], jogo['jogadores'])
                    print('================================================================================')

                else:
                    while jogada  not in posicoes_possiveis(jogo['mesa'],jogo['jogadores'][1]):
                        print('POSIÇÃO INVÁLIDA! TENTE NOVAMENTE')
                        jogada = int(input('\033[1;33;40mQUAL PEÇA VOCÊ QUER JOGAR? \033[m'))
                    
                    adiciona_na_mesa(jogo['jogadores'][1][jogada],jogo['mesa'])
                    del(jogo['jogadores'][1][jogada])
                    print('\033[1;32;40mJOGADA DO JOGADOR 1:\033[m')
                    print('\033[1;36;40mMESA: {}\033[m'.format(formata_pecas(jogo['mesa'])))
                    print('')
                    if jogo['jogadores'][1] != [] and jogo['jogadores'][2] != [] and jogo['jogadores'][n_jogadores-1] != [] and jogo['jogadores'][n_jogadores] != []:
                        bot(jogo, n_jogadores, jogo['mesa'], jogo['jogadores'])
                        print('================================================================================')
                    else:
                        ganhador = 1
                        continuar = False

            if posicoes_possiveis(jogo['mesa'],jogo['jogadores'][1]) == [] and len(jogo['monte']) == 0 and posicoes_possiveis(jogo['mesa'],jogo['jogadores'][2]) != [] or posicoes_possiveis(jogo['mesa'],jogo['jogadores'][n_jogadores - 1]) != [] or posicoes_possiveis(jogo['mesa'],jogo['jogadores'][n_jogadores]) != []:
                
                print('JOGADA JOGADOR 1:')
                print('Sem peças possíveis... Pulando a vez!')
                print('')
                bot(jogo, n_jogadores, jogo['mesa'], jogo['jogadores'])
                print('================================================================================')

                    
            if (jogo['jogadores'][1] == []) or (jogo['jogadores'][2] == []) or (jogo['jogadores'][n_jogadores-1] == []) or (jogo['jogadores'][n_jogadores] == []):
                for jogador in jogo['jogadores']:
                    for pecas in jogo['jogadores'][jogador]:
                        if pecas == []:
                            ganhador = jogador
                            continuar = False
                       
            if ((posicoes_possiveis(jogo['mesa'],jogo['jogadores'][1]) == [])) and jogo['jogadores'][1] != []:
                #COMPRANDO PEÇAS DO MONTE
                peca = [9,9]
                if len(jogo['monte'])>0:
                    while peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                        if jogo['jogadores'][1] != []:  
                            print('\033[1;32;40mJOGADOR 1: {}\033[m'.format(formata_pecas(jogo['jogadores'][1])))
                            comprar_peca = input('Nenhuma peça possível, compre uma peça!(ENTER) ')
                            jogo['jogadores'][1].append(jogo['monte'][0])
                            peca = jogo['monte'][0]
                            del(jogo['monte'][0])
                        if jogo['jogadores'][1] == []:
                            ganhador = 1
                            continuar = False
                            

                        if peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                            break
                        else:
                            print('A peça comprada não cabe na mesa! Compre outra')
                if len(jogo['monte']) == 0 and n_jogadores != 4:
                    print('Sem peças no monte... Pulando a vez!')
                    a = 0
                
                
                      
        
            if posicoes_possiveis(jogo['mesa'],jogo['jogadores'][1]) == [] and posicoes_possiveis(jogo['mesa'],jogo['jogadores'][2]) == [] and posicoes_possiveis(jogo['mesa'],jogo['jogadores'][n_jogadores-1]) == [] and posicoes_possiveis(jogo['mesa'],jogo['jogadores'][n_jogadores]) == [] and jogo['jogadores'][1] != [] and jogo['jogadores'][2] != [] and jogo['jogadores'][n_jogadores-1] != [] and jogo['jogadores'][n_jogadores] != []:
                print('NENHUM JOGADOR TEM MOVIMENTOS POSSÍVEIS! CONTABILIZANDO PONTOS!')
                pontos_jogadores = {}
                pontos_jogadores[1] = soma_pecas(jogo['jogadores'][1])
                pontos_jogadores[2] = soma_pecas(jogo['jogadores'][2])
                pontos_jogadores[n_jogadores-1] = soma_pecas(jogo['jogadores'][n_jogadores-1])
                pontos_jogadores[n_jogadores] = soma_pecas(jogo['jogadores'][n_jogadores])
                menor = min(pontos_jogadores.values())
                for key, value in pontos_jogadores.items():
                    if menor == value:
                        ganhador = key
                break
                
            
            
        print('O JOGADOR {} GANHOU! FIM DE JOGO'.format(ganhador))
        print('OBRIGADO POR JOGAR!')
        print('')
        jogar = input('\033[1;33;40mGOSTARIA DE JOGAR DOMINÓ NOVAMENTE(S/N)? \033[m')