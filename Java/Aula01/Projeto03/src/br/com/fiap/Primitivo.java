package br.com.fiap;

public class Primitivo {
    public static void main(String[] args) {
        //declaração e inicialização de variáveis -> tipo nome = valor;
        char sexo = 'F';
        byte idade = 27;
        short codigo = 15650;
        int alunos = 50, classes = 11;
        long brasileiros = 216635748; //indicar que o número é um Long
        float media = 8.7f; //indicar que o número é um float
        double dolar = 5.15;
        boolean alternativa = false;
        String nome = "Astrogildo Planetário Celeste";
        System.out.println("Sexo: " + sexo + " Idade: " + idade + " Código: " + codigo + " Média: " + media );
        System.out.println(" Alunos: " + alunos + " Turmas: " + classes + " Habitantes: " + brasileiros);
        System.out.println(" Cotação do dólar: " + dolar + " Alternativa: " + alternativa + " Nome: " + nome);

    }
}
