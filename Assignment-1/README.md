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

 <img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/49b74bee-482d-41d8-97fd-5d946d577500" />

 <img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/d8528e89-7809-4fc4-9c91-4c64b360e1f2" />



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
