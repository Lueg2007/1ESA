package com.lueg.fiap.JOption;

import javax.swing.*;

public class Triangulo {
    public static void main(String[] args) {
        double base = 0, altura = 0, area = 0;
        String aux;

        try {
            aux = JOptionPane.showInputDialog("Digite o valor da base: ");
            base = Float.parseFloat(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da altura: ");
            altura = Float.parseFloat(aux);
            area = (base * altura)/2;
            JOptionPane.showMessageDialog(null, "O valor da sua área é de: " + area);

        } catch (Exception e){
            JOptionPane.showMessageDialog(null, "Formato de número inválido:");
        }

    }
}

