package br.com.fiap.bean;

public class Radio {
    //atributos
    private int volume;
    private float estacao;

    //métodos getters/setters

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        try {
            if (volume >= 0 && volume <= 100) {
                this.volume = volume;
            } else {
                throw new RuntimeException("Volume fora da faixa permitida (Min: 0 e Max: 100)");
            }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public float getEstacao() {
        return estacao;
    }

    public void setEstacao(float estacao) {
        this.estacao = estacao;try {
            if (estacao >= 80.0 && volume <= 105.0) {
                this.estacao = estacao;
            } else {
                throw new RuntimeException("Estação fora de sintonia (Min: 80.0 e Max: 105.0)");
            }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }


    //métodos da classe
    public void aumentarVolume() {
        if (volume < 100) {
            volume++;
        }
    }
    public void diminuirVolume() {
        if(volume > 0) {
           volume--;
        }
    }
}
