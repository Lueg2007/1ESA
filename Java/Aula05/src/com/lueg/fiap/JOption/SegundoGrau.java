package com.lueg.fiap.JOption;

import javax.swing.*;

public class SegundoGrau {
    public static void main(String[] args) {
        double a, b, c, delta, x1, x2;
        String aux;

        try {
            aux = JOptionPane.showInputDialog("Digite o valor de A: ");
            a = Double.parseDouble(aux);
            aux = JOptionPane.showInputDialog("Digite o valor de B: ");
            b = Double.parseDouble(aux);
            aux = JOptionPane.showInputDialog("Digite o valor de C: ");
            c = Double.parseDouble(aux);
            delta = (b * b) - (4 * a * c);
            x1 = (-b + Math.sqrt(delta))/ (2 * a);
            x2 = (-b - Math.sqrt(delta))/ (2 * a);
            JOptionPane.showMessageDialog(null, "O valor de delta é de: " + delta +
                    "\nO valor de x1 é de: " + x1 +
                    "\nO valor de x2 é de: " + x2
                    );

        } catch (Exception e){
            JOptionPane.showMessageDialog(null, "Formato de número inválido:");
        }

    }
}

