package br.com.fiap.main;

import br.com.fiap.bean.Radio;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Radio radio = new Radio();
        int volume;
        float estacao;
        Scanner scan;
        try {
            // leitura das informações
            scan = new Scanner(System.in);
            System.out.println("Digite o volume:");
            volume = scan.nextInt();
            System.out.println("Digite a estação:");
            estacao = scan.nextFloat();

            //atribuição dos valores (para objeto)
            radio.setVolume(volume);
            radio.setEstacao(estacao);

            //aumentando o volume (3x vezes)
            radio.aumentarVolume();
            radio.aumentarVolume();
            radio.aumentarVolume();

            //exibindo informações
            System.out.printf("Volume: %d\nEstação: %.1f", radio.getVolume(), radio.getEstacao());
        } catch (Exception e) {
            System.out.println("Formato de número incorreto");
        }
    }
}
