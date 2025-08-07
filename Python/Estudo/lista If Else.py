"""
EX4
macas = int(input("Digite quantas mçãs você gostaria de comprar:"))
if macas < 12:
    duzia = 0.30 * macas
    print(f"O valor da sua compra é {duzia} reais.")
else:
    maisque = 0.25 * macas
    print(f"O valor da sua compra é {duzia} reais.")

EX6
altura = float(input("Digite a sua altura:"))
sexo = int(input("Digite qual o é seu sexo (1: feminino 2: masculino):"))

if sexo == 1:
    pesoF = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {pesoF}.")
else:
    pesoM = (72.7 * altura) - 58
    print(f"Seu peso ideal é {pesoM}.")

EXS 7 E 8
lados = int(input("Digite o número de lados do seu polígono:"))
medida = int(input("Digite a medida do lado do seu polígono em centímetros:"))

if lados < 3:
    print("NÃO é um polígono.")
elif lados > 5:
    print("Polígono não identificado.")
else:
    perimetro = lados*medida
    if lados == 3:
        print(f"Seu polígono é um TRIÂNGULO e a medida do seu perímetro é {perimetro}.")
    elif lados == 4:
        print(f"Seu polígono é um QUADRADO e a medida do seu perímetro é {perimetro}.")
    else:
        print(f"Seu polígono é um PENTÁGONO e a medida do seu perímetro é {perimetro}.")


EX9
valor1 = int(input("Digite o 1º número:"))
valor2 = int(input("Digite o 2º número:"))
valor3 = int(input("Digite o 3º número:"))

maior = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3

print(f"O maior valor é {maior}")

EX 5 - ERRADO
valor1 = int(input("Digite o 1º número:"))
valor2 = int(input("Digite o 2º número:"))
valor3 = int(input("Digite o 3º número:"))

maior = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3

menor = valor1
if valor2 > menor:
    menor = valor2
if valor3 > menor:
    menor = valor3

meio = valor1+ valor2+ valor3 - maior - menor
print(f"A ordem crescente é {menor}, {meio}, {maior}")

EX 5 - CERTO (AUX) #AUX guarda o valor de a, porque quando ele recebe o valor de b, seu valor some, ou seja, aux armazena um valor para não ser perdido
"""
a = int(input("Digite o 1º número:"))
b = int(input("Digite o 2º número:"))
c = int(input("Digite o 3º número:"))
if a>b and a>c:
    aux = a         #armazenando o valor
    a = c
    c = aux
elif b>c:
    aux = b
    b = c
    c = aux
if a>b:
    aux = a
    a = b
    b = aux
print(a,b,c)
