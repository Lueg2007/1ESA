package br.fiap.com.main;

import br.fiap.com.bean.FolhaDePagamento;

import javax.swing.*;

public class MainJOptionPane {
    public static void main(String[] args) {
        FolhaDePagamento folha = new FolhaDePagamento();
        String aux;
        try {
            aux = JOptionPane.showInputDialog("Digite o valor do salário bruto: ");
            folha.salarioBruto = Double.parseDouble(aux);
            aux = JOptionPane.showInputDialog("Digite o valor do número de dependentes: ");
            folha.numeroDeDependentes = Integer.parseInt(aux);
            aux = JOptionPane.showInputDialog("Digite o valor do desconto do INSS: ");
            folha.descontoINSS = Double.parseDouble(aux);
            aux = JOptionPane.showInputDialog("Digite o valor do valor do plano de saúde: ");
            folha.valorPlanoDeSaude = Double.parseDouble(aux);

            double salarioLiquido = folha.calcularSalarioLiquido();

            JOptionPane.showMessageDialog(null, "Resumo da sua folha de pagamento" +
                    "\nSalario Bruto: R$ " + folha.salarioBruto +
                    "\nNúmero de dependentes: " + folha.numeroDeDependentes +
                    "\nDesconto do INSS: R$ " + folha.descontoINSS +
                    "\nValor do plano de saúde: R$ " + folha.valorPlanoDeSaude +
                    "\nSeu salário líquido: R$ " + salarioLiquido);
        }catch (Exception e) {
            JOptionPane.showMessageDialog(null,"O valor digitado é inválido, por favor, coloque um número válido");
        }
    }
}
