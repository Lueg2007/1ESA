let idade = 17;

if(idade > 18){
console.log("Você é maior de idade...");
}

let temperatura = 25;

if(temperatura > 30){
    console.log("Está muito quente");
}

let nota = 7;

if(nota>=7){
    console.log("Você foi aprovado!");
}else{
    console.log("Você foi reprovado!");
}

let estaChovendo = false;

if(estaChovendo){
    console.log("Leve o guarda-chuva");
}else{
    console.log("Não precisa de guarda-chuva");
}

const inputIdade = document.getElementById('idadeInput');
const botaoVerificar = document.getElementById('verificarIdade');
const resultadoTexto = document.getElementById('resultadoVerificacao');

botaoVerificar.addEventListener('click',function(){
    let idadeDigitada = parseInt(inputIdade.value);
    if(!isNaN(idadeDigitada)){
    if(idadeDigitada>=18){
        resultadoTexto.textContent = 'Você é maior de idade';
        resultadoTexto.style.color = 'green';
    }else{
        resultadoTexto.textContent = 'Você é menor de idade';
        resultadoTexto.style.color = 'red';
    }
}else{
    resultadoTexto.textContent = 'Por favor, digite uma idade válida';
    resultadoTexto.style.color = 'orange';

}

})