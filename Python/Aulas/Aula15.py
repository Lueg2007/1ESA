import requests

# --- DIC DO AÇOUGUE E CARRINHO ---
acougue = {
    'Carne': ['Patinho', 'Picanha', 'Coxão Mole', 'Maminha', 'Fraldinha', 'Linguiça'],
    'Preço/kg': [35.9, 80.00, 24.78, 50.00, 49.85, 15],
    'Estoque': [10, 50, 30, 15, 20, 100],
    'Validade': ['4', '7', '5', '9', '20', '50']
}

carrinho = {
    'Endereço': {'Rua': '',
                 'Bairro': '',
                 'Nº': '',
                 'CEP': ''
                 },
    'Itens': {},
    'Valor Total': 0
}


# --- FUNÇOES Q GERAIS PARA AJUDAR AS OUTRAS FUNÇÕES ---
def forca_opcao(msg, listaOpcoes):
    msg += '\n' + ' --- '.join(listaOpcoes) + '\n->'
    opcoes = input(msg)
    while opcoes not in listaOpcoes:
        opcoes = input(msg)
    return opcoes


def cria_indice():
    indices = {}
    for i in range(len(acougue['Carne'])):
        indices[acougue['Carne'][i]] = i
    return indices


def verificaNum(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)


# ----- FUNÇÕES PARA O FUNCIONARIO -----
def cadastrar_produto():
    global indices
    for key in acougue.keys():
        if key in ['Preço/kg', 'Estoque']:
            while True:
                try:
                    info = float(input(f'Diga o novo/a {key}: '))
                except:
                    print('Tem que ser float')
                else:
                    acougue[key].append(info)
                    break
            continue
        info = float(input(f'Diga o novo/a {key}: '))
        acougue[key].append(info)
    indices = cria_indice()
    return


def remover():
    global indices  # n qro q essa variavel seja local
    item = forca_opcao('Diga qual carne vc quer excluir: ', acougue['Carne'])
    indice_item = indices[item]
    for key in acougue.keys():
        acougue[key].pop(indice_item)
    indices = cria_indice()
    return


def atualizar():
    item = forca_opcao('Qual item vc deseja atualizar?', acougue['Carne'])
    indice_item = indices[item]
    keys = list(acougue.keys())
    keys.pop(0)
    for key in keys:
        if forca_opcao(f'Qr atualizar {key} para {item}? ', ['sim', 'não']) == 'sim':
            info = input(f'Diga o novo/a {key}: ')
            acougue[key][indice_item] = info
        return


# ----- FUNÇOES DO CLIENTE -----
def comprar():
    item = forca_opcao('Qual item vc deseja? ', acougue['Carne'])
    indice_item = indices[item]
    for key in acougue.keys():
        print(f'{key}: {acougue[key][indice_item]}')
        cont = forca_opcao(f'Vc qr levar {item}? ', ['sim', 'nao'])
        if cont == 'nao':
            return
    qtd = verificaNum(f'Qnts kg de {item} vc quer? ')
    if qtd <= acougue['Estoque'][indice_item]:
        acougue['Estoque'][indice_item] -= qtd
        carrinho['Valor Total'] += qtd * acougue['Preço/kg'][indice_item]
        if item not in carrinho['Itens'].keys():
            carrinho['Itens'][item] = qtd
        else:
            carrinho['Itens'][item] += qtd
    else:
        print(f'So ha {acougue['Estoque'][indice_item]}kg no estoque')
        comprar()
    return


def confirmarCompra():
    print('Essas sao as informacoes da sua compra: ')
    print(carrinho)
    alterar = forca_opcao('Qr remover um item: ', ['Sim', 'Não'])
    if alterar == 'Sim':
        item = forca_opcao('Qual item vc irá remover? ', carrinho['Itens'].keys())
        indice = indices[item]
        qtd = verificaNum(f'Qnts kg de {item} serã removidos? ')
        if qtd <= carrinho['Itens'][item]:
            carrinho['Itens'][item] -= qtd
            carrinho['Valor Total'] -= qtd * acougue['Preço/kg'][indice]
        else:
            print(f'Não é possivel remover esse tanto pois so ha {carrinho['Itens'][item]}kg')
        confirmarCompra()
    return


def cadastro_endereco():
    while True:
        # PELO CEP VAI BUSCAR O SEU ENDEREÇO USANDO O JSON
        cep = input('Diga seu cep: ')
        endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if endereco.status_code == 200:
            carrinho['Endereço'] = endereco.json()
            carrinho['Endereço']['Nº'] = input('Numero da residencia: ')
            carrinho['Endereço']['Complemento'] = input('Complemento: ')
            break
        else:
            print('Cep invalido')
    return


# PARA TIRAR OS IF ELSE DENTRO DO WHILE TRUE
acoes = {
    'cadastrar': cadastrar_produto,
    'remover': remover,
    'atualizar': atualizar
}

indices = cria_indice()

# --- CODIGO PRINCIPAL ---
print('----- Bem vindo a Açougueria Agnello!!! 🍖 -----')
usuario = forca_opcao('Vc é ', ['cliente', 'funcionario'])
if usuario == 'cliente':
    cadastro_endereco()
while True:
    if usuario == 'funcionario':
        operacao = forca_opcao('Qual operacao sera realizada? ', acoes.keys())
        acoes[operacao]()
        cont = forca_opcao('Vc qr realizar outra operacao? ', ['sim', 'não'])
        if cont == 'nao':
            break
    else:
        comprar()
        confirmarCompra()
        encerrar = forca_opcao('Encerrar ou ver mais itens? ', ['encerrar', 'continuar'])
        if encerrar == 'encerrar':
            print(f'Vc vai levar {list(carrinho['Itens'].keys())} na {carrinho['Endereço']['logradouro']}')
            print(carrinho)
            print('Obrigado pela visita 😊')
            break

