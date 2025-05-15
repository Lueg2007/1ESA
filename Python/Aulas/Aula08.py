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
'''
profs = ['Danilo','André','Gabi','Yan','Lucas','Luís']
materias = ['Python','Historinha','Sw&TX','Matemática','Edge','Front','Web']
for i in range(len(profs)):
    print(f"O/A {profs[i]} dá a materia de {materias[i]}.")
