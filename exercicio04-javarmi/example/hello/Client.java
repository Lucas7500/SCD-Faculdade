package example.hello;

import java.rmi.Naming;

public class Client {

    private Client() {}

    public static void main(String[] args) {

        System.out.println("Initiating client");
        
        String host = (args.length < 1) ? "localhost" : args[0];
        try {
            //Registry registry = LocateRegistry.getRegistry(host);
            //System.out.println("Registry has been located");
            //Hello stub = (Hello) registry.lookup("Hello");

            Hello stub = (Hello) Naming.lookup("rmi://" + host + "/MyHello"); 
            System.out.println("Found server");
            String response = stub.sayHello();
            System.out.println("Response: " + response);

            int result = stub.soma(100,1000);
            System.out.println("Response from soma: " + result);

            double result2 = stub.divide(100.0, 3);
            System.out.println("Response from divide: " + result2);

            int result3 = stub.subtrai(1000, 250);
            System.out.println("Response from subtrai: " + result3);

            int result4 = stub.multiplica(25, 4);
            System.out.println("Response from multiplica: " + result4);

            Stats statsStub = (Stats) Naming.lookup("rmi://" + host + "/MyStats");
            System.out.println("Found stats server");

            double media = statsStub.media(7.5, 9.0, 8.5);
            System.out.println("Response from media: " + media);

            int maximo = statsStub.maximo(12, 30);
            System.out.println("Response from maximo: " + maximo);
            
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
