# compress_max.py

import zlib
import boto3

# AWS S3 configuration
bucket_name = 'your-bucket-name'
s3 = boto3.client('s3')

def compress_and_upload_data(data):
    compressed_data = zlib.compress(data)
    s3.put_object(Body=compressed_data, Bucket=bucket_name, Key='compressed_data.bin')

def download_and_decompress_data():
    response = s3.get_object(Bucket=bucket_name, Key='compressed_data.bin')
    compressed_data = response['Body'].read()
    decompressed_data = zlib.decompress(compressed_data)
    return decompressed_data

# Example usage
if __name__ == "__main__":
    data = b"Your data to compress and upload"
    
    # Compress and upload data to S3
    compress_and_upload_data(data)
    print("Data compressed and uploaded to S3.")

    # Download and decompress data from S3
    decompressed_data = download_and_decompress_data()
    print(f"Decompressed data: {decompressed_data.decode()}")
