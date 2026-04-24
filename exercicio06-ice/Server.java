import com.zeroc.Ice.*;

class PrinterI implements Demo.Printer {
    @Override
    public void printString(String s, Current current) {
        System.out.println("Printer (Java): " + s);
    }

    @Override
    public int add(int a, int b, Current current) {
        return a + b;
    }

    @Override
    public String toUpper(String s, Current current) {
        return s.toUpperCase();
    }
}

class CalculatorI implements Demo.Calculator {
    @Override
    public float add(float a, float b, Current current) {
        return a + b;
    }

    @Override
    public float sub(float a, float b, Current current) {
        return a - b;
    }
}

public class Server {
    public static void main(String[] args) {
        try (Communicator communicator = Util.initialize(args)) {
            ObjectAdapter adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000");
            
            adapter.add(new PrinterI(), Util.stringToIdentity("SimplePrinter"));
            adapter.add(new CalculatorI(), Util.stringToIdentity("SimpleCalculator"));
            
            adapter.activate();
            System.out.println("Servidor Java rodando...");
            communicator.waitForShutdown();
        }
    }
}
