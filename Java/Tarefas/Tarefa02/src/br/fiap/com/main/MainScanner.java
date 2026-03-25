package br.fiap.com.main;

import br.fiap.com.bean.FolhaDePagamento;

import java.util.Scanner;

public class MainScanner {
    public static void main(String[] args) {
        FolhaDePagamento folha = new FolhaDePagamento();
        double salarioBruto, descontoINSS, valorPlanoDeSaude, salarioLiquido;
        int numeroDeDependentes;
        Scanner scan;
        try {
            scan = new Scanner(System.in);
            System.out.print("Digite seu salário bruto: ");
            salarioBruto = scan.nextDouble();
            System.out.print("Digite o número de dependentes: ");
            numeroDeDependentes = scan.nextInt();
            System.out.print("Digite o desconto de INSS: ");
            descontoINSS = scan.nextDouble();
            System.out.print("Digite o valor do plano de saúde: ");
            valorPlanoDeSaude = scan.nextDouble();
            //armazenando valores mos atributos do objeto
            folha.salarioBruto = salarioBruto;
            folha.numeroDeDependentes = numeroDeDependentes;
            folha.descontoINSS = descontoINSS;
            folha.valorPlanoDeSaude = valorPlanoDeSaude;
            //calculando salário líquido
            salarioLiquido = folha.calcularSalarioLiquido();
            //exibindo informações e resultado
            System.out.printf("Salário Bruto: R$ %.2f\nNúmero de dependentes: %d\nINSS: %.1f%%\nPlano de saúde: R$ %.2f\nSalário líquido: R$ %.2f", folha.salarioBruto, folha.numeroDeDependentes, folha.descontoINSS, folha.valorPlanoDeSaude, salarioLiquido);

        }catch (Exception e){
            System.out.println("Formato incorreto!");
        }
    }
}
