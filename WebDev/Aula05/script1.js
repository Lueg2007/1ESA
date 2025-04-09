let nome = "Luigi";//forma de nomear uma variável
const idade = 18; //forma de nomear uma variável, o javascript ja identifica se é inteiro ou string
let mensagem = "Olá "+nome+"! Você tem "+idade+" anos de vida!!!";
console.log(mensagem);//print do javascript

let texto = "Isso é uma string";
let texto1 = "Isso também é uma string";
let numeroInteiro = 10;
let numeroDecimal = 3.14;
let isAtivo = true;
let nulo = null;
let indefinido;

console.log(typeof texto);
console.log(typeof texto1);
console.log(typeof numeroInteiro);
console.log(typeof numeroDecimal);
console.log(typeof isAtivo);
console.log(typeof nulo);
console.log(typeof indefinido);

let a = 5;
let b = 6;

console.log("Soma: ", a+b);
console.log("Subtração: ", a-b);
console.log("Multiplicação: ", a*b);
console.log("Divisão: ", a/b);
console.log("RestoDiv: ", a%b)
console.log("Potência: ", a**b)

a++;
b--;
console.log("Incrementando A: ",a);
console.log("Incrementando B: ",b);