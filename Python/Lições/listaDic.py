'''#1 – Modifique o seguinte Código para eliminar o uso de condicionais
import random
saudacoes = {
    'olá':['olá', 'eae', 'oi grazi', 'de boa?', 'eae chefe'] ,
    'tchau':['tchau', 'flw', 'flw viado', 'é nois', 'vlw']
}
while True:
    resposta = input('Diga "olá" ou "tchau":')
    print(random.choice(saudacoes[resposta]))'''

#2 – Traga ao usuário todas as informações sobre um carro de sua escolha:
carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}

pergunta = input("Digite o nome do carro:").lower()

if pergunta in carros['nome']:
    #Essa linha serve para achar a posição do carro em funçao de [i], indice do carro (começa em 0)

for i in range(len(carros['nomes'])):