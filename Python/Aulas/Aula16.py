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

acha_raiz(25)