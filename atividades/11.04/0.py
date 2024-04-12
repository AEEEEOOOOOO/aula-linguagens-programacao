# O código abaixo tem alguns problemas e está incompleto! 
# Altere o código abaixo para que ele atue como uma calculadora
# O usuário deve digitar um valor, um operador e outro valor
# seu programa deverá imprimir na tela o resultado da operação
# Faça com que o seu programa funcione até que o usuário digite -1
valor1 = 0
valor2 = 0
resultado = 0

valor1 = float(input("Digite o valor 1 \n"))

operadores_validos = ['+', '-', '*', '/']
operador = input("Digite o operador (+, -, *, /): ")

while operador not in operadores_validos:
    print("Operador inválido. Digite novamente.")
    operador = input("Digite o operador (+, -, *, /): ")

valor2 = float(input("Digite o valor 2 \n"))

while valor1 != -1 and valor2 != -1:
    
    if operador == '+':
        resultado = (valor1 + valor2)
        print("Resultado: {} {} {} = {}".format(valor1, operador, valor2, resultado ))

    elif operador == '-':
        resultado = valor1 - valor2
        print("Resultado: {} {} {} = {}".format(valor1, operador, valor2, resultado ))

    elif operador == '*':
        resultado = valor1 * valor2
        print("Resultado: {} {} {} = {}".format(valor1, operador, valor2, resultado ))

    elif operador == '/':
        resultado = valor1 / valor2
        print("Resultado: {} {} {} = {}".format(valor1, operador, valor2, resultado ))
    else:
        print('operador inválido')

    valor1 = float(input("Digite o valor 1 \n"))

    operadores_validos = ['+', '-', '*', '/']
    operador = input("Digite o operador (+, -, *, /): ")

    while operador not in operadores_validos:
        print("Operador inválido. Digite novamente.")
        operador = input("Digite o operador (+, -, *, /): ")

    valor2 = float(input("Digite o valor 2 \n"))

   