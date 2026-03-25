package br.com.fiap;

import java.util.Scanner;

public class EntradaDeDados {
    public static void main(String[] args) {
        int num1 = 0, num2 = 0, resultado = 0; //declaração e inicialização
        // declaração de um objeto
        Scanner scan; //objeto da classe scanner, é a declaração de um obj no Java
        // instanciação de um obj. Declaração só avisa, a instanciação torna esse aviso real

        try {
            scan = new Scanner(System.in); // É possivel fazer a instanciação e a declaração na mesma linha
            //Scanner = scan = new Scanner(System.in)
            System.out.println("Digite dois números inteiros: ");
            num1 = scan.nextInt(); //Fazer códigos com tratamento de erros, sempre
            num2 = scan.nextInt();
            resultado = num1 + num2;
            System.out.println(("Valor 1: " + num1 + "\nValor 2: " + num2 + "\nSoma dos valores: " + resultado));
            scan.close();
        } catch (Exception e) {
            System.out.println("Formato de número incorreto");
        }


    }
}
