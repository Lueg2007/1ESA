from fontTools.misc.cython import returns


def forca_opcao(msg,lista_opcoes):
    msg+= '\n' + '\n'.join(lista_opcoes) + '\n->'
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print("Erro!")
        opcao = input(msg)
    return(opcao)

def acha_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
def indice_maior(lista):
    indice_maior = 0
    for i in range(len(lista)):
        if lista[i] > lista[indice_maior]:
            indice_maior = [i]
    return(indice_maior)

def indice_menor(lista):
    indice_menor = 3
    for i in range(len(lista)):
        if lista[i] < lista[indice_menor]:
            indice_menor = [i]
    return(indice_menor)
'''
#1 – Modifique o seguinte Código para eliminar o uso de condicionais

dic = {
    'oi' : 'olá',
    'tchau' : 'flw'
}
resposta = input('Diga oi ou tchau: ')
print(dic[resposta])

#2 – Traga ao usuário todas as informações sobre um carro de sua escolha:
carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}
while True:
    pergunta = input("Digite o nome do carro:").lower()

    if pergunta in carros['nomes']: #Essa linha serve para achar a posição do carro em funçao de [i], indice do carro (começa em 0)
        i = carros['nomes'].index(pergunta) #i = o "numero" que o usuario escolheu, se escolher "Kombi", o i = 2 (porque começa em 0)

        for chave in carros.keys(): #pra cada coluna no meu armario(Dic: nome, portas, preço, ano), mostra o valor que está na linha i
            print(f"{chave} : {carros[chave][i]}")
        break
    else:
        print(f"{pergunta} não é um carro válido")

#3 – Use o dicionário do item anterior para trazer todas as informações sobre o carro mais caro
local_mais_caro = indice_maior(carros['preço'])
print('As infos sobre o carro mais caro são:')
for key in carros.keys():
    print(f"{key} : {carros[key][local_mais_caro]}")

#4 – Use o dicionário do item anterior para trazer todas as informações sobre o carro mais barato
local_mais_barato = indice_menor(carros['preço'])
print('As infos sobre o carro mais barato são:')
for key in carros.keys():
    print(f"{key} : {carros[key][local_mais_barato]}")

#5 – Pergunte ao usuário se ele gostaria de cadastrar um novo carro e implemente esta funcionalidade
for key in carros.keys():
    info = input(f"Diga o novo {key}:")
    carros[key].append(info)
print(carros)

#6 – Pergunte ao usuário se ele gostaria de remover um carro e implemente esta funcionalidade

remover = forca_opcao("Qual carro você que remover?", carros['nome'])
indice_remover = acha_indice(carros['nome'], remover)
for key in carros.key():
    carros[key].pop(indice_remover) #.pop = remover
print(carros)

atualizar = forca_opcao("Qual carro você deseja atualizar?",carros['nome'])
indice_atualizar = acha_indice(carros['nome'],atualizar)
for key in carros.keys():
    carros[key][indice_atualizar] = input(f"Diga o novo {key} do {atualizar}")


#7- Escreva um código capaz de contar a quantidade de vezes que uma palavra aparece numa frase, por exemplo:
#O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será.

frase = 'O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será.'
frase = frase.lower()
for char in ',.:;?!':
    frase = frase.replace(char,'')
print(frase)
palavras = frase.split(' ')
contador = {}
for palavra in palavras:
    if palavra not in contador.keys():
        contador[palavra] = 1
    else:
        contador[palavra] += 1


#8 – Escreva um código capaz de alterar números por extenso numa frase pelos caracteres correspondentes. Ex: Eu tenho aula na sala cinco zero dois -> Eu tenho aula na sala 502
numeros ={
    'zero' : '0',
    'dois' : '2',
    'cinco' : '5'
}
frase = 'Eu tenho aula na sala cinco zero dois'
for key in numeros.keys():
    frase = frase.replace(key+' ',numeros[key])
    frase = frase.replace(key, numeros[key])

print(frase)
'''


acougue = {
    'carne': ['Patinho', 'Coxão Mole', 'Fraldinha', 'Picanha', 'Maminha', 'LINGUIÇA'],
    'RS/kg': [35.90, 49.90, 39.90, 80.00, 45.90, 15],
    'estoque': [10, 50, 30, 15, 20, 100],
    'Validade': ['4', '7', '5', '9', '20', '50']
}
pergunta = input("Digite o nome da carne:").lower()

while True:
    nomes_lower = [nome.lower() for nome in acougue['carne']]

    if pergunta in nomes_lower:
        i = nomes_lower.index(pergunta)
        for chave in acougue.keys():
            print(f"{chave} : {acougue[chave][i]}")
        break
    else:
        print(f"{pergunta} não é uma carne válida")
        break
for key in acougue.keys():
    info = input(f"Diga um(a) novo(a) {key}:")
    acougue[key].append(info)
    print(acougue)