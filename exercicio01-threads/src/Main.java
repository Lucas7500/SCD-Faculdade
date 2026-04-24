import Threads.CounterThread;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws InterruptedException {
        CounterThread thread = new CounterThread("Thread 1 to 100");

        System.out.println("Programa Iniciado");
        thread.start();
        thread.join();
        System.out.println("Programa Finalizado");
    }
}