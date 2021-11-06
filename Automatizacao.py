from Functions import posicoes_possiveis

def bot(jogo, n_jogadores, mesa, pecas):
    import random
    from Functions import posicoes_possiveis
    from Functions import adiciona_na_mesa

    if n_jogadores == 2:
        if posicoes_possiveis(mesa, pecas[2]) != []:
            p_poss = posicoes_possiveis(mesa, pecas[2])
            jogada = random.choice(p_poss)
            adiciona_na_mesa(jogo['jogadores'][2][jogada],jogo['mesa'])
            del(jogo['jogadores'][2][jogada])
            print('JOGADA DO JOGADOR 2:')
            print('\033[1;36;40mMESA: {}\033[m'.format(jogo['mesa']))
        else:
            while posicoes_possiveis(mesa, pecas[2]) == []:
                jogo['jogadores'][2].append(jogo['monte'][0])
                del(jogo['monte'][0])

    elif n_jogadores == 3:
        for jogador in range(2,3):
            p_poss = posicoes_possiveis(mesa, pecas[jogador])
            if posicoes_possiveis(mesa, pecas[jogador]) != []:
                jogada = random.choice(p_poss)
                adiciona_na_mesa(jogo['jogadores'][jogador][jogada],jogo['mesa'])
                del(jogo['jogadores'][jogador][jogada])
                print('JOGADA DO JOGADOR {}: '.format(jogador))
                print('\033[1;36;40mMESA: {}\033[m'.format(jogo['mesa']))
            else:
                while posicoes_possiveis(mesa, pecas[jogador]) == []:
                    jogo['jogadores'][jogador].append(jogo['monte'][0])
                    del(jogo['monte'][0])

    elif n_jogadores == 4:
        for jogador in range(2,4):
            p_poss = posicoes_possiveis(mesa, pecas[jogador])
            if posicoes_possiveis(mesa, pecas[jogador]) != []:
                jogada = random.choice(p_poss)
                adiciona_na_mesa(jogo['jogadores'][jogador][jogada],jogo['mesa'])
                del(jogo['jogadores'][jogador][jogada])
                print('JOGADA DO JOGADOR {}: '.format(jogador))
                print('\033[1;36;40mMESA: {}\033[m'.format(jogo['mesa']))
            else:
                while posicoes_possiveis(mesa, pecas[jogador]) == []:
                    jogo['jogadores'][jogador].append(jogo['monte'][0])
                    del(jogo['monte'][0])


    


