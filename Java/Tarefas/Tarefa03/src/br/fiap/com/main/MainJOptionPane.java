package br.fiap.com.main;

import br.fiap.com.bean.Eventos;

import javax.swing.*;

public class MainJOptionPane {
    public static void main(String[] args) {
        Eventos festa = new Eventos();
        String aux;

        try {
            aux = JOptionPane.showInputDialog("Digite o valor da despesa com as bebidas: ");
            festa.bebida = Double.parseDouble(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da despesa com as comidas: ");
            festa.comida = Double.parseDouble(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da despesa com a equipe: ");
            festa.equipe = Double.parseDouble(aux);
            aux = JOptionPane.showInputDialog("Digite o número de convidados: ");
            festa.convidados = Integer.parseInt(aux);
            aux = JOptionPane.showInputDialog("Digite o valor da despesa com o show: ");
            festa.show = Double.parseDouble(aux);
            aux = JOptionPane.showInputDialog("Digite a margem de lucro: ");
            festa.lucro = Float.parseFloat(aux);

            double valorDoIngresso = festa.calcularValorDoIngresso();

            JOptionPane.showMessageDialog(null,
                    String.format(
                            "Despesa com bebida: R$ %.2f" +
                                    "\nDespesa com comida: R$ %.2f" +
                                    "\nDespesa com a equipe: R$ %.2f" +
                                    "\nNúmero de convidados: %d pessoas" +
                                    "\nDespesa com o show: R$ %.2f" +
                                    "\nMargem de lucro: %.1f%%" +
                                    "\nValor do ingresso: R$ %.2f",
                            festa.bebida,
                            festa.comida,
                            festa.equipe,
                            festa.convidados,
                            festa.show,
                            festa.lucro,
                            valorDoIngresso
                    )
            );

        }catch(Exception e){
            JOptionPane.showMessageDialog(null, "Valor inválido");

        }
    }
}
