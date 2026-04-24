import models.Aula;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        ArrayList<Integer> listaNumeros = new ArrayList<Integer>();

        Aula aula1 = new Aula(listaNumeros, 1, 3);
        Aula aula2 = new Aula(listaNumeros, 4, 6);
        Aula aula3 = new Aula(listaNumeros, 7, 9);

        Thread thread1 = new Thread(aula1);
        Thread thread2 = new Thread(aula2);
        Thread thread3 = new Thread(aula3);

        thread1.start();
        thread2.start();
        thread3.start();

        thread1.join();
        thread2.join();
        thread3.join();

        for (int numero : listaNumeros)
        {
            System.out.println(numero);
        }
    }
}