Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
Task: Automate the deletion of files older than 30 days in a specific S3 bucket.
1.	S3 Setup: (I used old bucket for the task)
a.	Navigate to the S3 dashboard and create a new bucket.
i.	Click the orange Create bucket button.
ii.	Bucket name: nikhilmathur-static-signup-site (Must be globally unique)
iii.	Choose your preferred region (Keep it consistent with other resources (like EC2, Lambda))
iv.	Open your bucket by clicking its name.
v.	 Click Upload → Add files (choose any file from your computer).
vi.	 Click Upload at the bottom.
 
<img width="500" height="356" alt="image" src="https://github.com/user-attachments/assets/e1e3ae29-63d4-466b-9a4c-4cf68446fb6e" />



2.	Lambda Function:
a.	Create an IAM Role for Lambda
i.	AWS Console => IAM =>Roles => Create role.
ii.	Trusted Entity type: AWS Services
iii.	Use Case: Lambda
iv.	Click Next
v.	Permissions policies: AmazonS3FullAccess
vi.	Role name: NikhilLambdaS3CleanupRole
 
<img width="500" height="422" alt="image" src="https://github.com/user-attachments/assets/11fc994b-2d22-4912-aace-011d137ed77a" />

<img width="500" height="382" alt="image" src="https://github.com/user-attachments/assets/1963efcf-4efd-48f3-8f7d-a7601d62d94c" />

 <img width="500" height="377" alt="image" src="https://github.com/user-attachments/assets/d8ef50cb-ba25-42a7-a74c-f5527bfc148f" />


 

b.	Create the Lambda Function
i.	Go to AWS Console => Lambda.
ii.	Click Create function.
iii.	Select Author from scratch
iv.	Function name: NikhilS3BucketCleanup
v.	Runtime: Python 3.13
vi.	Permissions:
vii.	Expand Change default execution role.
viii.	Select Use an existing role.
ix.	Choose NikhilLambdaS3CleanupRole from the dropdown.
x.	Note => I choose the role prashantb12-role-9p53470y for permission access to run the code.
xi.	Click Create function.


 <img width="500" height="363" alt="image" src="https://github.com/user-attachments/assets/44e60a62-6a23-462d-a0de-e96eb5336f4d" />

		
	Code

 <img width="864" height="603" alt="image" src="https://github.com/user-attachments/assets/d23d2ebd-1c71-49bb-9305-5bdea6318c62" />

		 
Click for deploy the code
Click Test → Create test event → name it CleanupTest.
Keep event JSON as {}.
Run the test.
Check the Logs for deleted files list.

 <img width="600" height="375" alt="image" src="https://github.com/user-attachments/assets/4cb71918-99a5-4b0a-b71c-79253746c14d" />


3.	Manual Invocation:
Before function run
 <img width="756" height="282" alt="image" src="https://github.com/user-attachments/assets/88059e83-2afa-4f21-a8ce-b9ae247360e7" />


After run the function
 <img width="756" height="295" alt="image" src="https://github.com/user-attachments/assets/6a6778e1-e401-4d05-8da6-9466415f7b4e" />

