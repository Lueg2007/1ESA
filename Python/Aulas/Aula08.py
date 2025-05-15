'''
vogais = 0
for char in 'danilo':
    if char in ['a','e','i','o','u']:
        vogais += 1
print(vogais)
for i in range(1,10,3):
    print(i)
for i in range(20,10,2):
    print(i)

for i in range(10):
    print(i)
    i = 0
    print(i)

for i in range(1,11):
    print(f"Tabuada do {i}:")
    for j in range(1,11):
        print(f"{i}*{j} = {i*j}")
    print()

i = 1
j = 1
while i < 11:
    j = 1
    print(f"Tabuada do {i}:")
    while j < 11:
        print(f"{i}*{j} = {i*j}")
        j += 1
    i += 1
    print()

lista = [3,True,1.5,'Luigi',[]]
for elem in lista:
    print(elem)
print()
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

lista = [3,True,1.5,'Luigi',[]]
for elem in lista:
    print(elem)
print()
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")


lista = [3,True,1.5,'Luigi',[]]
for elem in lista:
    elem = 1
print(lista)
for i in range(len(lista)):
    lista[i] = 1
print(lista)

profs = ['Danilo','André','Gabi','Yan','Lucas','Luís']
materias = ['Python','Historinha','Sw&TX','Matemática','Edge','Front','Web']
for i in range(len(profs)):
    print(f"O/A {profs[i]} dá a materia de {materias[i]}.")

alunos = ['Lucas Sena','Rhariel','Sara','Isabela','Lucas Zago']
notas = [8,8.5,6,4,1]
for i in range(len(alunos)):
    if notas[i] < 6:
        print(f"O/A aluno(a) {alunos[i]} foi reprovado com nota {notas[i]}.")
    else:
        print(f"O/A aluno(a) {alunos[i]} foi aprovado com nota {notas[i]}.")


numeros = [9,7,3,5,2,1,8,6,0,4]

#Ex1
pares = 0
for num in numeros:
    if num % 2 == 0:
        pares += 1
#Ex1 met2
pares = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares += 1


#Ex2
soma = 0
for num in numeros:
    soma += num
print(soma)

#Ex2 met2
soma = 0
for i in range(len(numeros)):
    soma += numeros[i]
print(soma)
media = soma/len(numeros)

lista = []
lista.append(349)
print(lista)
lista.append(67)
print(lista)
lista.append(765)
print(lista)

#WHILE
lista = []
i = 0
while i <= 10
    num = input(f"Diga o {i+1}° número:")
    if not num.isnumeric:
        num = input(f"Diga o {i+1}° número")
        continue
    num = int(num)
    lista.append(num)
    i += 1
print(lista)


#FOR
lista = []
for i in range(10):
    num = input(f"Diga o {i + 1}° número:")
    while not num.isnumeric:
        num = input(f"Diga o {i + 1}° número")
        continue
    num = int(num)
    lista.append(num)
    print(lista)


lista = [7,3,8,5,2,0,9,6,10,4]

maior = lista[0]
for num in lista:
    print(f"Vou testar se {num} > {maior}")
    if num > maior:
        print(f"Deu certo, vou trocar {maior} por {num}")
        maior = num
print(f"O maior numero em {lista} é {maior}")


lista = [7,3,8,5,2,0,9,6,10,4]
indice_maior = 0
maior = lista[0]
for i in range(len(lista)):
    print(f"Vou testar se {lista[i]} > {maior}")
    if lista[i] > maior:
        print(f"Deu certo, vou trocar {maior} por {lista[i]}")
        maior = lista[i]
        indice_maior = i
print(f"O maior numero em {lista} é {maior}")
'''

preco = [600,50,80,1000000,5]
carros = ['Mustang','Up','gol','Polinho turbão manual','uno']
indice_maior = 0
maior = preco[0]
for i in range(len(preco)):
    #print(f"Vou testar se {lista[i]} > {maior}")
    if preco[i] > maior:
        #print(f"Deu certo, vou trocar {maior} por {lista[i]}")
        maior = preco[i]
        indice_maior = i
print(f"O carro mais caro é o {carros[indice_maior]}")