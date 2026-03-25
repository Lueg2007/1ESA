package fiap.com.br;

import javax.swing.*;

public class Ex03 {
    public static void main(String[] args) {
        double raio = 0, area = 0;
        String aux;

        try {
            aux = JOptionPane.showInputDialog("Digite o valor do raio da sua circunferência: ");
            raio = Integer.parseInt(aux);
            area = 3.14 * (raio * raio);
            JOptionPane.showMessageDialog(null, "A área da sua circunferência é de: " + area);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Formato de valor incorreto");
        }
    }
}
