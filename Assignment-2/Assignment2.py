import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "nikhilmathur-static-signup-site"
    days_threshold = 10   #10 days old files

    # Calculate cutoff date
    cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days_threshold)

    # List all objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        print("Bucket is empty.")
        return {"Deleted": [], "Message": "No files found."}

    deleted_files = []

    for obj in response['Contents']:
        if obj['LastModified'] < cutoff_date:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            deleted_files.append(obj['Key'])
            print(f"Deleted: {obj['Key']}")

    if not deleted_files:
        print("No files older than threshold found.")
    else:
        print(f"Deleted {len(deleted_files)} files.")

    return {"Deleted": deleted_files}