from datetime import datetime

busca = input('Digite um nome: ') # Obtendo a entrada do usuário e guardando-a
busca_nome, busca_sobrenome = busca.split(' ') # Separando a entrada por elementos, definidos por espaço
busca_nome = busca_nome.lower() # Convertendo a entrada para letra minuscula 
busca_sobrenome = busca_sobrenome.lower # Convertendo a entrada para letra minuscula 

# Importando o arquivo excel
with open('dados.csv', 'r') as arquivo:
    next(arquivo)
    lista_linhas = arquivo.readlines()

    
    # Percorrendo toda a lista
    for linha in lista_linhas:
        nome_chamada, data_nascimento, matricula  = linha.strip('\n').split(',') # Separando e guardando os dados após a virgula (split) nas variáveis 

        
        # Separando nome, sobrenome e numero 
        nome, sobrenome, numero = nome_chamada.split(' ')
        
        # Condição: Mostrando apenas o nome específico
        if (nome.lower() == busca_nome and sobrenome.lower() == busca_sobrenome):
            data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
            hoje = datetime.now()
            idade = hoje.year - data_nascimento.year
            print('NOME: ', nome_chamada, 'IDADE: ', idade)