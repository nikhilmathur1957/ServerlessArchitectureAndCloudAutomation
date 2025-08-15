import boto3

def lambda_handler(event, context):
    #print(event)
    ec2 = boto3.client('ec2')

    # --- Stop instances with Auto-Stop tag ---
    stop_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}  # Only running ones
        ]
    )

    stop_ids = []
    for reservation in stop_response['Reservations']:
        for instance in reservation['Instances']:
            stop_ids.append(instance['InstanceId'])

    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print(f"Stopping instances: {stop_ids}")
    else:
        print("No running instances with Auto-Stop tag found.")

    # --- Start instances with Auto-Start tag ---
    start_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}  # Only stopped ones
        ]
    )

    start_ids = []
    for reservation in start_response['Reservations']:
        for instance in reservation['Instances']:
            start_ids.append(instance['InstanceId'])

    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print(f"Starting instances: {start_ids}")
    else:
        print("No stopped instances with Auto-Start tag found.")

    return {
        "StoppedInstances": stop_ids,
        "StartedInstances": start_ids
    }
