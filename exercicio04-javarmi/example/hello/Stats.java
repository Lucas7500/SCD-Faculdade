package example.hello;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Stats extends Remote {
    double media(double a, double b, double c) throws RemoteException;
    int maximo(int a, int b) throws RemoteException;
}
