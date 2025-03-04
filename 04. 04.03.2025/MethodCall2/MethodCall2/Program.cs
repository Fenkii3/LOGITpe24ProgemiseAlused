namespace MethodCall2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //siin kasutada if ja else
            //m]lemas valikus peab v'lja kutsuma meetodi
            //teemaks paaris ja paaritud arvud
            //paaris ja paaritu arvu tekst on teise meetodi sees

            Console.WriteLine("Hello, World!");

            int number = int.Parse(Console.ReadLine());

            if (int.IsEvenInteger(number))
            {
                EvenNumbers(number);
            }
            else
            {
                OddNumbers(number);
            }
        }

        static void EvenNumbers(int nr)
        {
            Console.WriteLine("Tegemist on paaris arvuga " + nr);
        }
        //EvenNumbers meetod

        static void OddNumbers(int nr)
        {
            Console.WriteLine("Tegemist on paaritu arvuga " + nr);
        }
        //OddNumbers meetod
    }
}



