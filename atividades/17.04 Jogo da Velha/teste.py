tabuleiro = []
resultado = ''
with open('tabuleiro.txt', 'r') as arquivo:
        linhas_arquivo = arquivo.readlines()
        tabuleiro = [linhas_arquivo[0].strip('\n').split('|'),
        linhas_arquivo[2].strip('\n').split('|'), 
        linhas_arquivo[4].strip('\n').split('|')]

print(tabuleiro)

for linha in tabuleiro:
    if linha[0] == linha[1] == linha[2]:
        print(linha[0])

for coluna in [0,1,2]:
    if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna]:
        print(tabuleiro[0][coluna])

        




