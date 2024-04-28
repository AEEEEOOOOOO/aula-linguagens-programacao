import os
import pdb

def limpa():
    os.system('cls')

def rastrear():
    pdb.set_trace()

# Cabeçalho para a exibição dos resultados
cabecalho = ("Código     | Nome do Produto              | Preço")

# Inicializando o programa com lista_produtos, que guardará em tipo lista os produtos lidos
lista_produtos = []

# Lendo um arquivo, pulando a primeira linha dele e definindo todas as linhas na variável lista_linhas
with open('produtos.csv', 'r', encoding= "utf-8") as produtos:
    next(produtos)
    lista_produtos = produtos.readlines()
 
# Inicializando contador e solicitando entrada do usuário
contador = 0
resultado = input('Por favor, digite o nome do produto OU o código do produto OU a categoria do produto.\n -> ').upper()

# Inicializando a lista de resultados fora do loop
lista_resultados = []

# Adicionando o cabeçalho já criado na lista de resultados
lista_resultados.append(cabecalho)

# Percorrendo toda a lista e separando os valores das colunas em variáveis
for linha in lista_produtos:
    nome_produto, categoria, valor, quantidade, codigo_produto = linha.upper().strip('\n').split(';') # Convertendo os valores da lista em letras maiúsculas, ignorando as quebras e separando-as por ;

    # Verificando se o valor inserido existe, se existir então prossiga
    if resultado in nome_produto or resultado == codigo_produto or resultado == categoria:
        contador += 1

        # Adicionando o resultado à lista de resultados
        lista_resultados.append(resultado)
        


        if contador >= 5:  # Verificando o contador após adicionar o resultado à lista
            break

# Imprimindo os resultados apenas se houver algum
if contador > 0:
    for resultado in lista_resultados:
        print(resultado)
else:
    print("Nenhum resultado encontrado.")

     

# opcao = ''
# while opcao != '0':
#     print('------------------------------------------------------')
#     print('| [1] - Adicionar item ao carrinho                   |')
#     print('| [2] - Visualizar itens do carrinho                 |')
#     print('| [0] - Finalizar compra                             |')
#     print('------------------------------------------------------')
#     opcao = input('Escolha uma opção do painel (digite apenas números): ')
#     if opcao == '1':
#         break
#     elif opcao == '2':
#          print('AAAAAAAAAAAAAA')
