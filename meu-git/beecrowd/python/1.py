def calcular_media_ponderada(nota1, nota2):
    peso_nota1 = 3.5
    peso_nota2 = 7.5
    soma_pesos = peso_nota1 + peso_nota2
    media = (nota1 * peso_nota1 + nota2 * peso_nota2) / soma_pesos
    return media

# Obter entradas do usuário
nota1 = float(input())
nota2 = float(input())

# Verificar se as notas estão dentro do intervalo válido
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media_aluno = calcular_media_ponderada(nota1, nota2)
    print(f"MEDIA = {media_aluno:,.5f}") # Exibido na tela o resultado com 5 casas decimais
else:
    print("As notas devem estar no intervalo de 0 a 10. Por favor, tente novamente!")
