tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]
for linha in range(0, 3): 
    for coluna in range(0,3): 
        tabuleiro[linha][coluna] = int(input('Digite um valor: '))
        
print(tabuleiro)