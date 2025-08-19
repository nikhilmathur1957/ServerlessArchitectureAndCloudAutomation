Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

Objective: To enhance your AWS security posture by setting up a Lambda function that detects any S3 bucket without server-side encryption.

Task: Automate the detection of S3 buckets that don't have server-side encryption enabled.

1.	Create an IAM Role for Lambda
	AWS Console => IAM =>Roles => Create role.
	Trusted Entity type: AWS Services
	Use Case: Lambda
	Click Next

<img width="800" height="421" alt="image" src="https://github.com/user-attachments/assets/c5cf2732-109e-469e-b727-a2340853e7c8" />

Permissions policies: AmazonEC2FullAccess
Role name: NikhilLambdaEC2ControlRole1
Click Create role.

2.	Create the Lambda Function
Go to AWS Console => Lambda.
Click Create function.
Select Author from scratch
Function name: NikhilS3EncryptionCheck
Runtime: Python 3.13
Permissions:
Expand Change default execution role.
Select Use an existing role.
Choose NikhilLambdaEC2ControlRole1 from the dropdown.
Note => I choose the role prashantb12-role-9p53470y for permission access to run the code.
Click Create function.

<img width="800" height="358" alt="image" src="https://github.com/user-attachments/assets/08387138-6fde-45bf-b97b-0459c0d388de" />

3.	Add Python Code to Control EC2

<img width="819" height="735" alt="image" src="https://github.com/user-attachments/assets/fad83ab2-2ffd-4520-a3b3-43e391081669" />
<img width="819" height="188" alt="image" src="https://github.com/user-attachments/assets/487d0cb5-c257-4388-9621-d40bc00dea7b" />

Create the test case

<img width="778" height="316" alt="image" src="https://github.com/user-attachments/assets/c08022fa-c7f5-4890-9125-c764de6010d1" />

Click for deploy the code
Test the code


<img width="778" height="421" alt="image" src="https://github.com/user-attachments/assets/d0677c73-7948-4458-8665-70eaaaffe89f" />



