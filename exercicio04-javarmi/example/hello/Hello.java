package example.hello;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Hello extends Remote {
    String sayHello() throws RemoteException;
    int soma(int a, int b) throws RemoteException;
    double divide(double a, int b) throws RemoteException;
    int subtrai(int a, int b) throws RemoteException;
    int multiplica(int a, int b) throws RemoteException;
}
