'''
Ex1
n1 = int(input("Digite um número:"))
n2 = int(input("Coloque outro número:"))
if n1 > n2:
    print(f"{n1} é o maior número")
else:
    print(f"{n2} é o maior número")

Ex2
Ano = int(input("Digite seu ano de nascimento:"))
if Ano <= 2009:
    print("Pode votar!")
else:
    print("Não pode votar!")

Ex3
senha = int(input("Qual é a senha?"))

if senha == 1234:
 print("PERMITIDO")

else:
 print("NEGADO")

Ex4
macas = float(input("Quantas maçãs você gostaria de comprar?:"))
if macas < 12:
    valor = (0.30 * macas)
    print(f"O valor total pago nas maçãs é de {valor} reais")
else:
    valor = (0.25 * macas)
    print(f"O valor total pago nas maçãs é de {valor} reais")

Ex5
n1 = int(input("Digite um número inteiro:"))
n2 = int(input("Digite outro número inteiro:"))
n3 = int(input("Agora digite o terceiro e último número inteiro:"))

if n1 < n2 < n3:
    ordem1 = n1, n2, n3
    print(f"A ordem correta corrta é {ordem1}!")
elif n3 < n1 < n2:
    ordem2 = n3, n1, n2
    print(f"A ordem correta corrta é {ordem2}!")
elif n2 < n3 < n1:
    ordem3 = n2, n3, n1
    print(f"A ordem correta corrta é {ordem3}!")
elif n1 < n3 < n2:
    ordem4 = n1, n3, n2
    print(f"A ordem correta corrta é {ordem4}!")
elif n2 < n1 < n3:
    ordem5 = n2, n1, n3
    print(f"A ordem correta corrta é {ordem5}!")
elif n3 < n2 < n1:
    ordem6 = n3, n2, n1
    print(f"A ordem correta corrta é {ordem6}!")

Ex6
sexo = input("Qual é o seu sexo?:")
altura = float(input("Agora, qual é a sua altura?:"))
if sexo == "masculino":
    peso = (72.7 * altura) - 58
    print(f"Esse é ó seu peso {peso} ideal!")
else:
    peso = (62.1 * altura) - 44.7
    print(f"Esse é o seu peso {peso} ideal!")

Ex7 e Ex8
poligono = int(input("Quantos lados seu polígono possui?:"))
if poligono == 3:
    print("Seu polígono é um triângulo! Agora, vamos calcular a sua área")
    base = int(input("Qual é a medida da base desse triângulo?"))
    altura = int(input("Qual é a medida da altura desse triângulo?"))
    area = (base * altura) / 2
    print(f"A sua área é de {area}cm²")
elif poligono == 4:
    print("Seu polígono é um quadrado! Agora, vamos calcular a sua área")
    lado = int(input("Qual é a medida do lado desse quadrado?"))
    area = (lado * lado)
    print(f"A sua área é de {area}cm²")
elif poligono == 5:
    print("Seu polígono é um pentágono! Agora, vamos calcular a sua área")
    lado = float(input("Qual é a medida do lado desse pentágono?"))
    apotema = (lado / 1.45)
    area = (lado * 5 * apotema) / 2
    print(f"A sua área é de {area:.2f}cm²")
elif poligono < 3:
    print("NÃO É UM POLÍGONO!")
else:
    print("POLÍGONO NÃO IDENTIFICADO")

Ex9
n1 = int(input("Por favor, digite um número inteiro:"))
n2 = int(input("Digite um número inteiro diferente:"))
n3 = int(input("Por último, digite outro valor diferente e inteiro:"))
if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número entre eles")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número entre eles")
else:
    print(f"{n3} é o maior número entre eles")

Ex10
n1 = int(input("Qual a medida de um dos lados do seu triângulo?:"))
n2 = int(input("Qual a medida de um outro lado do seu triângulo?:"))
n3 = int(input("Qual a medida do último lado do seu triângulo?:"))
if n1 == n2 == n3:
    print("Seu triângulo é equilátero")
elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
    print("Seu triângulo é isócele")
else:
    print("Seu triângulo é escaleno")
'''

angulo = int(input("Qual o grau de um dos lados do seu triângulo?:"))
if angulo == 90:
    print("Seu triângulo é retângulo")
elif angulo > 90 and angulo <180:
    print("Seu triângulo é obtusângulo")
elif angulo < 90 and angulo > 0:
    print("Seu triângulo é acutângulo")
else:
    print("Sua forma geométrica não é um triângulo")
