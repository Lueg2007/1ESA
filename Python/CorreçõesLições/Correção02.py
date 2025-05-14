'''
# EXERCÍCIO 1

num = input("Diga um número:")
while not num.isnumeric():
    num = input("Diga um número:")
num = int(num)
while num < 0 and num > 10:  # while not num > 0 and num <= 10
    print("Número inválido!")
    num = input("Diga um número:")

-------------------------------------------------------------------------------

# EXERCÍCIO 2
nome = input("Diga seu nome:")
while len(nome) < 3:
    nome = input("Diga seu nome:")

while True:
    idade = input("Diga a sua idade:")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        print(f"{num} está fora do intervalo 0 a 150")
    else:
        print(f"Deve ser digitado um número!")
salario = input("Diga seu salário:")
while not salario.isnumeric():
    salario = input("Diga seu salário:")
salario = int(salario)

sexo = input("Diga f ou m:")
while sexo != 'f' and sexo != 'm':
    sexo = input("Diga f ou m:")

e_c = input("Diga s, v, c ou d:")
while not(e_c == 's' or e_c == 'v' or e_c == 'c' or e_c == 'd'):
    e_c = input("Diga seu s, v, c ou d:")

-------------------------------------------------------------------------------

#EXERCÍCIO 3

#A fórmula é uma função exponencial, como se fossem juros compostos. A = 80 . 1.03^t e B = 200 . 1,015^t
a = 80
b = 200
t = 0
while a < b:
    a *= 1.03 #ele mesmo vezes 1.03
    b *= 1.015
    t += 1 #ele mesmo +1
print(t)

#Não tem como terminar por esse meio, é só resolver a equação exponencial

-------------------------------------------------------------------------------

#EXERCÍCIO 4

i = 0 #Contador de repetições
soma = 0
while i < 5:
    nota = input(f"Diga a {i+1} nota:")
    while not nota.isnumeric():
        nota = input(f"Diga a {i + 1} nota:")
    nota = int(nota)
    soma += nota
    i += 1
media = soma/i

-------------------------------------------------------------------------------

#EXERCÍCIO 5

a = input(f"Diga o primeiro número: ")
while not a.isnumeric():
    a = input(f"Diga o primeiro número: ")
a = int(a)

b = input(f"Diga o primeiro número: ")
while not b.isnumeric():
    b = input(f"Diga o primeiro número: ")
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a)
    a += 1

-------------------------------------------------------------------------------

#EXERCÍCIO 6

senha_cadastrada = '1234'
senha_tentativa = input("Diga a sua senha: ")
tentativas = 1
while senha_cadastrada != senha_tentativa and tentativas < 3:
    print(f"Você é Hacker? Só mais {3 - tentativas} tentativas!")
    senha_tentativa = input("Diga a sua senha: ")
    tentativas += 1

if senha_tentativa == senha_cadastrada:
    print("Acesso liberado")
else:
    print("Sai Hacker!")

usuario = input("Diga seu nome de usuário: ")
senha = input("Diga a sua senha: ")
while usuario == senha:
    print("Usuário não pode ser igual a senha...")
    usuario = input("Diga seu nome de usuário:")
    senha = input("Diga sua senha:")

-------------------------------------------------------------------------------

#EXERCÍCIO 7

num = 1
while num <= 10:
    print(f"Tabuada do {num}:")
    mult = 1
    while mult <= 10:
        print(f"{num}*{mult} = {num*mult}")
        mult += 1
    print()
    num += 1

-------------------------------------------------------------------------------

#EXERCÍCIO 8

a = 1
b = 1
print(a,b,end=' ')#End é para deixar as coisas uma do lado da outra
i = 2
while i < 100:
    c = a + b
    print(c/b)
    a = b
    b = c
    i += 1

-------------------------------------------------------------------------------

#EXERCÍCIO 9

i = 0
pares = 0
while i < 10:
    b = input(f"Diga o {i+1} número:")
    while not b.isnumeric():
        b = input(f"Diga o {i+1} número:")
    b = int(b)
    if b%2 == 0:
        pares += 1
    i += 1
print(f"Você digitou {pares} pares e {i - pares} ímpares")

#EXPLICAÇÃO DA SOMA

i = 0
soma = 0
while i < 10:
    i += 1
    soma += i
print(soma)

#FATORIAL EX 9

i = 1
fatorial = 1
while i < 5:
    i += 1
    fatorial *= i
print(fatorial)

#OUTRO MÉTODO

i = 1
fatorial = 1
num = 5
produto = f"{num}!*"
while i < num:
    produto += f"{i}*"
    i += 1
    fatorial *= i
produto += f"{i} = {fatorial}"
print(produto)

-------------------------------------------------------------------------------

#EXECÍCIO 10

num = 7
i = 2

while True:
    print(f"{num}%{i} = {num%i}")
    if num %i == 0:
        print("Não é primo!")
        break
    elif i >= num**(1/2):
        print("É primo")
        break
    i += 1
#O menor número de vezes que um número pode caber dentro de outro número é 2 vezes, ou seja, a sua metade, exemplo: 100, seu maior divisor é 50 que cabe 2 vezes dentro dele
#A partir da metade não precisa mais verificar, a partir da metade começa uma ordem decrescente dos números restantes

-------------------------------------------------------------------------------

#EXERCÍCIO 12 (Ver o exercício 5)

-------------------------------------------------------------------------------

#EXERCÍCIO 13

salario = 1000
ano = 1995
taxa_inicial = 0.015
while ano < 2000:
    taxa = 1 + taxa_inicial
    taxa_inicial *= 2
    salario *= taxa
    ano += 1
print(f"{salario:.2f}")

-------------------------------------------------------------------------------

'''

#EXERCÍCIO 14