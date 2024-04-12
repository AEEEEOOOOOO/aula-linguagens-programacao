idade = int(input("Digite sua idade: "))

if idade < 13:
    print("Você é criança!")
elif idade < 19:
    print("Você é adolescente!")
elif idade < 60:
    print("Você é adulto!")
elif idade > 60:
    print("Você é idoso!")
else:
    ("valor digitado é invalido!")
