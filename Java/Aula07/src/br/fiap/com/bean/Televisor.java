package br.fiap.com.bean;

public class Televisor {
    //atributos
    public int volume;
    public int canal;
    //métodos da classe
    public void aumentarVolume(){
        volume++;
    }
    public void diminuirVolume(){
        volume--;
    }
    public void trocarCanal(int novoCanal){
        canal = novoCanal;
    }

}
