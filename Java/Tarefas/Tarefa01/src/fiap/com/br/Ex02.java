package fiap.com.br;

import javax.swing.*;

public class Ex02 {
    public static void main(String[] args) {
        int nascimento = 0, anoDesejado = 0, idade = 0;
        String aux;

        try {
            aux = JOptionPane.showInputDialog("Digite o seu ano de nascimento: ");
            nascimento = Integer.parseInt(aux);
            aux = JOptionPane.showInputDialog("Digite o ano desejado ou o atual: ");
            anoDesejado = Integer.parseInt(aux);
            idade = anoDesejado - nascimento;
            JOptionPane.showMessageDialog(null, "A sua idade era/é/será: " + idade);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Formato de valor incorreto");
        }
    }
}

