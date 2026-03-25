package com.lueg.fiap.JOption;

import javax.swing.*;

public class Trapezio {
    public static void main(String[] args) {
        double baseMenor = 0, baseMaior = 0, altura = 0, area = 0;
        String aux;

        try {
            aux = JOptionPane.showInputDialog("Digite o valor da base maior: ");
            baseMaior = Float.parseFloat(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da base menor: ");
            baseMenor = Float.parseFloat(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da altura: ");
            altura = Float.parseFloat(aux);
            area = ((baseMaior + baseMenor) * altura)/2;
            JOptionPane.showMessageDialog(null, "O valor da sua área é de: " + area);

        } catch (Exception e){
            JOptionPane.showMessageDialog(null, "Formato de número inválido:");
        }

    }
}