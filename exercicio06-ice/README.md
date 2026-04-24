Executar o cliente Java desta tarefa em conjunto com o objeto servidor do Exercício 05 (mas em máquinas separadas) e, em seguida fazer, o que se pede:

* Estender o cliente para chamar os novos métodos do objeto servidor;
* Criar um servidor Java com para a mesma interface.

---

### Install ICE for Java on Amazon Linux
#### Install Amazon Corretto 17 (JDK):
```
sudo dnf install java-17-amazon-corretto-devel -y
```
#### Add ZeroC Ice 3.8 Repository
```
sudo dnf install sudo dnf install sudo dnf install  https://download.zeroc.com/ice/3.7/amzn2023/ice-repo-3.7.amzn2023.noarch.rpm -y
```
#### Install the Slice-to-Java compiler
```
sudo dnf install ice-compilers -y
```

### Install ICE for Java on Ubuntu
#### Install OpenJDK
```
sudo apt uptdate
sudo apt install default-jdk
```
#### Add ZeroC Ice 3.8 Repository
```
wget "https://download.zeroc.com/ice/3.7/ubuntu24.04/ice-repo-3.7_1.0.0_all.deb" -O ice-repo.deb
sudo dpkg -i ice-repo.deb
rm ice-repo.deb
sudo apt-get update
```
#### Install the Slice-to-Java compiler
```
sudo apt-get install zeroc-ice-compilers
```

### Get the ICE jar (the ICE Java runtime)
```
wget https://repo1.maven.org/maven2/com/zeroc/ice/3.7.11/ice-3.7.11.jar
```
### Compile the Client (after compiling the interface with slice2java)
```
javac -cp ".:ice-3.7.11.jar" Client.java Demo/*.java
```
### Run the client:
```
java -cp ".:ice-3.7.11.jar" Client
```
### Note: configure the IP address and port appropriately