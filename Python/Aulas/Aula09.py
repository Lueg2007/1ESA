'''
def verifica_numero(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero

qtd = verifica_numero(f"Quantos números você vai colocar na lista?\n-> ")
print(qtd)
#ano = verifica_numero(f"Diga o seu ano de nascimento\n-> ")
lista = []
while len (lista) < qtd:
    num = input(f"Diga o {len(lista)+1}º número: ")
    while not num.isnumeric():
        num = input(f"Diga o {len(lista) + 1}º número: ")
    num = int(num)
    lista.append(num)
    print(lista)

#----------------------------------------------------

def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes) #unir elas em 1 string e separá-las por um caracter, por exemplo a vírgula ou o \n
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in lista_opcoes:
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

vinhos = ['Pérgola','Sangue de Boi','Salton']
vinho = forca_opcao("Qual vinho você quer? ", vinhos)
print(f"Você escolheu o {vinho}")
opcoes = ['s','n']
continuar = forca_opcao("Você quer continuar? (s/n)\n->", opcoes)
print(f"Você disse {continuar}")

#----------------------------------------------------
#CALCULA A MÉDIA DOS NÚMEROS
def acha_media(lista_numeros): #É o coringa
    print(lista_numeros)
    soma = 0
    for num in lista_numeros:
        soma += num
    media = soma/len(lista_numeros)
    return media

lista = [5,1,8,7,2,3]
media = acha_media(lista)
print(media)
lista_2 = [1,2,3]
media = acha_media(lista_2)
print(media)

#def soma_div (soma, calculo_media):
#    media = '\n'. join(calculo_media)
#lista = [7, 2, 5, 3, 8, 10]

#----------------------------------------------------
#CALCULA A QUANTIDADE DE PARES

def acha_pares(lista_numeros): #É o coringa
    pares = 0
    for num in lista_numeros:
        if num % 2 == 0:
            pares += 1
    return pares

lista = [5,1,8,7,2,3]
pares = acha_pares(lista)
print(f"Existem {pares} números pares na lista")
lista_2 = [1,2,3]
pares = acha_pares(lista_2)
print(f"Existem {pares} números pares na lista")

#----------------------------------------------------
#MAIOR ELEMENTO DA LISTA

def acha_maior(lista): #É o coringa
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior
carros = ['up','gol','polinho turbão manual','uno','celta']
precos = [10,20,1000000,100,200]
local_maior = acha_maior(precos)
print(local_maior)

#----------------------------------------------------
#OBRIGAR O USUÁRIO A ESCOLHER UM CARRO E MOSTRAR O PREÇO

def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in lista_opcoes:
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha
def acha_index(lista,elem):
    for i in range(len(carros)):
        if lista[i] == elem:
            return i
carros = ['up','gol','polinho turbão manual','uno','celta']
precos = [10,20,1000000,100,200]

escolha = forca_opcao("Qual carro te interessa?", carros)
indice_escolha = acha_index(carros,escolha)
print(f"O {escolha} custa {precos[indice_escolha]}")
'''

#----------------------------------------------------
#SOMAR OS CARACTERES COM O JOIN

def join(lista_str,sep):
    ajuntado = lista_str[0]
    for i in range(1,len(lista_str)):
        ajuntado += sep + lista_str[i]
    return ajuntado

def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in lista_opcoes:
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

def acha_index(lista,elem):
    for i in range(len(carros)):
        if lista[i] == elem:
            return i
carros = ['up','gol','polinho turbão manual','uno','celta']
precos = [10,20,1000000,100,200]

escolha = forca_opcao("Qual carro te interessa?", carros)
indice_escolha = acha_index(carros,escolha)
print(f"O {escolha} custa {precos[indice_escolha]}")