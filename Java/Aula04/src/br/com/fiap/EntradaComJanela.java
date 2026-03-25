package br.com.fiap;

import javax.swing.*;

public class EntradaComJanela {
    public static void main(String[] args) {
        int num1, num2, resultado;
        String auxiliar;
        try {
            auxiliar = JOptionPane.showInputDialog("Digite um número: ");
            num1 = Integer.parseInt(auxiliar);
            auxiliar = JOptionPane.showInputDialog("Digite outro número: "); //Integer porque o número é inteiro
            num2 = Integer.parseInt(auxiliar);
            resultado = num1 + num2;
            JOptionPane.showMessageDialog(null, "Valor 1: " + num1 + "\nValor 2: " + num2 + "\nSoma dos valores: " + resultado);//null = o java quer a localização da janela, posso abrir ela dentro de outra janela, como não tem outra janela, coloca nulo, caso tivesse outra e eu quisesse colocar, era só colocar o valor da outra janela

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Formato de número incorreto");
        }
    }
}
