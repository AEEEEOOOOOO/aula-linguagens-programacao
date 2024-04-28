# Faça um programa em python com uma ou mais funções que receba como parametro uma lista de strings 
# como essa ["oi", "tubem", "palavra", "quadro"] e imprima na tela o seguinte resultado:

# quantidade de palavras na lista: 4
# quantidade de letras na palavra 1: 2
# quantidade de letras na palavra 2: 5
# quantidade de letras na palavra 3: 7
# quantidade de letras na palavra 4: 6

# Você não pode usar a função len()

def contar_letras(palavra):
    contador = 0
    
    for letra in palavra:
        contador += 1

    return contador

entrada_usuario = input("Digite um texto: ")
print("O número de letras do texto é", contar_letras(entrada_usuario))




