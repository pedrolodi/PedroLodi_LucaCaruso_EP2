from Functions import posicoes_possiveis


def bot(jogo, n_jogador):
    if len(posicoes_possiveis(jogo[mesa], jogo[jogadores][n_jogador])) > 0:
        jogo[mesa].append(jogo[jogadores][n_jogador][0])
    return jogo[mesa]


    


