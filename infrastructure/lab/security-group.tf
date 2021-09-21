resource "aws_security_group" "k8s-lab-sg" {
  name        = "k8s-lab-sg"
  description = "Allow traffic to k8s lab instance"
  vpc_id      = data.aws_vpc.default_vpc.id
}

resource "aws_security_group_rule" "k8s-lab-ingress-ssh" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  ipv6_cidr_blocks  = ["::/0"]
  security_group_id = aws_security_group.k8s-lab-sg.id
}

resource "aws_security_group_rule" "k8s-lab-ingress-http" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  ipv6_cidr_blocks  = ["::/0"]
  security_group_id = aws_security_group.k8s-lab-sg.id
}

resource "aws_security_group_rule" "k8s-lab-egress-all" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = -1
  cidr_blocks       = ["0.0.0.0/0"]
  ipv6_cidr_blocks  = ["::/0"]
  security_group_id = aws_security_group.k8s-lab-sg.id
}
