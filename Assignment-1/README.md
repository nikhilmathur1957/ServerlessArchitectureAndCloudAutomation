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

 <img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/e1c1cc5f-5743-4f50-b386-b41efed2ca15" />

 <img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/67bbfc84-2200-4267-b3b9-0c40b1b2a1f6" />



Lambda Function Creation:
1. Create an IAM Role for Lambda
   
* AWS Console => IAM =>Roles => Create role.
* Trusted Entity type: AWS Services
* Use Case: Lambda
* Click Next

<img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/9606616e-7480-438e-a81f-d68ff63214bc" />

Permissions policies: AmazonEC2FullAccess

<img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/a9e5de4d-7fd3-4735-8223-1ac602e83682" />


Role name: NikhilLambdaEC2ControlRole
Click Create role.

<img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/8c9caff9-4f7f-470a-9d3b-05c9fe10c9da" />

<img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/1c068b16-34fd-43dd-9709-2e130eff2080" />


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

<img width="500" height="332" alt="image" src="https://github.com/user-attachments/assets/84e81a98-a5fb-4945-a85e-0b60ba0939e4" />


3. 3.	Add Python Code to Control EC2
	prints instance IDs with a given tag
	Full Code

 <img width="750" height="628" alt="image" src="https://github.com/user-attachments/assets/bc44df78-3690-4398-a83a-cd69d4fe2fc5" />
 <img width="750" height="499" alt="image" src="https://github.com/user-attachments/assets/96dd181d-06d8-4312-bcac-b278895afc86" />

Create the test case
  <img width="500" height="316" alt="image" src="https://github.com/user-attachments/assets/784c2464-c7bc-42c8-96eb-c24d9e664697" />

Click for deploy the code

<img width="500" height="296" alt="image" src="https://github.com/user-attachments/assets/2d82c77d-275a-4873-8d22-480ba2f6b8f5" />

Click on test for Output

 <img width="500" height="328" alt="image" src="https://github.com/user-attachments/assets/2753c914-091b-42d5-b0fe-fb01c9d8169a" />


Verification

 <img width="500" height="203" alt="image" src="https://github.com/user-attachments/assets/7d1b43d0-2fbe-47c5-a699-888aea774da5" />

