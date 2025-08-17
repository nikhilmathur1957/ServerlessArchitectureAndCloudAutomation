import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Extract instance ID from the event
    detail = event.get("detail", {})
    instance_id = detail.get("instance-id")

    if not instance_id:
        print("No instance ID found in event.")
        return

    # Current date
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    # Define tags
    tags = [
        {'Key': 'LaunchDate', 'Value': today},
        {'Key': 'Owner', 'Value': 'Nikhil'} 
    ]

    # Apply tags
    ec2.create_tags(Resources=[instance_id], Tags=tags)
    
    print(f"Tagged instance {instance_id} with {tags}")
    return {"instance_id": instance_id, "tags": tags}
