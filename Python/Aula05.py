'''
i = 0
pares = 0

while i < 10:
    num = int(input(f"Diga o {i+1}° número: "))
    if num%2 == 0:
        pares = pares + 1
    i = i + 1 #Esse espaçamento faz diferença, NÃO ESQUECER ESPAÇAMENTO!!!!

print(f"Você digitou {pares} números pares e {i - pares} números ímpares")
'''

senha = input("Digite a senha:")
while senha != '0702':
    if senha == '0702':
        print("Acesso Permitido!")
    else:
        print("Acesso Negado")
    senha = input("Digite a senha:")