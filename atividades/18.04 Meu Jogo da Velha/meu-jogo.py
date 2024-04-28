import quem_ganhou
import os
def limpa():
    os.system('cls')

tabuleiro = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def montar_tabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(' ' + tabuleiro[i][0] + ' | ' + tabuleiro[i][1] + ' | ' + tabuleiro[i][2])
        if i < 2:
            print('-----------')

def atualizar_tabuleiro(tabuleiro):
    with open ('tabuleiro.txt', 'w') as arquivo:
        for i, linha in enumerate(tabuleiro):
            arquivo.write(' {} | {} | {} \n'.format(linha[0], linha[1], linha[2]))
            if i < 2:
                arquivo.write('-----------\n')

def jogar():
    jogador = 'X'
    while quem_ganhou.verificar_vencedor(tabuleiro) == 'O jogo ainda não acabou!':
        montar_tabuleiro(tabuleiro)
        linha, coluna = map(int, input(f'\nÉ a vez do jogador {jogador}. Em qual posição você deseja jogar? \n -> ').split())
        limpa()

        while tabuleiro[linha][coluna] != ' ':
            print('Posição já ocupada. Tente novamente!')
            montar_tabuleiro(tabuleiro)
            linha, coluna = map(int, input(f'\nÉ a vez do jogador {jogador}. Em qual posição você deseja jogar? \n -> ').split())
            limpa()

        tabuleiro[linha][coluna] = jogador
        atualizar_tabuleiro(tabuleiro)

        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'

    montar_tabuleiro(tabuleiro)
    print(f'\nParabéns, jogador {quem_ganhou.verificar_vencedor(tabuleiro)}, você venceu! :D')

def menu():
    opcao = ''
    while opcao != '0':
        print('------------------------------------------------')
        print('|              Seja bem vindo!                 |')
        print('------------------------------------------------')
        print('| [1] - Iniciar jogo                           |')
        print('| [0] - Encerrar programa                      |')
        print('------------------------------------------------')
        opcao = input('Escolha uma opção do painel (digite apenas números): ')
        limpa()
        if opcao == '1':
            jogar()
            break

menu()
