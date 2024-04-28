import os  # Importa o módulo os para usar funcionalidades do sistema operacional

resultado_obtido = []
resultados_de_busca = []
armazena_codigo = []
contador = 0  # Variável para contar itens encontrados durante a pesquisa
indice = ''  # Variável não utilizada
ler_file = []
chave_busca = ''

# Função para limpar a tela
def limpa():
    os.system("clear")


# Funções para exibir os menus
def menu1(): # --> Exibir menu principal 
    print('-----------------------------------------------------------------------')
    print('| [1] - Fazer uma nova busca                                          |')
    print('| [2] - Adicionar item no carrinho                                    |')
    print('| [0] - Finalizar compra                                              |')
    print('-----------------------------------------------------------------------')

def menu2():
    print('|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|')
    print("|/\/\|  [1] Fazer nova busca       |/\/\|")
    print("|/\/\|  [2] Adicionar ao carrinho  |/\/\|")
    print("|/\/\|  [3] Visualizar carrinho    |/\/\|")
    print("|/\/\|  [4] Finalizar a compra     |/\/\|")
    print('|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|')



menu1()
opcao = input('Escolha uma opção: ').lower()

while opcao != 'sair':

    # Abre o arquivo 'produtos.csv' em modo de leitura ('r')
    with open('produtos.csv', 'r') as file:
        next(file)  # Pula a primeira linha (cabeçalho)
        ler_file = file.readlines()  # Lê todas as linhas do arquivo e as armazena em uma lista

        if (opcao == '1'):
            limpa()
            resultados_de_busca = []
            chave_busca = input('Digite sua chave de busca:\n>')  # Solicita ao usuário a chave de busca
            chave_busca = chave_busca.upper()  # Converte a chave de busca para minúsculas

            print(f'{"CODIGO".ljust(25)}{"NOME DO PRODUTO".ljust(40)}{"VALOR EM R$".rjust(15)}')
            for indice in ler_file:
                # Divide a linha em colunas e converte para maiúsculas
                nome_produto, categoria, preco, quantidade, codigo_produto, *_ = indice.upper().strip().split(';')
                # Verifica se a chave de busca está presente no nome do produto, no código do produto ou no preço
                if chave_busca in nome_produto or chave_busca == codigo_produto or chave_busca == preco:
                    resultados_de_busca.append(indice)
            
            for indice in resultados_de_busca[:5]:
                nome_produto, categoria, preco, quantidade, codigo_produto, *_ = indice.upper().strip().split(';')
                print(f'{codigo_produto.ljust(12)}{nome_produto.ljust(55)}{preco.rjust(10)}')


        if (opcao == '2'):
            limpa()
            for indice in resultados_de_busca[:5]:
                nome_produto, categoria, preco, quantidade, codigo_produto, *_ = indice.upper().strip().split(';')
                print(f'{codigo_produto.ljust(12)}{nome_produto.ljust(55)}{preco.rjust(10)}')

            
            digita_codigo = input('Digite o código do produto \n-> ')
            digita_codigo = digita_codigo.upper()
            
            for indice in resultados_de_busca[:5]:
                nome_produto, categoria, preco, quantidade, codigo_produto, *_ = indice.upper().strip().split(';')

                if digita_codigo == codigo_produto:
                    armazena_codigo.append(codigo_produto)
                    print(armazena_codigo)                







        menu1()
        opcao = input('Escolha uma opção: ').lower()

    #     # Exibe cabeçalho da tabela de produtos
    #     # Itera sobre cada linha do arquivo
      
          
    #         # if contador == 5:  # Se já encontrou 5 itens, interrompe a busca
    #         #     break
    #     for indice in range(0,5):

    #         if chave_busca in nome_produto or chave_busca == codigo_produto or chave_busca == preco:
    #             resultado_obtido = (f'{codigo_produto.ljust(12)}{nome_produto.ljust(55)}{preco.rjust(10)}')
    #             print(resultado_obtido)  # Exibe o resultado encontrado


    #     # if opcao == '1':
    #     #     pesquisar_produtos()
    #     # elif opcao == '2':
    #     #     #   adicionar_carrinho()
    #     # elif opcao == '3':
    #     #     #  finalizar_compra()