produto = []
resultado = []
carrinho = []

def carrinho_de_compras(cod_prod):
     for pesquisa in produto:
        for item in pesquisa:
            if str(cod_prod) in str(item).lower():
                resultado.append(pesquisa)
        print(' ')
        print(carrinho)

def menu():
        print('------------------------------------------------------')
        print('| [1] - Fazer nova busca                             |')
        print('| [2] - Adicionar itens ao carrinho                  |')
        print('| [3] - Visualizar itens do carrinho                 |')
        print('| [4] - Finalizar compra                             |')
        print('------------------------------------------------------')
        
def busca_produtos(busca):
    for pesquisa in produto:
        for item in pesquisa:
            if str (busca) in str(item).lower():
                resultado.append(str(pesquisa).split(','))
    print('Resultado:')
    print('Codigo | Produto | Valor')
    for posicao in range(0, 5):
        print(resultado[posicao][4] + '\t' + resultado[posicao][0] + '\t' + resultado[posicao][2])
    print(' ')
    menu()
    opcao = input('Escolha uma opção do painel (digite apenas números): ')
    if opcao == '1':
        print('Nova busca solicitada!')
        busca2 = input('Informe o produto: ')
        busca_produtos(busca2)
    elif opcao == 2:
        cod_prod = str(input('Digite o código do produto que deseja adicionar')).lower()
        carrinho_de_compras(cod_prod)
    else:
         print('acabou')


with open('produtos.csv', 'r', encoding='utf=8') as arquivo:
        next(arquivo)
        lista_produtos = arquivo.readlines()
        # criando a lista de produto
        for i in lista_produtos:
            produto.append (i.strip('\n').split(';'))
        busca = input('Busca: ').lower()
        busca_produtos(busca)
        