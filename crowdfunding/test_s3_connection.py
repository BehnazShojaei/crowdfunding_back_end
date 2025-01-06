import boto3
import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_S3_REGION_NAME", "ap-southeast-2")

def test_s3_connection():
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        # List S3 buckets to verify the connection
        response = s3.list_buckets()
        print("Buckets:", [bucket["Name"] for bucket in response["Buckets"]])

        # Check if bucket is accessible
        s3.head_bucket(Bucket=AWS_STORAGE_BUCKET_NAME)
        print(f"Bucket '{AWS_STORAGE_BUCKET_NAME}' is accessible.")
    except Exception as e:
        print(f"Error connecting to S3: {e}")

if __name__ == "__main__":
    test_s3_connection()
