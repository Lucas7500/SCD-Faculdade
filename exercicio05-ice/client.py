import sys, Ice
import Demo
 
with Ice.initialize(sys.argv) as communicator:
    base_printer = communicator.stringToProxy("SimplePrinter:default -p 11000")
    printer = Demo.PrinterPrx.checkedCast(base_printer)
    if not printer:
        raise RuntimeError("Proxy inválido para Printer")

    print("--- Testando Printer ---")
    printer.printString("Olá do cliente modificado!")
    print(f"Soma (Printer): 10 + 20 = {printer.add(10, 20)}")
    print(f"Upper (Printer): 'hello ice' -> {printer.toUpper('hello ice')}")

    base_calc = communicator.stringToProxy("SimpleCalculator:default -p 11000")
    calculator = Demo.CalculatorPrx.checkedCast(base_calc)
    if not calculator:
        raise RuntimeError("Proxy inválido para Calculator")

    print("\n--- Testando Calculator ---")
    print(f"Soma (Calc): 15.5 + 4.5 = {calculator.add(15.5, 4.5)}")
    print(f"Sub (Calc): 100.0 - 30.0 = {calculator.sub(100.0, 30.0)}")
