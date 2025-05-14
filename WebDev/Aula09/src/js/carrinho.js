const inputNovoItem = document.getElementById('novo-item');
const botaoAdicionar = document.getElementById('adicionar-ao-carrinho');
const listaDeItens = document.getElementById('lista-de-itens');

const chaveCarrinho = 'itensCarrinho';

function obterCarrinho(){
    const carrinhSalvo = sessionStorage.getItem(chaveCarrinho);
    return carrinhSalvo ? JSON.parse(carrinhSalvo) : [];
}

let carrinho = obterCarrinho();

exibirCarrinho();

function exibirCarrinho(){
    listaDeItens.innerHTML = '';

    carrinho.array.forEach(item => {
        const listaItem = document.createElement('li');
        listaItem.textContent = item;
        listaDeItens.appendChild(listaItem);
    });
}

botaoAdicionar.addEventListener('click', ()=>{
    const novoItem = inputNovoItem.value.trim();
    if(novoItem !== ''){
        carrinho.push(novoItem);
        sessionStorage.setItem(chaveCarrinho,JSON.stringify(carrinho));
        inputNovoItem.value = '';
        exibirCarrinho();
    }
})