const frutas = ['maçã', 'melancia', 'banana']; // forma de colocar um array

const numeros = [10, 20, 30, 40]; //tanto faz ser uma string ou valor númerico, ele ja vai estar considerando

const misturado = [1, 'dois', 3, 'quatro', true, null, undefined,{chave:'valor'}]; // pode colocar qualquer elemento no array, não precisa ser específico

const cores = new Array('vermelho', 'preto', 'branco'); // segunda forma para criar um array

const vazio = []; //também é possível criar um array sem nada dentro

const linguagens = ['javascript','java','python','c#'];

//Acessando o primeiro elemento do array
const primeiraLinguagem = linguagens[0];
console.log(`A primeira linguagem é; ${primeiraLinguagem}`);

const ultimaLinguagem = linguagens[linguagens.length-1];// 0,1,2,3, ou seja, smp vai começar com a posição 0 porque a posição 4 seria um quinto elemento e não temos ele
console.log(`A última linguagem é: ${ultimaLinguagem}`);

let coresMutaveis = ['branco', 'azul', 'rosa'];
coresMutaveis[1]='amarelo';
console.log(`Array após alteração: ${coresMutaveis}`);
coresMutaveis[coresMutaveis.length]='roxo';

let planetas = ['Terra', 'Marte'];
//push()--> adiciona 1 ou mais elementos ao final do array e retorna o novo componente
const novoComprimentoPush = planetas.push('Saturno', 'Urano'); // vai no array e adiciona na sequência

//pop()--> remove o último elemento do meu array e o shift remove o primeiro
const ultimoPlanetaRemovido = planetas.pop();

//indexOf()--> retorna o primeiro índice em que um elemento pode ser encontrado no array, ele vai por índice e não por elemento
const indiceTerra = planetas.indexOf('Terra');

//join()--> join significa junção, ou seja, faz junções de tabelas, útil para banco de dados. Cria e retorna uma nova string, concatenando todos os elementos do array
const stringPlanetas = planetas.join('-');

const coresInteracao = ['laranja','ciano','magenta'];

//3 argumentos, inicio fim, acremento/decremento. número de elementos, 0,1,2, não vai chegar em 3, cada vez que passar pelo laço vai somar +1
for(let i=0;i<coresInteracao.length;i++){
    console.log(`Cor no índice ${i} : ${coresInteracao[i]}`);
}

//Laço 'for...of' (mais moderno e legível para iterar sobre os valores)
for(const cor of coresInteracao){
    console.log(`Cor: ${cor}`);
}

coresInteracao.forEach(function(cor,indice){
    console.log(`Cor: ${cor} no índice ${indice}`);
});

//Este trecho demonstra como criar um array em JavaScript
//recebendo dados do usuário através do terminal (Node.js)
const readLine = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

//Criar um array vazio para armazenar os itens da lista de compras do usuário
const listaCompras = [];

//criar uma função para adicionar um item na lista de compras
function adicionarItem(){
    readLine.question(`Digite um item para adicionar à lista de compras (ou "fim para sair):`,(item) =>{
        const itemFormatado = item.trim();//remove todos os espaços em branco extras
        //Verifica se o usuário digitou "Fim" (Ignorando caixa alta/baixa[maiúsculo/minúsculo])
        if(itemFormatado.tolowerCase()=== 'fim'){
            //se o usuário digitou "fim", encerra a interação com o terminal
            console.log('\nSua lista de compra completa: ');
            //itera sobre cada item no array 'listaCompras'
            listaCompras.forEach((produto,indice) =>{
                console.log(`${indice+1}. ${produto}`);
            });
            readLine.close();
        }else if(itemFormatado !== ''){
            listaCompras.push(itemFormatado)//push adiciona um elemento
            console.log(`"${itemFormatado}" foi adicionado à sua lista.`);
            adicionarItem();
        }else{
            //se o usuário digitou apenas espaços ou nada
            console.log('Por favor, digite um item válido.');
            adicionarItem();
        }
    
    });
}
//inicia o processo de adicionar itens à lista de compras chamando a função pela primeira vez
console.log('Bem vindo a sua lista de compra');
adicionarItem();