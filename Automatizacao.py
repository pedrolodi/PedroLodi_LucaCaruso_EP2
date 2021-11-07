from Functions import formata_pecas, posicoes_possiveis

def bot(jogo, n_jogadores, mesa, pecas):
    import random
    from Functions import posicoes_possiveis
    from Functions import adiciona_na_mesa
    from Functions import formata_pecas

############################################################# 2 JOGADORES ##########################################################
    if n_jogadores == 2:
        p_poss = posicoes_possiveis(mesa, pecas[2])
        if posicoes_possiveis(mesa, pecas[2]) != []:
            p_poss = posicoes_possiveis(mesa, pecas[2])
            jogada = random.choice(p_poss)
            adiciona_na_mesa(jogo['jogadores'][2][jogada],jogo['mesa'])
            del(jogo['jogadores'][2][jogada])
            print('JOGADA DO JOGADOR 2:')
            print('\033[1;36;40mMESA: {}\033[m'.format(formata_pecas(jogo['mesa'])))

        if posicoes_possiveis(jogo['mesa'],jogo['jogadores'][2]) == [] and jogo['jogadores'][2] != []:
                peca = [9,9]
                if len(jogo['monte'])>0:
                    while peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                        jogo['jogadores'][2].append(jogo['monte'][0])
                        peca = jogo['monte'][0]
                        del(jogo['monte'][0])
                        if peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                            jogo['mesa'].append(peca)
                            break
                        else:
                            print('A peça comprada não cabe na mesa! Compre outra')
                else:
                    print('JOGADA DO JOGADOR 2:')
                    print('Sem peças no monte... Pulando a vez!')

############################################################# 3 JOGADORES ##########################################################
    elif n_jogadores == 3:
        for jogador in range(2,4):
            p_poss = posicoes_possiveis(mesa, pecas[jogador])
            if posicoes_possiveis(mesa, pecas[jogador]) != []:
                jogada = random.choice(p_poss)
                adiciona_na_mesa(jogo['jogadores'][jogador][jogada],jogo['mesa'])
                del(jogo['jogadores'][jogador][jogada])
                print('JOGADA DO JOGADOR {}: '.format(jogador))
                print('\033[1;36;40mMESA: {}\033[m'.format(formata_pecas(jogo['mesa'])))
                print("")
                
            elif posicoes_possiveis(jogo['mesa'],jogo['jogadores'][jogador]) == []:
                peca = [9,9]
                if len(jogo['monte'])>0:
                    while peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                        jogo['jogadores'][jogador].append(jogo['monte'][0])
                        peca = jogo['monte'][0]
                        del(jogo['monte'][0])
                        if peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                            break
                        else:
                            print('A peça comprada não cabe na mesa! Compre outra')
                else:
                    print('Sem peças no monte... Pulando a vez!')
                    
############################################################# 4 JOGADORES ##########################################################
    elif n_jogadores == 4:
        for jogador in range(2,5):
            p_poss = posicoes_possiveis(mesa, pecas[jogador])
            if posicoes_possiveis(mesa, pecas[jogador]) != []:
                jogada = random.choice(p_poss)
                adiciona_na_mesa(jogo['jogadores'][jogador][jogada],jogo['mesa'])
                del(jogo['jogadores'][jogador][jogada])
                print('JOGADA DO JOGADOR {}: '.format(jogador))
                print('\033[1;36;40mMESA: {}\033[m'.format(formata_pecas(jogo['mesa'])))
                print('')

            if (posicoes_possiveis(jogo['mesa'],jogo['jogadores'][jogador]) == []) and (jogo['jogadores'][1] != [] or jogo['jogadores'][2] != [] or jogo['jogadores'][3] != [] or jogo['jogadores'][4] != []):
                    print('JOGADA DO JOGADOR {}: '.format(jogador))
                    print('Sem peças possíveis... Pulando a vez!')
                    print('')
                    


    


