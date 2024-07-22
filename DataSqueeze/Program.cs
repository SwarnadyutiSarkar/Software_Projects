// Program.cs
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Welcome to DataSqueeze - Data Compression and Storage Optimization");
        Console.WriteLine("Choose an option:");
        Console.WriteLine("1. Compress a file");
        Console.WriteLine("2. Decompress a file");
        Console.Write("Enter your choice (1/2): ");
        string choice = Console.ReadLine();

        switch (choice)
        {
            case "1":
                Console.Write("Enter the path of the file to compress: ");
                string inputFile = Console.ReadLine();
                Console.Write("Enter the path for the compressed file: ");
                string compressedFile = Console.ReadLine();

                try
                {
                    CompressionUtility.CompressFile(inputFile, compressedFile);
                    Console.WriteLine("File compressed successfully.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error compressing file: {ex.Message}");
                }
                break;

            case "2":
                Console.Write("Enter the path of the compressed file: ");
                string compressedFile2 = Console.ReadLine();
                Console.Write("Enter the path for the decompressed file: ");
                string decompressedFile = Console.ReadLine();

                try
                {
                    CompressionUtility.DecompressFile(compressedFile2, decompressedFile);
                    Console.WriteLine("File decompressed successfully.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error decompressing file: {ex.Message}");
                }
                break;

            default:
                Console.WriteLine("Invalid choice. Please choose 1 or 2.");
                break;
        }

        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }
}
