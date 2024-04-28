from datetime import datetime

busca = input('Digite um nome: ') # Obtendo a entrada do usuário e guardando-a

# Importando o arquivo excel
with open('dados.csv', 'r') as arquivo:
    next(arquivo)
    lista_linhas = arquivo.readlines()
    
    # Percorrendo toda a lista
    for linha in lista_linhas:
        nome, data_nascimento, matricula  = linha.strip('\n').split(',')

        # Separando nome e sobrenome do números
        nome_total = nome.split(' ') # <-- Separando as palavras que possuem espaço 
        nome_completo = nome_total[0] + ' ' + nome_total[1] # Palavras já separadas, agora é mostrado apenas primeira e segunda palavra
        numero = nome_total[2] # Caso queira ver a terceira palavra (número), basta chamar a variável número 
        
        # Condição: Mostrando apenas o nome específico
        if (nome_completo == busca): # Se nome de entrada for igual a nome pertecente no arquivo, então
            data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y') # Convertendo a data de nasc. presente no arquivo para outro padrão
            data_atual = datetime.now() # Declarando a data atual
            idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day)) 
            print(nome_completo, '>', idade)