'''
15 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero.
'''

candidato_1 = candidato_2 = candidato_3 = candidato_4 = branco = nulo = 0

while True:
    voto = input("\n1 Bolsonaro"
                     "\n2 Lula"
                     "\n3 Dilma"
                     "\n4 Luigi"
                     "\n5 Branco"
                     "\n6 Nulo"
                     "\n Digite uma das opções acima:")
    while not voto.isnumeric():
        voto = input("\n1 Bolsonaro"
                     "\n2 Lula"
                     "\n3 Dilma"
                     "\n4 Luigi"
                     "\n5 Branco"
                     "\n6 Nulo"
                     "\n Digite uma das opções acima:")

    voto = int(voto)

    if voto == 1:
        candidato_1 += 1

    elif voto == 2:
        candidato_2 += 1

    elif voto == 3:
        candidato_3 += 1

    elif voto == 4:
        candidato_2 += 1

    elif voto == 5:
        branco += 1

    elif voto == 6:
        nulo += 1

    else:
        print("Digite um valor entre 1 a 6")

    