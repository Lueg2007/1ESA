const readline = require('readline').createInterface({
    input:process.stdin,
    output:process.stdout,
});

readline.question('Por favor, digite o valor total da compra: ' ,(numeroDigitado) => {
    const numero = parseFloat(numeroDigitado);
    
    if(isNaN(numero)) {
        console.log('Por favor, digite um número válido.'); 
        } else {
            let numeroFinal = numero;
        
        if(numero > 100) {
            numeroFinal = numero * 0.9;
            console.log(`Desconto de 10% aplicado, o valor final é de: R$ ${numeroFinal.toFixed(2)}`);
        }else{
            console.log(`Sem desconto o valor final é de: R$ ${numeroFinal.toFixed(2)}`);
        }
    } 

    readline.close();
});