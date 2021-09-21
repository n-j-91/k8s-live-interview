variable "region" {
  type    = string
  default = "eu-west-1"
}

variable "ami-id" {
  type = string
  description = "AMI ID with existing configurations"
}
