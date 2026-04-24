Com base no exemplo apresentado em aula (código-fonte fornecido no repositório da tarefa por meio GitHub Classroom), faça o que se pede:

* acrescente novas funções no servidor
* faça o cliente chamar as novas funções
* crie um novo objeto servidor (você escolhe a função)
* faça o cliente chamar as funções do novo servidor

---

# POO-JavaRMI-Hello
Simple example used to teach distributed objects in the OOP course

Based on Oracle's Java RMI Guide: https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/hello/hello-world.html

It is composed by three files:

- Hello.java: description of the remote object's interface
- Server.java: implementation of the remote object + code to start a server process where the object will run
- Client.java: a simple client to demonstrate the invocation of method's on the remote object.

### First, if necessary, install the JDK on the machines:

  sudo apt install default-jdk

### Then, configure the firewall (security group -- if running it on AWS)

  Open the following ports for TCP: 1099, 1900

### Then, run the server on one machine and the client on another

  java example.hello.Server

  java example.hello.Client <IP_Address_of_Server>
  
### Now, extend the example:

Try adding other methods to the remote object and calling them from the client.