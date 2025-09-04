'''EXERCICIO 1'''

matriz = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]

def elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return matriz
def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

matriz = mostra_matriz(matriz)
matriz = elementos_matriz([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

'''EXERCICIO 2'''
def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz
matriz = cria_matriz(10,10)
matriz = mostra_matriz(matriz)

def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

'''EXERCICIO 3'''
def cria_diagonal(matriz):
    for i in range(len(matriz)):
        matriz [i][i] = 1
    return

def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def mostra_matriz(linha):
    for linha in matriz:
        print(linha)

'''EXERCICIO 4'''

def cria_contradiagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz)-i-1] = 1

def cria_matriz(linhas,colunas):
    matriz = []
    for i  in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def mostra_matriz(linha):
    for linha in matriz:
        print(linha)
    return

'''EXERCICIO 5'''


def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def mostra_matriz(linha):
    for linha in matriz:
        print(linha)
    return

def cria_triangulo(matriz):
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            matriz[i][j] = 1
            matriz[j][i] = 2
        return



matriz = cria_matriz(10,10)
matriz = mostra_matriz(matriz)

'''EXERCICIO 6'''

def matriz_transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return

matriz = cria_matriz(5,5)
mostra_matriz(matriz)

'''EXERCICIO 8'''

def cria_xadrez(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i %2 == j %2:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1
    return

'''EXERCICIO 9'''

def cria_ciruclo(matriz):
    raio = (matriz) / 2
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i-raio) ** 2 + (j-raio) ** 2 <= raio ** 2:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1
    return

'''EXERCICIO 10'''

def cria_xadrez(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i %2 == j %2:
                matriz[i][j] = "vago"
            else:
                matriz[i][j] = "ocupado"
    return