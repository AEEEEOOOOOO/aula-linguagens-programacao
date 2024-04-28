import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # --> Definindo a localização para o BR

def limpa(): # --> Função para limpar o console
    os.system("cls")

itens_carrinho = []
produtos = []
indice = ''
busca = ''
opcao = ''
adiciona_carrinho = ''  

def menu1():
    print('-----------------------------------------------------------------------')
    print('| [1] - Fazer uma nova busca                                          |')
    print('| [2] - Adicionar item no carrinho                                    |')
    print('| [0] - Finalizar compra                                              |')
    print('-----------------------------------------------------------------------')
    
def menu2():
    print('--------------------------------------------------------------')
    print('| [1] - Fazer nova busca                                     |')
    print('| [2] - Adicionar item ao carrinho                           |')
    print('| [3] - Visualizar itens do carrinho                         |')
    print('| [0] - Finalizar compra                                     |')
    print('--------------------------------------------------------------')

while opcao != '0':
    if itens_carrinho == []:
        menu1()
        opcao = input('Escolha uma opção do painel (digite apenas números): ')
    else:  
        menu2()
        opcao = input('Escolha uma opção do painel (digite apenas números): ')

    with open('produtos.csv', 'r', encoding='utf=8') as arquivo: # --> Leitura do arquivo 'produtos.csv' em modo de leitura ('r')
        next(arquivo)  # --> Pula a primeira linha do arquivo (cabeçalho)
        produtos = arquivo.readlines()  # --> Lê todas as linhas do arquivo e as armazena em uma lista       
        
        if (opcao == '1'):
            limpa()
            lista_busca = []
            busca = input('Por favor, digite o nome do produto OU o código do produto OU a categoria do produto que desejas visualizar \n -> ').upper()  # Entrada de busca do usuário já convertida para maiúscula
            print('-----------------------------------------------------------------------') # --> Cabeçalho que será exibido antes dos 5 produtos buscados
            print('|                           CAIORRINHO                                |') # --> Cabeçalho que será exibido antes dos 5 produtos buscados
            print('-----------------------------------------------------------------------') # --> Cabeçalho que será exibido antes dos 5 produtos buscados
            print(f'|   {"CODIGO".ljust(25)}{"NOME DO PRODUTO".ljust(24)}{"VALOR EM R$".rjust(16)} |') # --> Cabeçalho que será exibido antes dos 5 produtos buscados

            # ------------> FORMATAÇÃO DAS LINHAS <--------------
            for indice in produtos: # --> Percorre todas as linhas (indice) do arquivo lido (produto)
                nome_produto, categoria, preco, quantidade, codigo_produto = indice.upper().strip().split(';') # --> Divide as linhas em colunas e as converte para maiúsculas
                
                # ------------> PESQUISANDO E INCLUINDO PRODUTO NA LISTA   <--------------    
                if busca in nome_produto or busca == codigo_produto or busca == preco:  # --> Verifica se a chave de busca está presente no nome do produto, no código ou no preço
                    lista_busca.append(indice) # --> Se estiver presente, soma essas linhas (indice) à lista busca, criada como vazia lá em cima 

            # ------------> APÓS SOMADO A PESQUISA NA LISTA, EXIBE A LISTA <--------------     
            for indice in lista_busca[:5]: # --> Percorre as linhas (indice) da lista e mostra apenas as 5 primeiras
                nome_produto, categoria, preco, quantidade, codigo_produto = indice.upper().strip().split(';') # --> Divide as linhas em colunas e as converte para maiúsculas 
                preco_formatado = locale.currency(float(preco)) # Chama o local definido lá em cima e depois converte os valores de preço em FLOAT
                print(f'| {codigo_produto.ljust(20)}{nome_produto.ljust(36)}{preco_formatado.rjust(10)}  |')
            

        elif (opcao == '2'):
            limpa()
            print('-----------------------------------------------------------------------') # --> Cabeçalho que será exibido antes dos 5 produtos buscados
            print('|                           CAIORRINHO                                |') # --> Cabeçalho que será exibido antes dos 5 produtos buscados
            print('-----------------------------------------------------------------------') # --> Cabeçalho que será exibido antes dos 5 produtos buscados
            print(f'|   {"CODIGO".ljust(25)}{"NOME DO PRODUTO".ljust(25)}{"VALOR EM R$".rjust(16)}|') # --> Cabeçalho que será exibido antes dos 5 produtos buscados
            
            for indice in lista_busca[:5]:
                nome_produto, categoria, preco, quantidade, codigo_produto = indice.upper().strip().split(';') # --> Divide as linhas em colunas e as converte para maiúsculas 
                preco_formatado = locale.currency(float(preco)) # Chama o local definido lá em cima e depois converte os valores de preço em FLOAT
                print(f'| {codigo_produto.ljust(20)}{nome_produto.ljust(36)}{preco_formatado.rjust(10)}  |')
                
            print('-----------------------------------------------------------------------') # --> Cabeçalho que será exibido antes dos 5 produtos buscados
            adiciona_carrinho = input('Por favor, digite o código do produto que desejas adicionar ao carrinho. \n -> ').upper()    
            
            for indice in lista_busca[:5]:
                nome_produto, categoria, preco, quantidade, codigo_produto = indice.upper().strip().split(';')
                
                if adiciona_carrinho == codigo_produto:
                    itens_carrinho.append(f'{codigo_produto} | {nome_produto} | {categoria} | {preco_formatado}')
                    print(itens_carrinho)
                    print('Produto adicionado ao carrinho!')


        elif (opcao == '3'):
            limpa()
            valor_total = 0
            itens_total = 0

            for item in itens_carrinho:
                print(item)
                itens_total += 1
                codigo_produto, nome_produto, categoria, preco = item.split(' | ')
                valor_total += float(preco.replace('R$', '').replace(',', '.'))

            preco_total_formatado = locale.currency(valor_total)
            print('Total de itens:', itens_total)
            print('Valor total do carrinho:', preco_total_formatado)
      
        elif (opcao == '0'):
            limpa()
            valor_total = 0
            itens_total = 0

            for item in itens_carrinho:
                print(item)
                itens_total += 1
                codigo_produto, nome_produto, categoria, preco = item.split(' | ')
                valor_total += float(preco.replace('R$', '').replace(',', '.'))

            preco_total_formatado = locale.currency(valor_total)
            print('Total de itens:', itens_total)
            print('Valor total do carrinho:', preco_total_formatado)
            print('\nObrigado por usar o CAIOrrinho. Até a próxima! <3')
