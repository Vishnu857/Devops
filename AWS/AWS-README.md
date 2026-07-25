# AWS USEFUL CLI COMMANDS
# EC2
List EC2
```bash
aws ec2 describe-instances --profile <profile> --output table --query "Reservations[*].Instances[*].{ID:InstanceId,Name:Tags[?Key=='Name']|[0].Value,Type:InstanceType,State:State.Name}"
```
Connect to EC2 using SSM
```bash
aws ssm start-session --profile <profile> --target  <Instance-id>
```
----
# Connect to DB/Redis/Elasticache
```bash
aws ssm start-session --target <instance-id> --document-name AWS-StartPortForwardingSessionToRemoteHost --parameters host="<DB-HOST>",portNumber="<DB-PORT>",localPortNumber="<LOCAL-PORT>" --profile <profile>
```
----
# SECURITY GROUP
Add CIDR to security group
```bash
 aws ec2 authorize-security-group-ingress --group-id <sg-id> --ip-permissions 'IpProtocol=tcp,FromPort=<from-port>,ToPort=<to-port>,IpRanges=[{CidrIp=<ip>/32,Description=""}]' --profile <profile>
```
Get security group id by name
```Bash
aws ec2 describe-security-groups --filters "Name=group-name,Values=<sg-name>" --query "SecurityGroups[0].GroupId" --output text --profile <profile>
```
Get details about a security group
```Bash
aws ec2 describe-security-groups --group-ids <sg-id> --query "SecurityGroups[*].IpPermissions" --output table  --no-cli-pager --profile <profile>
```
----
# EKS
Connect to EKS and get kubeconfig along with alias
```bash
aws eks update-kubeconfig  --name <CLUSTER-NAME> --alias <ALIAS-NAME>
```
----
# S3
List S3 buckets
```bash
aws s3 ls
```
List files in S3 bucket
```bash
aws s3 ls s3://<BUCKET-NAME>
```
Upload a File
```bash
aws s3 cp <file-name.txt> s3://<BUCKET-NAME>/<path>
```
Upload an entire folder
```bash
aws s3 cp ./<FOLDER-NAME> s3://<BUCKET-NAME>/<FOLDER-NAME> --recursive
```
Download a file to specific directory
```bash
aws s3 cp s3://<BUCKET-NAME>/<FILE-NAME> <PATH>
```
Download an entire folder
```bash
aws s3 cp s3://<BUCKET-NAME>/<FOLDER-NAME> ./<FOLDER-NAME> --recursive
```
Uploads only new or changed files.
```bash
aws s3 sync ./<FOLDER> s3://<BUCKET-NAME>/<FOLDER>
```
Delete files in S3 that don't exist locally:
```bash
aws s3 sync ./<FOLDER> s3://<BUCKET-NAME>/<FOLDER> --delete
```
Sync S3 to Local
```bash
aws s3 sync s3://<BUCKET-NAME>/<FOLDER> ./<FOLDER>
```
Copy Files Within S3
```bash
aws s3 cp s3://bucket1/file.txt s3://bucket2/file.txt
```
Copy a folder:
```bash
aws s3 cp s3://bucket1/images s3://bucket2/images --recursive
```
Local → S3
```bash
aws s3 mv file.txt s3://my-bucket/
```
S3 → Local
```bash
aws s3 mv s3://my-bucket/file.txt .
```
Within S3
```bash
aws s3 mv s3://bucket1/file.txt s3://bucket2/file.txt
```
Delete a File
```bash
aws s3 rm s3://my-bucket/file.txt
```
Delete a Folder
```bash
aws s3 rm s3://my-bucket/images --recursive
```
Remove Everything from a Bucket
```bash
aws s3 rm s3://my-bucket --recursive
```
----
