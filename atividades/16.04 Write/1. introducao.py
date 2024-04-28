# with open('hoje.txt', 'w') as arquivo: # -----> Cria o arquivo e escreve onde o curso está
#     arquivo.write('Luisa Braga\n')
#     arquivo.write('Turma NAI03')

# with open('hoje.txt', 'a') as arquivo: # ----------> Abre o arquivo de novo, move o cursor para o final e escreve no fim
#     arquivo.write('Caio Silva\n')


with open('alunos.txt', 'a') as arquivo: 
    nome_aluno = input('Digite o nome do aluno: ')
    while nome_aluno != 'sair':
        texto = nome_aluno + '\n'
        arquivo.write(texto)
        nome_aluno
