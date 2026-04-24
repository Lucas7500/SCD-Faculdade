package models;

import java.util.List;

public class Aula implements Runnable {

    private final List<Integer> listaNumeros;
    private final int numeroInicial;
    private final int quantidadeNumeros;

    public Aula(List<Integer> listaNumeros, int numeroInicial, int quantidadeNumeros) {
        this.listaNumeros = listaNumeros;
        this.numeroInicial = numeroInicial;
        this.quantidadeNumeros = quantidadeNumeros;
    }

    @Override
    public void run() {
        for (int i = numeroInicial; i <= quantidadeNumeros; i++)
        {
            listaNumeros.add(i);
        }
    }
}
