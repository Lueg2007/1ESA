'''#1 Modifique o seguinte Código para eliminar o uso de condicionais
resp = input("Diga oi ou tchau:")
dic = {'oi' : 'olá' ,
       'tchau' : 'falou'}
print(dic[resp])


#7 Escreva um código capaz de contar a quantidade de vezes que uma palavra aparece numa frase
"O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será."
'''
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