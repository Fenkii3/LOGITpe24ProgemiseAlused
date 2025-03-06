namespace RandomColor
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Random Color");

            //Colour c = (Colour)(new Random()).Next(0, 5);

            //kasutate switchi, et kutsuda esile v'rv

            for (int i = 0; i < 130; i++)
            {
                Colour c = (Colour)(new Random()).Next(0, 5);

                switch (c)
                {
                    case Colour.Red:
                        Console.BackgroundColor = ConsoleColor.Red;
                        Console.Clear();
                        Console.WriteLine("The colour is red");
                        Console.Beep();
                        break;

                    case Colour.Green:
                        Console.BackgroundColor = ConsoleColor.Green;
                        Console.Clear();
                        Console.WriteLine("The colour is green");
                        Console.Beep();
                        break;

                    case Colour.Blue:
                        Console.BackgroundColor = ConsoleColor.Blue;
                        Console.Clear();
                        Console.WriteLine("The colour is blue");
                        Console.Beep();
                        break;

                    case Colour.Brown:
                        Console.BackgroundColor = ConsoleColor.DarkMagenta;
                        Console.Clear();
                        Console.WriteLine("The colour is brown");
                        Console.Beep();
                        break;

                    case Colour.Purple:
                        Console.BackgroundColor = ConsoleColor.DarkMagenta;
                        Console.Clear();
                        Console.WriteLine("The colour is purple");
                        Console.Beep();
                        break;

                    case Colour.White:
                        Console.BackgroundColor = ConsoleColor.White;
                        Console.Clear();
                        Console.WriteLine("The colour is white");
                        Console.Beep();
                        break;

                    default:
                        Console.WriteLine("ERROR");
                        break;
                }
            }

            Colour colour = (Colour)(new Random()).Next(0, 5);
            Console.WriteLine("The color is {0}", colour);
        }
    }

    public enum Colour
    {
        Red,
        Green,
        Blue,
        Brown,
        Purple,
        White
    }
}
