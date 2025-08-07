#EX 2
nome = input("Digite o seu nome:")
while len(nome) < 3:
    nome = input("Digite o seu nome:")

idade = int(input("Digite a sua idade:"))
while idade > 150 or idade < 0:
    idade = int(input("Digite a sua idade:"))

salario = int(input("Digite o seu salário:"))
while salario <= 0:
    salario = int(input("Digite o seu salário:"))

sexo = input("Digite o seu sexo (f - feminino e m - masculino)")
while sexo != "f" and sexo != "m":
    sexo = input("Digite o seu sexo (f - feminino e m - masculino)")

EstCiv = input("Digite o seu estado civil [s / c / v / d]:")
while not(EstCiv == 's' or EstCiv == 'v' or EstCiv == 'c' or EstCiv == 'd'):
    EstCiv = input("Digite o seu estado civil [s / c / v / d]:")


#EX 6
nome = input("Diga o seu nome:")
senha = input("Cadastre sua senha:")
while senha == nome:
    print("Senha e nome de usuário nao podem ser iguais!")
    nome = input("Diga o seu nome:")
    senha = input("Cadastre sua senha:")


#EX 7