def contar_letras(palavra):
    contador = 0 
    for contar_letras in palavra:
        contador += 1 
    return contador 

def contar_palavras_e_letras(lista):
    qtd_palavras = 0
    for i, palavra in enumerate(lista):
        qtd_palavras += 1
        qtd_letras = contar_letras(palavra)
        print(f'Quantidade de letras na palavra {i + 1}: {qtd_letras}')

    print(f'Quantidade de palavras na lista: {qtd_palavras}')

lista = ["oi", "tudo bem", "palavra", "quadro"]
contar_palavras_e_letras(lista)