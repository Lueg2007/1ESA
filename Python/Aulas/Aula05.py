'''
i = 0
pares = 0

while i < 10:
    num = int(input(f"Diga o {i+1}° número: "))
    if num%2 == 0:
        pares = pares + 1
    i = i + 1 #Esse espaçamento faz diferença, NÃO ESQUECER ESPAÇAMENTO!!!!

print(f"Você digitou {pares} números pares e {i - pares} números ímpares")



senha_fornecida = input("Digite a senha:")
senha_cadastradra = '0702'
tentativas = 1

while senha_fornecida != senha_cadastradra and tentativas < 3:
    print(f"Você errou, você tem mais {3 - tentativas} tentativas restantes!")
    senha_fornecida = input("Digite a senha:")
    tentativas = tentativas + 1

if senha_cadastradra == senha_fornecida:
    print("Acesso Permitido!")
else:
    print("Acesso Negado!")



sexo = input("Qual é o seu sexo?:")

while sexo != "masculino" and sexo != "feminino":
    print("Erro. Digite um sexo válido")
    sexo = input("Qual é o seu sexo?:")

altura = float(input("Agora, qual é a sua altura?:"))
if sexo == "masculino":
        peso = (72.7 * altura) - 58
        print(f"Esse é ó seu peso {peso} ideal!")
else:
    peso = (62.1 * altura) - 44.7
    print(f"Esse é o seu peso {peso} ideal!")



sexo = input("Qual é o seu sexo?:")

while not (sexo == "masculino" or sexo == "feminino"):
        print("Erro. Digite um sexo válido")
        sexo = input("Qual é o seu sexo?:")

altura = float(input("Agora, qual é a sua altura?:"))
if sexo == "masculino":
        peso = (72.7 * altura) - 58
        print(f"Esse é ó seu peso {peso} ideal!")
else:
        peso = (62.1 * altura) - 44.7
        print(f"Esse é o seu peso {peso} ideal!")



ano = input("Digite o seu ano de nascimento:")

while not ano.isnumeric():
    print("Erro. O que foi digitado não é um número")
    ano = input("Digite o seu ano de nascimento:")
if ano.isnumeric:
    print(f"Você nasceu em {ano}!")

    #OUTRO JEITO

num = input("Diga um número: ")
print(type(num))

if num.isnumeric():
    num = int(num)

else:
    print("Você não digitou um número!")
print(type(num))



i = 0
pares = 0

while i < 10:
    num = int(input(f"Diga o {i+1}° número: "))
    if num%2 == 0:
        pares += 1
    i += 1 #Esse espaçamento faz diferença, NÃO ESQUECER ESPAÇAMENTO!!!!

print(f"Você digitou {pares} números pares e {i - pares} números ímpares")

# Explicação sobre +=
'''