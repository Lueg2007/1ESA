'''
2- Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

nome = input("Qual é o seu nome?")
while len(nome) < 3:
    nome = input("Qual é o seu nome?")

while True:
    idade = input("Agora, digite a sua idade:")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        else:
            print("Idade fora do intervalo válido (1 a 149). Tente novamente.")
    else:
        print("Não é um número, por favor, digite novamente.")
        