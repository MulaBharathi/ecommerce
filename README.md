# E-Commerce Microservices Application

This project is a cloud-native e-commerce application using a microservices architecture, containerization, CI/CD, Kubernetes deployment, and monitoring.

## Microservices

- **User Service** – User registration and authentication
- **Product Service** – Product listing and management
- **Order Service** – Order placement and tracking



## Build Docker Images
# Build images for each service

```
docker build -t bharu2703/user-service:latest ./user-service
docker build -t bharu2703/product-service:latest ./product-service
docker build -t bharu2703/order-service:latest ./order-service
```

# Push to DockerHub

```
docker push bharu2703/user-service:latest
docker push bharu2703/product-service:latest
docker push bharu2703/order-service:latest
```

# ☸️ Apply Kubernetes Manifests

# Apply all manifests

```
kubectl apply -f k8s/
```