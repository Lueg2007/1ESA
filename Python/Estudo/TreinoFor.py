'''
lista = [3, 'Luigi', 0.5, True]
#lista[0] = 3
#lista[1] = 'Luigi'
#lista[2] = 0.5
#lista[3] = True

for i in range(len(lista)): # viu um "i" -> sempre colocar um "in range(len())"
    print(f"lista[{i}] = {lista[i]}")

for elem in lista:
    print(elem)

lista = [4,1,5,7,3,6,9,2,10,8] #len = tamanho
soma = media = 0
for i in range(len(lista)):
    soma += lista[i]
media = soma/len(lista)
print(f"A soma é {soma} e a média é {media:.2f}")


lista = []
par = impar = 0
for i in range(10):
    num = input(f"Digite o {i + 1} número:")
    while not num.isnumeric:
        num = input(f"Digite o {i + 1} número:")
    num = int(num) #para repetir caso digite uma string e não quebre o código
    lista.append(num)

for i in range(len(lista)):
    if lista[i] %2 == 0:
        par += 1
    else:
        impar += 1
print(f"\n{lista}"
      f"\nO número de pares é {par} e de impares é {impar}.")

def acha_media(lista):
    soma = 0
    for num in numeros:
        soma += num
    media = soma/len(numeros)
    return media

def vinhos(msg,lista):
    opcoes = "\n".join(lista)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in lista:
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

listaVinhos = ['Tinto','LeRunito','Branco']
opcao = vinhos("Digite qual vinho você deseja:",listaVinhos)
'''

print("Boas vindas à vinheria Agnello")
idade = input("Diga a sua idade:")
while not idade.isnumeric():
    idade = input("Diga a sua idade:")
idade = int(idade)
if idade > 17:
    endereco = input("Qual é o seu endereço? ")
else:
    print("Você é menor de idade, não podemos vender nada à você, adeus.")

def vinhos(msg,lista1,lista2):
    opcoes = "\n".join(lista1)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in lista1 and lista2:
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

listaPreco = ['Mais Barato - R$20,00','Preço Médio - R$40,00','Mais Caro - R$60,00']
listaVinhos = ['Tinto','LeRunito','Branco']
opcao = vinhos("Digite qual vinho você deseja:",listaVinhos, listaPreco)
