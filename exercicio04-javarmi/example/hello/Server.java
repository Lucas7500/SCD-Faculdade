package example.hello;

import java.rmi.Naming;
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;

public class Server {

    public Server() {}

    public static void main(String args[]) {
        try {
            try {
                LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
            } catch (Exception ex) {
                LocateRegistry.getRegistry(Registry.REGISTRY_PORT);
            }
            
            HelloImplem obj = new HelloImplem(5678);
            Naming.rebind("MyHello", obj);

            System.err.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
