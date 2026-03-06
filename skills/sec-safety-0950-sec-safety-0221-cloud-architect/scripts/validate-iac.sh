#!/bin/bash
# Validate Terraform/CloudFormation
terraform fmt -check
terraform validate
echo "IaC validation complete."
