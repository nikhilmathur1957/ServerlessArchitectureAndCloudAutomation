import boto3
import datetime

def lambda_handler(event, context):
    BUCKET_NAME = "nikhilmathur-s3"
    DAYS_THRESHOLD = 20 #20 days old files for this test

    s3 = boto3.client("s3")

    # Calculate cutoff date (UTC)
    cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=DAYS_THRESHOLD)

    deleted_files = []
    continuation_token = None

    # Use paginator to handle >1000 objects
    while True:
        if continuation_token:
            response = s3.list_objects_v2(Bucket=BUCKET_NAME, ContinuationToken=continuation_token)
        else:
            response = s3.list_objects_v2(Bucket=BUCKET_NAME)

        if "Contents" not in response:
            print(f"No objects found in bucket {BUCKET_NAME}")
            break

        for obj in response["Contents"]:
            key = obj["Key"]
            last_modified = obj["LastModified"]

            if last_modified < cutoff_date:
                print(f"Deleting {key} (LastModified: {last_modified})")
                s3.delete_object(Bucket=BUCKET_NAME, Key=key)
                deleted_files.append(key)

        # Check if more pages of results exist
        if response.get("IsTruncated"):
            continuation_token = response["NextContinuationToken"]
        else:
            break

    print(f"✅ Deleted {len(deleted_files)} objects from {BUCKET_NAME}")
    return {"deleted_count": len(deleted_files), "deleted_files": deleted_files}
