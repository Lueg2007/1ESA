//Obter referências aos botões do tema e da página
const botaoClaro = document.getElementById('temaClaro');
const botaoEscuro = document.getElementById('temaEscuro');
const body = document.body;

//define uma chave para armazenar a preferência do tema no LocalStorage
const chaveTema = 'preferênciaTema';

//Função para aplicar um tema específico ao corpo da página

function aplicarTema(tema){
    body.classList.remove('tema-claro','tema-escuro');
    body.classList.add(`tema-${tema}`)
    //Salva a preferência do tema no LocalStorage
    localStorage.setItem(chaveTema,tema);
}

//Verificar se já existe uma preferência de tema salva no LocalStorage ao carregar a página
const temaSalvo = localStorage.getItem(chaveTema);

if(temaSalvo){
    aplicarTema(temaSalvo);
}else{
    aplicarTema('claro');
}

//adiciona um evento de clique ao botão 'Claro'
botaoClaro.addEventListener('click', ()=>{
    //quando o botão for clicado, chama a função para aplicar o tema claro.
    aplicarTema('claro');
});

//adiciona um evento de clique ao botão 'Escuro'
botaoEscuro.addEventListener('click', ()=>{
    //quando o botão for clicado, chama a função para aplicar o tema escuro.
    aplicarTema('escuro');
});