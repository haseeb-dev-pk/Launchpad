output "aws_account_id" {
  description = "AWS account ID detected from the configured AWS credentials"
  value       = data.aws_caller_identity.current.account_id
}
