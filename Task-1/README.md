Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
Launch EC2 Instances
	1. In the AWS Console, search for EC2 in the search bar and click EC2.
	2. Click Launch instances.
		Name: NikhilAutoStop
		Tag:
		Key: Action
		Value: Auto-Stop

       Name: NikhilAutoStart
	Tag:
	Key: Action
	Value: Auto-Start
       
       AMI : Ubuntu
	Instance Type : t2.micro
	Key pair (login):
	Network settings:
	Allow SSH (port 22) from My IP.
	Allow HTTP (port 80) 
       Click Launch instance

















Lambda Function Creation:
1. Create an IAM Role for Lambda
* AWS Console => IAM =>Roles => Create role.
* Trusted Entity type: AWS Services
* Use Case: Lambda
* Click Next


Permissions policies: AmazonEC2FullAccess



Role name: NikhilLambdaEC2ControlRole
Click Create role.





2. Create the Lambda Function
Go to AWS Console => Lambda.
Click Create function.
Select Author from scratch
Function name: NikhilEC2TagBasedControl
Runtime: Python 3.12 (or latest).
Permissions:
Expand Change default execution role.
Select Use an existing role.
Choose NikhilLambdaEC2ControlRole from the dropdown.
Click Create function.








3. Add Python Code to Control EC2
* prints instance IDs with a given tag:
* https://chatgpt.com/c/689753ea-5a90-8332-a329-a23f290b2fd7

