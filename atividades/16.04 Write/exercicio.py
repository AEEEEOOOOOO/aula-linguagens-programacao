# with open('hoje.txt', 'w') as arquivo: # -----> Cria o arquivo e escreve onde o curso está
#     arquivo.write('Luisa Braga\n')
#     arquivo.write('Turma NAI03')

# with open('hoje.txt', 'a') as arquivo: # ----------> Abre o arquivo de novo, move o cursor para o final e escreve no fim
#     arquivo.write('Caio Silva\n')

from datetime import datetime

def cabecalho(arquivo):
    nome = input('Digite o nome completo: ')
    formato_nome = 'NOME COMPLETO: ' + nome.upper()
    data = datetime.now().strftime('%d/%m/%Y')
    data_string = str(data)
    formato_data = 'DATA: ' + data_string + ' MANAUS - AM'
    arquivo.write(formato_nome + '\n')
    arquivo.write(formato_data + '\n')

with open('cabecalho.txt', 'a') as arquivo:
    cabecalho(arquivo)

    disciplina = input('Digite a disciplina: ').upper()
    nota = input('Digite a nota: ')

    while disciplina != 'sair' and nota != 'sair':
        arquivo.write(disciplina + ',' + nota + '\n')
        disciplina = input('Digite a disciplina: \n').upper()
        print('Digite sair para encerrar o programa.')
        nota = input('Digite a nota: ')
