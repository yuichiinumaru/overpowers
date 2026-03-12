#!/bin/bash
# Quick AWS enumeration for pen testing

echo "--- Caller Identity ---"
aws sts get-caller-identity

echo "--- IAM Users ---"
aws iam list-users --query 'Users[*].UserName' --output text

echo "--- S3 Buckets ---"
aws s3 ls

echo "--- EC2 Instances ---"
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,PublicIpAddress]' --output table

echo "--- Lambda Functions ---"
aws lambda list-functions --query 'Functions[*].FunctionName' --output text

echo "--- RDS Instances ---"
aws rds describe-db-instances --query 'DBInstances[*].DBInstanceIdentifier' --output text
