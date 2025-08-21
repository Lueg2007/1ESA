import matplotlib.pyplot as plt
'''
matriz = [[1,2,3,4], [4,5,6,7], [7,8,9,10]] #cada sublista é uma linha, a quantidade de sublista determina o número de linhas
plt.imshow(matriz, 'hot')
plt.colorbar()
plt.show()

matriz = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]
print(matriz[0])
print(type(matriz[0]))
print(matriz[0][2]) #Primeiro escolhe a sublista que você quer, depois o elemento dessa sublista


#PRINT DE CADA NÚMERO INDIVIDUALMENTE

matriz = [[1,2,3,4], [4,5,6,7], [7,8,9,10]] #3 linhas e 4 colunas
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")

matriz = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]

linhas = 3
colunas = 4

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(1)
    matriz.append(linha)
    print(matriz)

#FAZER UMA MATRIZ COM DEF QUE RETORNE
def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(i+j)
        matriz.append(linha)
    return matriz

a = cria_matriz(50, 50)
mostra_matriz(a)
plt.imshow(a,'hot')
plt.colorbar()
plt.show()


#DIAGONAL
def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

diagonal = cria_matriz(10, 10)
for i in range(len(diagonal)):
    for j in range(len(diagonal[0])):
        if i == j:
            diagonal[i][j] = 1

        for i in range(len(diagonal)):
            diagonal[i][i] = 1
plt.imshow(diagonal,'hot')
plt.colorbar()
plt.show()
'''
#XADREZ

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

'''
xadrez = cria_matriz(8, 8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i %2 == 0:
            if j %2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j %2 != 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
'''

#CÍRCULO

circulo = cria_matriz(1000, 1000)
raio = len(circulo)/2
for i in range(len(circulo)):
    for j in range(len(circulo[0])):
        if (i-raio)**2 + (j-raio)**2 <= raio ** 2:
            circulo[i][j] = i
        else:
            circulo[i][j] = 0

plt.imshow(circulo,'hot')
plt.colorbar()
plt.show()