resource "aws_key_pair" "k8s-lab-instance" {
  key_name   = "k8s-lab-instance"
  public_key = file("${path.module}/files/k8s_lab_rsa.pub")
  provisioner "generate-key-pair" {
    command = "echo ${self.private_ip} >> private_ips.txt"
  }
}

data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "k8s-lab-instance" {
  ami             = data.aws_ami.ubuntu.id
  instance_type   = "t2.medium"
  key_name        = aws_key_pair.k8s-lab-instance.key_name
  security_groups = [aws_security_group.k8s-lab-sg.id]
  subnet_id       = data.aws_subnet.default_subnet.id

  root_block_device {
    volume_size = 30
    volume_type = "standard"
  }

  user_data_base64 = filebase64("${path.module}/files/userdata.sh")
}
