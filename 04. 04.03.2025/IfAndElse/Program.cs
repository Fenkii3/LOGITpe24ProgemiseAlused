namespace IfAndElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //if ja else rakendus tuleb teha
            //kontrollib sinu vanust
            //1. kui old alla 18, siis konsool annab vastuseks,
            //et oled alaealine

            //2. Kui oled 19 kuni 65 aastat vana, siis
            //konsool vastab, et oled täisealine

            //3. Kui oled üle 65a vana, siis pensionäär
            
            Console.WriteLine("Sisestage oma vanus");
            int age = int.Parse(Console.ReadLine());

            if (age < 18)
            Console.WriteLine("Olete alaealine");


            else if (age >= 18 & age <= 65)
            Console.WriteLine("Olete täisealine");

            else if (age >= 66 - 100)
            Console.WriteLine("Olete pensionäär");
            

        }
    }
}
