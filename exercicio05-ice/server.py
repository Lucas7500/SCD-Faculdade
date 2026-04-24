import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(f"Printer: {s}")

    def add(self, a, b, current=None):
        return a + b

    def toUpper(self, s, current=None):
        return s.upper()

class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b
    
    def sub(self, a, b, current=None):
        return a - b

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
    
    printer_obj = PrinterI()
    adapter.add(printer_obj, communicator.stringToIdentity("SimplePrinter"))
    
    calc_obj = CalculatorI()
    adapter.add(calc_obj, communicator.stringToIdentity("SimpleCalculator"))
    
    adapter.activate()
    print("Servidor rodando...")
    communicator.waitForShutdown()
