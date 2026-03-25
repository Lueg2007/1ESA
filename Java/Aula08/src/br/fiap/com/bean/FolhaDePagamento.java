package br.fiap.com.bean;

public class FolhaDePagamento {
    //atributos
    public double salarioBruto;
    public int numeroDependentes;
    public double descontoINSS;
    public double valorPlanoDeSaude;

    //métodos da classe
    public double calcularSalarioLiquido() {
        double desconto1, desconto2, salarioLiquido;
        desconto1 = salarioBruto * (descontoINSS / 100);
        desconto2 = valorPlanoDeSaude * (numeroDependentes + 1);
        salarioLiquido = salarioBruto - (desconto1 + desconto2);
        return salarioLiquido ;
    }
}
