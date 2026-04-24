module Demo
{
    interface Printer
    {
        void printString(string s);
        int add(int a, int b);
        string toUpper(string s);
    }

    interface Calculator
    {
        float add(float a, float b);
        float sub(float a, float b);
    }
}