def contar_letras(palavra):
    contador = 0
    for contar_letras in palavra:
        contador += 1
    return contador

def analisar_lista(lista_palavras):
    num_palavras = 0
    for palavra in lista_palavras:
        num_palavras += 1
    print(f"quantidade de palavras na lista: {num_palavras}")
    
    for i, palavra in enumerate(lista_palavras, 1):
        num_letras = contar_letras(palavra)
        print(f"quantidade de letras na palavra {i}: {num_letras}")

num_palavras = int(input("Digite o número de palavras na lista: "))
lista_strings = []
for i in range(num_palavras):
    palavra = input(f"Digite a palavra {i+1}: ")
    lista_strings.append(palavra)

analisar_lista(lista_strings)
