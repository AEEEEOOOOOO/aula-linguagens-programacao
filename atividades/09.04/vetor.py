# Obter entradas do usuário
nome = str(input("Por favor, digite seu nome: "))
sobrenome = str(input("Por favor, digite seu sobrenome: "))

# Mostrando apenas a primeira letra do nome em maiúscula
print(nome[0].lower() + nome[1:10].upper())

# Mostrando apenas a primeira letra do sobrenome em minúscula
print(sobrenome[0].upper() + sobrenome[1:10].lower())
