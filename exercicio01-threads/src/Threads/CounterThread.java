package Threads;

public class CounterThread extends Thread {
    public CounterThread (String nome) {
        super(nome);
    }

    @Override
    public void run() {
        for (int i = 1; i <= 100; i++) {
            System.out.println("Contando: " + i);
        }
    }
}
