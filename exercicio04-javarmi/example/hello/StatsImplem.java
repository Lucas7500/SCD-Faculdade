package example.hello;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class StatsImplem extends UnicastRemoteObject implements Stats {

    public StatsImplem(int port) throws RemoteException {
        super(port);
    }

    @Override
    public double media(double a, double b, double c) throws RemoteException {
        return (a + b + c) / 3.0;
    }

    @Override
    public int maximo(int a, int b) throws RemoteException {
        return Math.max(a, b);
    }
}
