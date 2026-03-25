package br.com.fiap.main;

import br.com.fiap.bean.FolhaDePagamento;

public class Main {
    public static void main(String[] args) {
        FolhaDePagamento folha = new FolhaDePagamento();
        folha.salarioBruto = 10000;
        folha.descontoINSS = 15;
        folha.numeroDependentes = 4;
        folha.valorPlanoDeSaude = 150;
        System.out.printf("Salario Bruto: R$ %.2f\nDependentes: %d\nINSS: %.1f%%\nPlano de saúde: R$ %.2f \nSalário Líquido: R$ %.2f", folha.salarioBruto, folha.numeroDependentes, folha.descontoINSS, folha.valorPlanoDeSaude, folha.calcularSalarioLiquido());
    }
}
