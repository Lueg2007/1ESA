'''#1 Modifique o seguinte Código para eliminar o uso de condicionais
resp = input("Diga oi ou tchau:")
dic = {'oi' : 'olá' ,
       'tchau' : 'falou'}
print(dic[resp])


#7 Escreva um código capaz de contar a quantidade de vezes que uma palavra aparece numa frase
"O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será."

#8 Escreva um código capaz de alterar números por extenso numa frase pelos caracteres correspondentes. Ex: Eu tenho aula na sala cinco zero dois -> Eu tenho aula na sala 502

frase = "Eu tenho aula na sala cinco zero dois"
numeros = {'zero' : '0',
           'dois' : '2',
           'cinco' : '5'}
for key in numeros.keys():
       frase = frase.replace(key+' ', numeros[key])
       frase = frase.replace(key, numeros[key])
print(frase)

#9- Dados dois dicionários, retorne uma lista com todas as chaves presentes em ambos.
'''


carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

def acha_indice(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def cria_indice():
    indices = {}
    for i in range(len(carros['nomes'])):
        indices[carros['nomes'][i]] = i
    return indices

def forca_opcao(msg, lista_opcoes):
    msg += '\n' + ','.join(lista_opcoes) + '\n ->'
    opcoes = input(msg)
    while opcoes not in lista_opcoes:
        opcoes = input(msg)
    return opcoes

def mostra_informacoes():
    global indices
    informacao = forca_opcao("Qual você quer?", carros['nomes'])
    indice = indices[informacao]
    for key in carros.keys():
        print(f"{key}: {carros[key][indice]}")
        indices = cria_indice()
    return

def adiciona_item():
    for key in carros.keys():
        adicionar = input(f"Adicione novo(a) {key}: ")
        carros[key].append(adicionar)
    return

def remover_item():
    global indices
    informacao = forca_opcao("Qual você quer remover?", carros['nomes'])
    indice = indices[informacao]
    for key in carros.keys():
        carros[key].pop(indice)
        indices = cria_indice()
    return

def atualizar_item():
    global indices
    informacao = forca_opcao("Qual você quer atualizar?", carros['nomes'])
    indice = indices[informacao]
    keys = list(carros.keys())
    keys.pop(0)
    for key in carros.keys():
        if forca_opcao(f"Você deseja atualizar {key} da {informacao}?", ["SIM" , "NÃO"]) == "SIM":
            novo = input(f"Atualize para o(a) novo(a) {key}:")
            carros[key][indice] = novo
            indices = cria_indice()
        return

indices = cria_indice()


trava_lingua = ("O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, "
                "um bom desconstantinopolitanizador será.").lower()
for char in ',.:?!; ':
    trava_lingua = trava_lingua.replace(char , '')

lista_palavras = trava_lingua.split(' ')

dic = {}
for palavra in lista_palavras:
    if palavra not in dic.keys():
        dic[palavra] = 1
    else:
        dic[palavra] += 1
print(dic)


