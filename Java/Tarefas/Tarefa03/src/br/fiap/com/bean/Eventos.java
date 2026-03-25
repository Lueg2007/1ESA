package br.fiap.com.bean;

public class Eventos {
    //atributos
    public double bebida;
    public double comida;
    public double equipe;
    public int convidados;
    public double show;
    public float lucro;

    //métodos
    public double calcularValorDoIngresso(){
        double despesa1, valorDoIngresso;
        despesa1 = bebida + comida + equipe + show;
        valorDoIngresso = (despesa1 * (1 + lucro / 100))/convidados;
        return valorDoIngresso;
    }
}
