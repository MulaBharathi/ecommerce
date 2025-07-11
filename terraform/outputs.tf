output "eks_cluster_endpoint" {
  value = aws_eks_cluster.ecommerce_eks.endpoint
}

output "eks_cluster_name" {
  value = aws_eks_cluster.ecommerce_eks.name
}

output "eks_cluster_arn" {
  value = aws_eks_cluster.ecommerce_eks.arn
}
