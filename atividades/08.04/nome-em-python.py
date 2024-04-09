# Obter entradas do usuário
nome = str(input("Por favor, digite seu nome: "))
sobrenome = str(input("Por favor, digite seu sobrenome: "))

# Mostrar sobrenome e primeira letra do nome
print(sobrenome, ',', nome[0], sep='') # 'sep' usado para resetar o espaço entre as vírgulas

# Contar e salvar em uma variável o número de caracteres
len(nome)
tamanho_nome = len(nome)
print(f"O seu nome possui {tamanho_nome} caracteres.")

# Definir e mostrar o último caracteres da variável nome
ultima_letra = nome[tamanho_nome -1]
print(f"A última letra do seu nome é {ultima_letra}.")