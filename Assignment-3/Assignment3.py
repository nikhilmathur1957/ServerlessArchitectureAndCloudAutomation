import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    
    # Get all S3 buckets
    response = s3.list_buckets()
    buckets = response["Buckets"]

    non_encrypted_buckets = []

    for bucket in buckets:
        bucket_name = bucket["Name"]
        try:
            # Check encryption settings
            enc = s3.get_bucket_encryption(Bucket=bucket_name)
            rules = enc["ServerSideEncryptionConfiguration"]["Rules"]
            
            # If rules exist, SSE is enabled
            print(f" {bucket_name} has encryption: {rules}")
        
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "ServerSideEncryptionConfigurationNotFoundError":
                print(f" {bucket_name} does NOT have encryption enabled")
                non_encrypted_buckets.append(bucket_name)
            else:
                print(f" Could not check bucket {bucket_name}: {e}")

    if non_encrypted_buckets:
        print("Buckets without encryption:", non_encrypted_buckets)
    else:
        print("All buckets have encryption enabled ✅")

    return {"NonEncryptedBuckets": non_encrypted_buckets}
