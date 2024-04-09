# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

# Entrada
# O arquivo de entrada contém 4 valores inteiros.

# Saída
# Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

def calcular_diferenca(valorA, valorB, valorC, valorD):
    int = valorA, valorB, valorC, valorD

    # Obter entradas do usuário
valorA = float(input())
valorB = float(input())
valorC = float(input())
valorD = float(input())

DIFERENCA = (valorA * valorB - valorC * valorD)
print(f'DIFERENCA = { DIFERENCA:,.0f}')