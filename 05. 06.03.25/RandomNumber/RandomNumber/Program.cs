namespace RandomNumber
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            int number = new Random().Next(1, 7);

            //nüüd tuleb kasutada switchi, et näidata numbrit 1-st kuni 6-ni.

            switch (number)
            {
                case 1:
                    Console.WriteLine("Veeretasid nr 1");
                    break;
                case 2:
                    Console.WriteLine("Veeretasid nr 2");
                    break;
                case 3:
                    Console.WriteLine("Veeretasid nr 3");
                    break;
                case 4:
                    Console.WriteLine("Veeretasid nr 4");
                    break;
                case 5:
                    Console.WriteLine("Veeretasid nr 5");
                    break;
                case 6:
                    Console.WriteLine("Veeretasid nr 6");
                    break;
                default:
                    Console.WriteLine("ERROOOR");
                    break;
                }
            }
        }
}




