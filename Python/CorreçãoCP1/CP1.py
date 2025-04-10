print("Seja bem-vindo à Vinheria Agnello!!!!")
ano = int(input("Diga o seu ano de nascimento: "))
endereco = input("Diga seu endereço: ")
idade = 2025 - ano
if idade < 18:
    print("Você não pode comprar nada aqui, adeus!")
else:
    vinho1 = 'Pérgola'
    vinho2 = 'Branco'
    vinho3 = 'Tinto'
    preco1 = 50
    preco2 = 30
    preco3 = 10
    escolha = input(f"Esses são nossos vinhos: \n{vinho1} - {preco1} "
                    f"\n{vinho2} - {preco2}\n{vinho3} - {preco3}"
                    f"\nQual você quer?\n->")
    qtd = int(input(f"Quantas garrafas de {escolha} você quer?\n->"))
    if escolha == vinho1:
        preco = preco1
    elif escolha == vinho2:
        preco = preco2
    else:
        preco = preco3
    total = qtd*preco
    frete = 10
    if total > 100:
        frete = 0
        print ("Frete grátis!")
    total = frete
    print(f"Obrigado pela preferência, o valor total foi de {total} e será entregue em {endereco}")