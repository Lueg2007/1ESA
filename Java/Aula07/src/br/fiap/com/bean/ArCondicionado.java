package br.fiap.com.bean;

public class ArCondicionado{
    //atributos
    public int temperatura;
    public String modo;
    //métodos da classe
    public void aumentarTemperatura(){
        temperatura++;
    }
    public void diminuirTemperatura(){
        temperatura--;
    }
    public void trocarModo(String novoModo){
        modo = novoModo;
    }

}
