'''
idoso = input("Você é idoso?\n->")
cartãozinho = input("Você tem cartãozinho?")
if idoso == 'sim' and cartãozinho == 'sim':
    print("Pode estacionar!")
else:
    print("Não pode estacionar!")

idoso = input("Você é idoso?\n->")
deficiente = input("Você é deficiente?\n->")
if idoso == 'sim' or deficiente == 'sim':
    print("Pode estacionar!")
else:
    print("Não pode estacionar!")
'''
'''
letra = (input("Escolha uma letra:"))
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"{letra} é uma vogal!")
else:
    print(f"{letra} é uma consoante!")

time = input("Diga para que time você torce: ")
if time == 'São Paulo':
    print("Bambi, queima a rosca, filho do corinthians!")
elif time == 'Palmeiras':
    print("Maior do Brasil, primeiro campeão mundial, 4 copas do Brasil, 3 liberta, 14 campeonatos brasileiros, pai do corinthians")
elif time == 'Corinthians':
    print("Rebaixado, favelado, cheio de dívida, nunca vai ser maior que o Palmeiras")
elif time == 'Santos':
    print("Rei Pelé, ta em crise, prabéns pela série B, Neymar é foda")

s = float(input("Qual a faixa do seu salário?:"))
if s <= 1903:
 print("Nada é descontado!")
elif s > 1903 and s <= 2826:
    taxa = (s * 7.5) / 100
    novo_s = (s - taxa)
    print(f"A taxa é de R${taxa} e seu novo salário é de {novo_s}")
elif s > 2826 and s <= 3751:
    taxa = (s * 15) / 100
    novo_s = (s - taxa)
    print(f"A taxa é de R${taxa} e seu novo salário é de {novo_s}")
elif s > 3751 and s <= 4664:
    taxa = (s * 22.5) / 100
    novo_s = (s - taxa)
    print(f"A taxa é R${taxa} e seu novo salário é de {novo_s}")
else:
    taxa = (s * 27.5) / 100
    novo_s = (s - taxa)
    print(f"A taxa é R${taxa} e seu novo salário é de {novo_s}")
    

s = float(input("Qual a faixa do seu salário?:"))
if s <= 1903:
    print("Nada é descontado!")
elif s > 1903 and s <= 2826:
    taxa = (s * 7.5) / 100
    novo_s = (s - taxa)
    print("A taxa é de R${:.2f} e seu novo salário é de {:.2f}".format(taxa, novo_s))
elif s > 2826 and s <= 3751:
    taxa = (s * 15) / 100
    novo_s = (s - taxa)
    print("A taxa é de R${:.2f} e seu novo salário é de {:.2f}".format(taxa, novo_s))
elif s > 3751 and s <= 4664:
    taxa = (s * 22.5) / 100
    novo_s = (s - taxa)
    print("A taxa é R${:.2f} e seu novo salário é de {:.2f}".format(taxa, novo_s))
else:
    taxa = (s * 27.5) / 100
    novo_s = (s - taxa)
    print("A taxa é R${:.2f} e seu novo salário é de {:.2f}".format(taxa, novo_s))
'''

nome = input(f"Diga o seu nome:")
print(f"Prazer {nome}, bem vindo à calculadora!")
a = float(input("Diga um número:"))
b = float(input("Diga outro número:"))
opcao = input("Qual operação você gostaria de fazer?\nsoma\nsubtraçâo\ndivisão\nmultplicação")
if opcao == 'soma':
    print(f"{a} + {b} = {a + b}")
elif opcao == 'subtração':(
    print(f"{a}-{b} = {a - b}"))
elif opcao == 'divisão':(
    print(f"{a}/{b} = {a / b}"))
elif opcao == 'multiplicação':(
    print(f"{a}*{b} = {a * b}"))
else:
    print("Opção inválida. Por favor, escolha uma operação válida.")