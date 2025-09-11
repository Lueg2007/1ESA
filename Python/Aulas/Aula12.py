'''dic = {'chave':'valor'} #não permite repetição e a chave sempre será o da esquerda
print(dic['chave'])
dic['nova chave'] = 'novo valor'
print(dic)
dic['chave'] = '123'
print(dic)

import random
saudacoes = {
    'oi':['ola','SALVE','iae','BÃO uai'], #Vai randomizar alguma dessas mensagens pré programadas
    'tchau':['flw','tchau migo','bjssssss diva','até mais']
}
while True:
    resposta = input("Diga oi ou tchau:")
    print(random.choice(saudacoes[resposta]))

    if resposta == 'oi':
        print("Olá")
    else:
        print('flw')


#NUMERO ALEATORIO Logisitc equation, ruido/modelo atmosférico

#EXERCICIO POLIGONOS
geometria = {
    '3':['Triângulo'] ,
    '4':['Quadrado'] ,
    '5':['Pentágono'] ,
    '6':['Hexágono']
}
while True:
    resposta = input("Diga o número de lados:")
    print(f"Você escolheu um {geometria[resposta]}.")
    break

emojis = {
    ':)':'😊' ,
    ':(':'😔' ,
    '<3':'❤️' ,
    ":'(":'🥲'
}
texto = 'Eu amo python <3'
for key in emojis.keys():
    texto = texto.replace(key,emojis[key]) #emojis[key] = Substitua o antigo pelo novo, ou seja <3 por ❤️#uma variável de um conjunto de coisas, pega o conjunto de chaves do dicionário e substitui
print(texto)#Exemplo: o "<3" vai virar "❤️"


#Nove = chave
#9 = valor
#Procura a chave no texto para substituir o valor


#EXERCICIO TELEFONE

telefone = {
    'um':'1' ,
    'dois':'2' ,
    'três':'3' ,
    'quatro':'4' ,
    'cinco':'5' ,
    'meia':'6' ,
    'seis':'6' ,
    'sete':'7' ,
    'oito':'8' ,
    'nove':'9' ,
    'onze':'11'
}
numero = 'onze nove meia três três quatro nove seis quatro nove'
for key in telefone.keys():
    numero = numero.replace(key,telefone[key])
print(numero)
numero = numero.replace(' ','') #Apagar os espaços entre os números
print(f"O número de telefone é {numero}.")



dic = {
    'nome' : ['Luigi','Giovanna','Japa'],
    'idade' : ['18','16','15']
}
for i in range(len(dic['nome'])):
    for key in dic.keys():#Cria um conjunto de chaves dentro do dicionário
        print(f"{key} : {dic[key][i]}")#para passar cada linha mostrando as chaves respectivas
    print()#Só para não ficar grudado


#Bag of words

frase = "A aranha arranha a rã. a rã arranha a aranha. nem a aranha arranha a rã. Nem a rã arranha a aranha"
print(frase)
frase = frase.lower()
print(frase)
frase = frase.replace('.','')
print(frase)
palavras = frase.split(' ')#Split = separe conforme com um caracter; join é o contrário
print(palavras)
contador = {',l;jsd'} = 1 #elemento da lista é a chave do dicionário
'''

frase = "A aranha arranha a rã. a rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha"
frase = frase.lower()
frase = frase.replace('.','')
palavras = frase.split(' ')

contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra]+=1
    else:
        contador[palavra] = 1 #Revisar isso #verifica se ja é uma chave do dicionario, se não for, tenho que associar ela ao numero 1 porque é a primeir avez q a palavra aparece
print(contador)