variable "region" {
  description = "The AWS region to deploy to"
  default = "us-west-2"
}

variable "cluster_name" {
  description = "EKS cluster name"
  default = "ecommerce-cluster"
}

