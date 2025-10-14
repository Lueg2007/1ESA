lojaBrinquedos = {
    'Brinquedos': ['Carrinho de Controle Remoto', 'Boneca', 'Lego Star Wars', 'Urso de Pelúcia',
                   'Tabuleiro Banco Imobiliário', 'Bola de Futebol'],
    'Preço': [199.90, 89.99, 450.00, 120.00, 159.90, 79.90],
    'Idade Recomendada': [['6+', '8+', '10+'], ['3+', '5+'], ['8+', '10+', '12+'], ['3+', '5+'], ['7+', '10+'],
                          ['5+', '7+', '10+']],
    'Cor': [['Vermelho', 'Azul', 'Verde'], ['Rosa', 'Azul', 'Amarelo'], ['Multicolorido'], ['Marrom', 'Bege', 'Branco'],
            ['Multicolorido'], ['Branco', 'Preto', 'Azul']],
    'Estoque': [50, 120, 30, 200, 45, 80]
}

# --- DIC CARRINHO ---
carrinho = {
    'Endereço': {
        'Rua': '',
        'Bairro': '',
        'Nº': '',
        'CEP': ''
    },
    'Itens': {},
    'Valor Total': 0
}

acoes = {
    'Adicionar': add_item,
    'Remover': remover_item,
    'Atualizar': atualizar_item
}

def forca_opcao(msg , lista_opcoes):
    msg += "\n" + ",".join(lista_opcoes) + "\n" + "->"
    opcao = input(msg)
    while opcao not in lista_opcoes:
        opcao = input(msg)
    return opcao

def cria_indice():
    indice = {}
    for i in range(len(lojaBrinquedos['Brinquedos'])):
        indice[lojaBrinquedos['Brinquedos'][i]] = i
    return indice

def remover_item():
    global indice
    escolha = forca_opcao("Você deseja remover algum item?", lojaBrinquedos['Brinquedos'])
    indices = indice[escolha]
    for key in lojaBrinquedos.keys():
        lojaBrinquedos[key].pop(indices)
    indice = cria_indice()
    return

def add_item():
    for key in lojaBrinquedos.keys():
        if key in ['Preço', 'Estoque']:
            try:
                informacao = float(input(f"Diga o novo(a) {key}"))
            except:
                print("É necessário ser um valor númerico válido")
            else:
                lojaBrinquedos[key].append(informacao)
        informacao = input(f"Diga o novo(a) {key}")
        lojaBrinquedos[key].append(informacao)
    return

def atualizar_item():
    global indice
    escolha = forca_opcao("Qual brinquedo você deseja atualizar?", lojaBrinquedos["Brinquedos"])
    indices = indice[escolha]
    chaves = list(lojaBrinquedos.keys())
    chaves.pop(0)
    for key in chaves:
        if forca_opcao((f"Você quer atualizar o {key} de {escolha}?" , ["SIM","NÃO"])) == "SIM":
            novo = input(f"Diga o valor do(a) novo(a) {key}")
            lojaBrinquedos[key][indices] = novo
    return