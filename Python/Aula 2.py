''' frase = "Hello World!!!!!"
print(frase)
print(frase)
print(frase)
print(frase)

print ("Hello World!!!!!")
print ("Hello World")
print ("Hello World")
print ("Hello World")

palavra_1 = "Olá"
palavra_2 = "Mundo"
print(palavra_1 + palavra_2)
frase = palavra_1 + palavra_2
print (frase)


frase = "Eu"
print(frase)
frase = frase + " " + "sou"
print(frase)
frase = frase + " " + "o"
print(frase)
frase = frase + " " + "Luigi"
print(frase)

frase = input("Diga a primeira palavra: ")
print(frase)
frase = frase + " " + input("Diga a segunda palavra: ")
print(frase)
frase = frase + " " + input("diga a terceira palavra: ")
print(frase)
frase = frase + " " + input("diga a quarta palavra: ")
print(frase)
frase = frase + " " + input("diga a quinta palavra: ")
print(frase)

print(type("Olá Mundo"))

a = 2
b = 3
print(type(a))
soma = a + b
sub = a - b
mult = a * b
div = a/b
potencia = a ** b
print(f"A soma entre {a} e {b} é {soma}")
print(f"A subtração entre {a} e {b} é {sub}")
print(f"A divisão entre {a} e {b} é {div}")
print(f"A multiplicação entre {a} e {b} é {mult}")
print(f"A potenciação entre {a} e {b} é {potencia}")

nome = input("Diga o seu nome: ")
print(f"Olá, {nome}! Bem vindo à calculadora! ")
a = int(input("Diga o primeiro número: "))
b = int(input("Diga o segundo número: "))
soma = a + b
sub = a - b
mult = a * b
div = a/b
pot = a ** b

a = 2
b = 3
print(f"O resultado de {a} > {b} é {a>b}")
print(f"O resultado de {a} < {b} é {a<b}")
print(f"O resultado de {a} >= {b} é {a>=b}")
print(f"O resultado de {a} <= {b} é {a<=b}")
print(f"O resultado de {a} == {b} é {a==b}")
print(f"O resultado de {a} != {b} é {a!=b}")

a = 2
b = 3
print(f"O resultado de {a} > {b} and {a} < {b}, ou seja,{2 > 3} and {2 < 3} dá {2 > 3 and 3 > 2}")
print(f"O resultado de {a} != {b} and {a} <= {b}, ou seja,{2 != 3} and {2 <= 3} dá {2 != 3 and 3 >= 2}")
print(f"O resultado de {a} >= {b} and {a} == {b}, ou seja,{2 >= 3} and {2 == 3} dá {2 >= 3 and 3 == 2}")
print(f"O resultado de {a} > {b} and {a} == {b}, ou seja,{2 > 3} and {2 == 3} dá {2 > 3 and 3 == 2}")
print("")
print(f"O resultado de {a} > {b} or {a} < {b}, ou seja,{2 > 3} or {2 < 3} dá {2 > 3 or 3 > 2}")
print(f"O resultado de {a} != {b} or {a} <= {b}, ou seja,{2 != 3} or {2 <= 3} dá {2 != 3 and 3 >= 2}")
print(f"O resultado de {a} <= {b} or {a} >= {b}, ou seja,{2 <= 3} or {2 >= 3} dá {2 <= 3 and 3 >= 2}")
print(f"O resultado de {a} >= {b} or {a} > {b}, ou seja,{2 >= 3} or {2 > 3} dá {2 >= 3 and 3 > 2}")

idade = int(input("Diga a sua idade: "))
if idade >= 18:
    print("Adulto")
if idade <= 18:
    print("Criança")
if idade >= 60:
    print("Idoso")

idoso = input("Você é idoso?\n->")
deficiente = input("Você é pcd?\n->")
if idoso == 'sim' or deficiente == 'sim':
    print("Pode estacionar!")
else:
    print("Não pode estacionar, cai fora!")
'''
junio = input("Você é junior?\n->")
leandro = input("Você é leandro?\n->")
if junio == 'sim' or leandro == 'sim':
    print("Você pode juniar!")
else:
    print("Junior está bravo com você!")

