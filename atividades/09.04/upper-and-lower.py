# Obter entradas do usuário
nome = str(input("Por favor, digite seu nome: "))
sobrenome = str(input("Por favor, digite seu sobrenome: "))
ano_nasc = (input("Por favor, digite seu ano de nascimento: "))

# Mostrando NOME e SOBRENOME maiúsuculo e concatenando tudo
print(nome.lower() + ' ' + sobrenome.upper() + ' nasceu no ano de ' + ano_nasc)
