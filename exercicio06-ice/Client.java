import com.zeroc.Ice.*;

public class Client {
    public static void main(String[] args) {
        try (Communicator communicator = Util.initialize(args)) {
            ObjectPrx basePrinter = communicator.stringToProxy("SimplePrinter:default -h localhost -p 11000");
            Demo.PrinterPrx printer = Demo.PrinterPrx.checkedCast(basePrinter);

            if (printer == null) {
                throw new Error("Proxy inválido para Printer");
            }

            System.out.println("--- Testando Printer (Java) ---");
            printer.printString("Olá de Java!");
            System.out.println("Soma (Printer): 10 + 20 = " + printer.add(10, 20));
            System.out.println("Upper (Printer): 'hello ice' -> " + printer.toUpper("hello ice"));

            ObjectPrx baseCalc = communicator.stringToProxy("SimpleCalculator:default -h localhost -p 11000");
            Demo.CalculatorPrx calculator = Demo.CalculatorPrx.checkedCast(baseCalc);

            if (calculator == null) {
                throw new Error("Proxy inválido para Calculator");
            }

            System.out.println("\n--- Testando Calculator (Java) ---");
            System.out.println("Soma (Calc): 15.5 + 4.5 = " + calculator.add(15.5f, 4.5f));
            System.out.println("Sub (Calc): 100.0 - 30.0 = " + calculator.sub(100.0f, 30.0f));

        } catch (LocalException e) {
            e.printStackTrace();
        }
    }
}
