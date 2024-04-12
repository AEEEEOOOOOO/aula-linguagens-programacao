# O código abaixo é uma tentativa de criar um verificador de palíndromos.
# Palíndromos são palavras ou frases que são iguais quando lidas de trás para frente.
# No entanto, o código está incompleto e contém erros.
# Complete e corrija o código para que ele funcione corretamente.
# O usuário deve digitar uma palavra ou frase, e o programa deve imprimir se é um palíndromo ou não.
# Ignore espaços, pontuações e diferenças entre maiúsculas e minúsculas.


caracter = ['.', ',', '!', ' ', '?', '@', '#', '*', '&']

texto = input("Digite um texto: ") #RECEBE O TEXTO DO USUÁRIO

for i in range(len(caracter)):
    texto = texto.replace(caracter[i], '')

caixaAltaTexto = texto.upper() #CONVERTE O TEXTO INTEIRO PARA CAIXA ALTA

texto_invertido = texto[::-1] #INVERTE O TEXTO ESCRITO PELO USUÁRIO
caixaAltaIvertido = texto_invertido.upper() #CONVERTE O TEXTO INTEIRO INVERTIDO PARA CAIXA ALTA


print(texto)
print(texto_invertido)

if caixaAltaTexto == caixaAltaIvertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")