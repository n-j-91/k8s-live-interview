
output "ssh-details" {
  value       = "ssh -i ./files/k8s_lab_rsa ubuntu@${aws_instance.k8s-lab-instance.public_ip}"
  description = "SSH details"
}
