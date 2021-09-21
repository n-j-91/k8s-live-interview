variable "region" {
  type    = string
  default = "eu-west-1"
}

variable "unique-prefix" {
  type = string
  description = "A Unique prefix for identifying this instance(mandatory)"
}

variable "ami-id" {
  type = string
  description = "AMI ID with existing configurations(optional)"
}
