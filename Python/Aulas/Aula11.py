import matplotlib.pyplot as plt

# REVISANDO A AULA PASSADA

'''matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matriz[0])
print(type(matriz[0]))
print(matriz[0][3])
print(matriz[2][1])

print('----------------------------------------------------')

# fixa a linha na 0 e percorre todas as colunas e dps a linha +1
def elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'matriz[{i}][{j}] = {matriz[i][j]}')
    return

# funcao q mostrar cada linha da funcao
def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(0) # se for lista.append(i) a 1º linha = 0 a 2º = 1 e assim por diante
        matriz.append(lista)
    return matriz

def plotar_matriz(matriz):
    plt.imshow(matriz)
    plt.colorbar()
    plt.show()
    return

imagem = cria_matriz(10, 10)
mostrar_matriz(imagem)
plotar_matriz(imagem)


print('----------------------------------------------------')

# DIAGONAL
def elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'matriz[{i}][{j}] = {matriz[i][j]}')
    return

# funcao q mostrar cada linha da funcao
def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(0)
        matriz.append(lista)
    return matriz

def plotar_matriz(matriz):
    plt.imshow(matriz)
    plt.colorbar()
    plt.show()
    return

matriz = cria_matriz(10, 10)
for i in range(len(matriz)):
    for j  in  range(len(matriz[0])):
        if i == j:
            matriz[i][j] = 1  # poderia colocar matriz[i][i] pq se o i = j é a msm coisa de matriz[i][i]
plotar_matriz(matriz)

print('----------------------------------------------------')

# MSM FUNCAO DA ANTERIOR SO Q MODIFICOU AS LINHAS 77 A 80 DA ANTERIOR 
def elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'matriz[{i}][{j}] = {matriz[i][j]}')
    return

# funcao q mostrar cada linha da funcao
def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(0)
        matriz.append(lista)
    return matriz

def plotar_matriz(matriz):
    plt.imshow(matriz)
    plt.colorbar()
    plt.show()
    return

matriz = cria_matriz(10, 10)
for i in range(len(matriz)):
    matriz[i][i] = 1
plotar_matriz(matriz)'''

print('----------------------------------------------------')

# CONTRA DIAGONAL
def elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'matriz[{i}][{j}] = {matriz[i][j]}')
    return

# funcao q mostrar cada linha da funcao
def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(0)
        matriz.append(lista)
    return matriz

'''def plotar_matriz(matriz):
    plt.imshow(matriz)
    plt.colorbar()
    plt.show()
    return
'''
matriz = cria_matriz(10, 10)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i + j == len(matriz) - 1: # o 9 representa o n, e o n == nº de linhas ou colunas - 1
            matriz[i][j] = 1
'''plotar_matriz(matriz)'''

# MELHOR JEITO

matriz = cria_matriz(10, 10)
for i in range(len(matriz)):
    matriz[i][len(matriz) - i - 1] = 1
'''plotar_matriz(matriz)'''

print('----------------------------------------------------')

#
def elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'matriz[{i}][{j}] = {matriz[i][j]}')
    return

# funcao q mostrar cada linha da funcao
def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        lista = []
        for j in range(colunas):
            lista.append(0)
        matriz.append(lista)
    return matriz

def plotar_matriz(matriz):
    plt.imshow(matriz)
    plt.colorbar()
    plt.show()
    return

matriz = cria_matriz(10, 10)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i %2 == 0:
            if j %2 == 0:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1
        else:
            if j %2 != 0:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1

'''plotar_matriz(matriz)'''

'''-------MELHOR JEITO XADREZ--------'''
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i%2 == j%2:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 1

'''plotar_matriz(matriz)'''

matriz = cria_matriz(10,10)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if j>i:
            matriz[i][j] = 1
        elif j==i:
            matriz[i][j] = 2

'''plotar_matriz(matriz)'''

'''-------MATRIZ TRANSPOSTA--------'''


def transposta_boa(matriz):
    for i in range(len(matriz)):
        print(matriz[i][j])
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return

plotar_matriz(matriz)


'''--------INVERSÃO DE LISTA--------'''

def superior_bom(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz[0])):
            matriz[i][j] = 1
    return
plotar_matriz(matriz)