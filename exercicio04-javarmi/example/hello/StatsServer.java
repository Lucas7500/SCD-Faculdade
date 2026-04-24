package example.hello;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class StatsServer {

    public StatsServer() {}

    public static void main(String[] args) {
        try {
            try {
                LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
            } catch (Exception ignored) {
                LocateRegistry.getRegistry(Registry.REGISTRY_PORT);
            }

            StatsImplem obj = new StatsImplem(5679);
            Naming.rebind("MyStats", obj);

            System.err.println("Stats server ready");
        } catch (Exception e) {
            System.err.println("Stats server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
