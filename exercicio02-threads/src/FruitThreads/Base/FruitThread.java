package FruitThreads.Base;

public abstract class FruitThread extends Thread {
    public FruitThread(String fruitName) {
        super(fruitName);
    }

    @Override
    public void run() {
        while (!isInterrupted()) {
            System.out.println(getName());
        }
    }
}
