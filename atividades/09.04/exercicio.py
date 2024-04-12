# # Obter entradas do usuário
# nome = str(input("Por favor, digite seu nome: "))
# posicao = int (input("Digite em números a posição que desejas alterar uma letra: "))
# letra = str (input("Agora digite a nova letra: "))
# caracter_antigo = nome[posicao]
# caracter_novo = nome[posicao] + letra

# # Substituindo um caractere específico (por exemplo, 'a' por 'x')
# caractere_antigo = nome[posicao]
# caractere_novo = nome[posicao + letra]
# novo_nome = nome.replace(caractere_antigo, caractere_novo)


# print(novo_nome)



# # #Adicionar uma letra em certa posição
# # # Contar e salvar em uma variável o número de caracteres
# # len(nome)
# # tamanho_nome = len(nome)
# # print("O seu nome possui" tamanho_nome "caracteres.")

# # # Condiçao

# # # Mostrando apenas a primeira letra do sobrenome em minúscula

# Obtendo a entrada do usuário
nome = input("Digite um nome: ")
posicao = int(input("Digite a posição do caractere a ser substituído (começando em 0): "))
nova_letra = input("Digite a nova letra para substituir: ")

if posicao < 0 or posicao >= len(nome):
    print("Posição inválida.")
elif: 
    nova_letra == R 
    nova_letra_S == S
elif:
    lista_nome = list(nome)
    lista_nome[posicao] = nova_letra
    novo_nome = ''.join(lista_nome)  

    print("Nome com caractere substituído:", novo_nome)
