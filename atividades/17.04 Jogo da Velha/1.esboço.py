def tabuleiro(arquivo):
    jogada1 = ' X |O| X'
    linha2 = '-----------'
    jogada2 = ' X |O| O'
    linha4 = '-----------'
    jogada3 = ' X |O| X'
    arquivo.write(jogada1 + '\n')
    arquivo.write(linha2 + '\n')
    arquivo.write(jogada2 + '\n')
    arquivo.write(linha4 + '\n')
    arquivo.write(jogada3)

with open('jogo_da_velha.txt', 'w') as arquivo:
    tabuleiro(arquivo)

    print(tabuleiro)


    # while disciplina != 'sair' and nota != 'sair':
    #     arquivo.write(disciplina + ',' + nota + '\n')
    #     disciplina = input('Digite a disciplina: \n').upper()
    #     print('Digite sair para encerrar o programa.')
    #     nota = input('Digite a nota: ')