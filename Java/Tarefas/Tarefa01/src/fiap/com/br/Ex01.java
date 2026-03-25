package fiap.com.br;

import javax.swing.*;

public class Ex01 {
    public static void main(String[] args) {
        float soma = 0, prova1 = 0, prova2 = 0, prova3 = 0, prova4 = 0, media = 0;
        String aux;
        try {
            aux = JOptionPane.showInputDialog("Digite o valor da primeira prova: ");
            prova1 = Float.parseFloat(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da segunda prova: ");
            prova2 = Float.parseFloat(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da terceira prova: ");
            prova3 = Float.parseFloat(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da quarta prova: ");
            prova4 = Float.parseFloat(aux);
            soma = prova1 + prova2 + prova3 + prova4;
            media = soma / 4;
            JOptionPane.showMessageDialog(null, "A média das provas é de: " + media);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Formato de valor inválido");
        }
    }
}
