### 1. Build and push all 3 Docker 
```
docker build -t bharu2703/order-service:latest ./order-service
docker push bharu2703/order-service:latest

docker build -t bharu2703/product-service:latest ./product-service
docker push bharu2703/product-service:latest

docker build -t bharu2703/user-service:latest ./user-service
docker push bharu2703/user-service:latest
```

### 2.Apply Kubernetes deployments:

```
kubectl apply -f order-service/k8s/
kubectl apply -f product-service/k8s/
kubectl apply -f user-service/k8s/
```

