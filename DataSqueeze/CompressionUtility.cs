// CompressionUtility.cs
using System;
using System.IO;
using System.IO.Compression;

public static class CompressionUtility
{
    public static void CompressFile(string inputFile, string compressedFile)
    {
        using (FileStream inputFileStream = File.OpenRead(inputFile))
        {
            using (FileStream compressedFileStream = File.Create(compressedFile))
            {
                using (GZipStream compressionStream = new GZipStream(compressedFileStream, CompressionMode.Compress))
                {
                    inputFileStream.CopyTo(compressionStream);
                }
            }
        }
    }

    public static void DecompressFile(string compressedFile, string decompressedFile)
    {
        using (FileStream compressedFileStream = File.OpenRead(compressedFile))
        {
            using (FileStream decompressedFileStream = File.Create(decompressedFile))
            {
                using (GZipStream decompressionStream = new GZipStream(compressedFileStream, CompressionMode.Decompress))
                {
                    decompressionStream.CopyTo(decompressedFileStream);
                }
            }
        }
    }
}
