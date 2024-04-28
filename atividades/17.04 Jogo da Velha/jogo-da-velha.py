tabuleiro = []
resultado = ''

with open('tabuleiro.txt', 'r') as arquivo:

    linhas_arquivo = arquivo.readlines()
    tabuleiro = [linhas_arquivo[0].strip('\n').split('|'), 
                 linhas_arquivo[2].strip('\n').split('|'), 
                 linhas_arquivo[4].strip('\n').split('|')]

    # for linha in tabuleiro:
    #     for coluna in linha:
    #         print(coluna, '\t')

    for linha in tabuleiro:
        for jogada in linha:
            if jogada == ' ':
                resultado = 'O jogo ainda não acabou!!'

    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            resultado = linha[0]

    for coluna in range(0,3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[2][coluna] != ' ':
            resultado = tabuleiro[0][coluna]

    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2]) and tabuleiro[1][1] != ' ':
        resultado = tabuleiro[1][1]

    if resultado == '':
        resultado = 'Velhou'

    print(resultado)
