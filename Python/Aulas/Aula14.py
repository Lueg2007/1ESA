import requests
'''a = [i**2 for i in range(10)]
print(a)'''

acougue = {
    'Carnes' : ['Patinho','Coxão Mole','Fraldinha','Picanha','Maminha','LINGUIÇA'],
    'Preço/kg' : [35.90,49.90,39.90,80.00,45.90,15.00],
    'Estoque' : [10,50,30,15,20,100],
    'Validade' : ['4','7','5','9','20','50'],
}

def forca_opcao(msg,lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    opcao = input(f"{msg}\n{opcoes}\n->")
    while not opcao in lista_opcoes:
        opcoes = '\n'.join(lista_opcoes)
        opcao = input(f"{msg}\n{opcoes}\n->")
    return opcao

def cadastrar():
    global indices
    for key in acougue.keys():
        info = input(f"Diga o novo {key}: ")
        acougue[key].append(info)
    indices = cria_indices()
    return

def cria_indices():
    indices = {acougue['Carnes'][i] : i for i in range(len(acougue['Carnes']))}
    '''indices = {}
    for i in range(len(acougue['Carnes'])):
        indices[acougue['Carnes'][i]] = i
    '''
    return indices

def remover():
    global indices
    item = forca_opcao("Qual item será removido?",acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys(): #Passa por todas as linhas do meu dic
        acougue[key].pop(indice_item)
    return item

def atualizar():
    item = forca_opcao("Qual item você deseja atualizar?",acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        if forca_opcao(f"Você quer atualizar {key} para {item}?",['sim','não']) == 'sim':
            info = input(f"Diga o novo {key}: ")
            acougue[key][indice_item] = info
    return

'''indices = cria_indices()
atualizar()
print('-'*20)
cadastrar()
print('-'*20)
remover()'''

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def comprar():
    item = forca_opcao("Qual item você quer comprar?",acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        print(f"{key} : {acougue[key][indice_item]}")
    continuar = forca_opcao(f"Você quer levar {item}?",['sim','não'])
    if continuar == 'não':
        return
    qtd = verifica_numero(f"Quantos kg de {item}?")
    if qtd <= acougue['Estoque'][indice_item]:
        carrinho['valor Total'] += qtd * acougue['Preço/kg'][indice_item]
        if item not in carrinho['Itens'].keys():
            carrinho['Itens'][item] = qtd
        else:
            carrinho['Itens'][item] += qtd
    else:
        print(f"Só há {acougue['Estoque'][indice_item]} kg no estoque!")
        comprar()
    return


indices = cria_indices()
carrinho = {
    "Endereço" : {
        "Rua" : '',
        "Bairro" : '',
        "Número" : '',
        "Cep" : '',
    },
    "Itens" : {},
    "valor Total" : 0
}
def cadastro_endereco():
    while True:
        cep = input("Diga o seu cep: ")
        endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if endereco.status_code == 200:
            carrinho['Endereço'] = endereco.json()
            carrinho['Endereço']['N'] = input("Número da residência: ")
            carrinho['Endereço']['Complemento'] = input("Complemento:")
            break
        else:
            print("Cep inválido")
    return

cadastro_endereco()
comprar()
print(carrinho)


for key in carrinho['Endereço'].keys():
    info = input(f"Diga o/a {key}: ")
    carrinho['Endereço'][key] = info
print(carrinho)

print("Bem vindo à vinheria Agnello!!!")
usuario = forca_opcao("Você é cliente ou usuário?", ['cliente','funcionário'])
while True:
    if usuario == 'funcionário':
        operacao = forca_opcao("Qual operação será realizada?",['cadastrar','remover','atualizar'])
        if operacao == 'cadastrar':
            cadastrar()
        elif operacao == 'remover':
            remover()
        else:
            atualizar()
        continuar = forca_opcao("Você deseja realizar outra operação?",['sim','não'])
        if continuar == 'não':
            break
    else:
        comprar()
        encerrar = forca_opcao("Encerrar a compra ou ver mais itens?",['encerrar','continuar'])
        if encerrar == 'encerrar':
            print(f'Você vai levar\n{list(carrinho["Itens"].keys())[0]} na {carrinho["Endereço"]["logradouro"]}')
            print(carrinho)
            break