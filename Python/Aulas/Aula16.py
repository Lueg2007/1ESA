def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

#CORREÇÃO

'''def ordena_lista(lista):
    ordenada = []
    qtd = len(lista)
    for i in range(qtd):
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
    return ordenada'''

#DEF DE CIMA COM AUX

lista = [3,1,5,6,2,4,7]
print(lista[2:1])
def ordena_lista(lista):
    for i in range(len(lista)):
        local_menor = indice_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[local_menor]
        lista[local_menor] = aux
        print (lista)

#NUMERO SECRETO
'''
def acha_raiz(num):
    while True:
        try:
            palpite = float(input(f"Dê o seu palpite para achar a raiz de {num} \n ->"))
        except:
            print("Utilize somente números")
        else:
            pot = palpite ** 2
        if pot > num:
            print("O palpite deve ser menor!")
        elif pot < num:
            print("O palpite deve ser maior!")
        else:
            print("O palpite está correto!")
            break
    return

acha_raiz(25)'''


def selection_sort_melhorzinho(lista):
    for i in range(len(lista)):
        ind = indice_menor(lista[i:]) + i #Pegue a lista e corte i elementos, passe a partir de i
        aux = lista[i]
        lista[i] = lista[ind]
        lista[ind] = aux
        print(lista)
        print()
    return
lista = [5,0,4,1,2,7,6,3]
selection_sort_melhorzinho(lista)
print(lista)

def bubble_sort(lista):
    for i in range(len(lista)):
        trocas = 0
        for j in range(len(lista) - i - 1): #o ultimo par é o ultimo com o penultimo, não existe sucessor, por isso o "-1"
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                trocas += 1
        if trocas == 0:
            break

    return

lista = [5,0,4,1,2,7,6,3]
bubble_sort(lista)
print( )





