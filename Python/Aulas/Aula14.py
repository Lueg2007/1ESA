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
    for key in acougue.keys():
        info = input(f"Diga o novo {key}: ")
        acougue[key].append(info)
    return

def cria_indices():
    indices = {acougue['Carnes'][i] : i for i in range(len(acougue['Carnes']))}
    '''indices = {}
    for i in range(len(acougue['Carnes'])):
        indices[acougue['Carnes'][i]] = i
    '''
    return indices

def remover():
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
indices = cria_indices()
atualizar()
print('-'*20)
cadastrar()
print('-'*20)
remover()

'''a = [i**2 for i in range(10)]
print(a)'''
