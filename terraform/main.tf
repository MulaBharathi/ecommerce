provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "ecommerce_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "ecommerce-vpc"
  }
}

resource "aws_subnet" "ecommerce_subnet" {
  vpc_id = aws_vpc.ecommerce_vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-west-2a"
  map_public_ip_on_launch = true
  tags = {
    Name = "ecommerce-subnet"
  }
}

resource "aws_eks_cluster" "ecommerce_eks" {
  name = "ecommerce-cluster"
  role_arn = aws_iam_role.eks_role.arn
  vpc_config {
    subnet_ids = [aws_subnet.ecommerce_subnet.id]
  }
}

resource "aws_iam_role" "eks_role" {
  name = "ecommerce-eks-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Principal = {
          Service = "eks.amazonaws.com"
        }
        Effect = "Allow"
        Sid = ""
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "eks_policy_attach" {
  role       = aws_iam_role.eks_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}

