import FruitThreads.*;

public class Main {
    public static void main(String[] args) {
        AppleThread appleThread = new AppleThread();
        BananaThread bananaThread = new BananaThread();
        GrapeThread grapeThread = new GrapeThread();
        PeachThread peachThread = new PeachThread();
        PineappleThread pineappleThread = new PineappleThread();

        appleThread.start();
        bananaThread.start();
        grapeThread.start();
        peachThread.start();
        pineappleThread.start();

        try {
            Thread.sleep(3000);
        }
        catch (Exception ex) {
            System.out.println(ex.toString());
        }

        appleThread.interrupt();
        bananaThread.interrupt();
        grapeThread.interrupt();
        peachThread.interrupt();
        pineappleThread.interrupt();
    }
}