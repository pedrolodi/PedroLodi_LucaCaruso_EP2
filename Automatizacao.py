from Functions import formata_pecas, posicoes_possiveis

def bot(jogo, n_jogadores, mesa, pecas):
    import random
    from Functions import posicoes_possiveis
    from Functions import adiciona_na_mesa
    from Functions import formata_pecas

    if n_jogadores == 2:
        if posicoes_possiveis(mesa, pecas[2]) != []:
            p_poss = posicoes_possiveis(mesa, pecas[2])
            jogada = random.choice(p_poss)
            adiciona_na_mesa(jogo['jogadores'][2][jogada],jogo['mesa'])
            del(jogo['jogadores'][2][jogada])
            print('JOGADA DO JOGADOR 2:')
            print('\033[1;36;40mMESA: {}\033[m'.format(jogo['mesa']))

        elif posicoes_possiveis(jogo['mesa'],jogo['jogadores'][2]) == []:
                peca = [9,9]
                while peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                    comprar_peca = input('Nenhuma peça possível, compre uma peça!(ENTER) ')
                    jogo['jogadores'][2].append(jogo['monte'][0])
                    peca = jogo['monte'][0]
                    print('\033[1;32;40mJOGADOR 1: {}\033[m'.format(formata_pecas(jogo['jogadores'][2])))
                    del(jogo['monte'][0])
                    if peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                        break
                    else:
                        print('A peça comprada não cabe na mesa! Compre outra')

    elif n_jogadores == 3:
        for jogador in range(2,4):
            p_poss = posicoes_possiveis(mesa, pecas[jogador])
            if posicoes_possiveis(mesa, pecas[jogador]) != []:
                jogada = random.choice(p_poss)
                adiciona_na_mesa(jogo['jogadores'][jogador][jogada],jogo['mesa'])
                del(jogo['jogadores'][jogador][jogada])
                print('JOGADA DO JOGADOR {}: '.format(jogador))
                print('\033[1;36;40mMESA: {}\033[m'.format(jogo['mesa']))
                
            elif posicoes_possiveis(jogo['mesa'],jogo['jogadores'][jogador]) == []:
                peca = [9,9]
                while peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                    comprar_peca = input('Nenhuma peça possível, compre uma peça!(ENTER) ')
                    jogo['jogadores'][jogador].append(jogo['monte'][0])
                    peca = jogo['monte'][0]
                    print('\033[1;32;40mJOGADOR 1: {}\033[m'.format(formata_pecas(jogo['jogadores'][jogador])))
                    del(jogo['monte'][0])
                    if peca[0] != jogo['mesa'][0][0] or peca[0] != jogo['mesa'][-1][-1] or peca[1] != jogo['mesa'][0][0] or peca[1] != jogo['mesa'][-1][-1]:
                        break
                    else:
                        print('A peça comprada não cabe na mesa! Compre outra')

    elif n_jogadores == 4:
        for jogador in range(2,5):
            p_poss = posicoes_possiveis(mesa, pecas[jogador])
            if posicoes_possiveis(mesa, pecas[jogador]) != []:
                jogada = random.choice(p_poss)
                adiciona_na_mesa(jogo['jogadores'][jogador][jogada],jogo['mesa'])
                del(jogo['jogadores'][jogador][jogada])
                print('JOGADA DO JOGADOR {}: '.format(jogador))
                print('\033[1;36;40mMESA: {}\033[m'.format(jogo['mesa']))

            elif posicoes_possiveis(jogo['mesa'],jogo['jogadores'][jogador]) == []:
                print('Jogador {} sem Peças possíveis!'.format(jogador))


    


