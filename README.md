# Running the App with Docker Compose
1. **Download files**  
   Clone this repository to your local machine.
2. **Run the app using Docker Compose**  
   Open a terminal, navigate to the project directory where the `docker-compose.yml` file is located, and run the
   following command:
   ```bash
   docker-compose up -d
   ```
3. **Access the application**  
   Access the application at [http://localhost:5001](http://localhost:5001)
4. **Stop the application**  
   To stop the running containers, execute the following command:
   ```bash
   docker-compose down
   ```

local Docker image
The `minikube image load` command is used to load a local Docker image into the Minikube Kubernetes cluster
minikube image load worker-service:latest 
minikube image load web-service:latest
apply all files
 kubectl apply -f ...


ECR Docker image
authenticates Docker to your **Amazon Elastic Container Registry (ECR)** so it can securely push or pull images from the specified ECR repository
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 057724841053.dkr.ecr.us-east-1.amazonaws.com

aws ecr create-repository --repository-name worker-service
aws ecr create-repository --repository-name web-service

docker tag web-service:latest 057724841053.dkr.ecr.us-east-1.amazonaws.com/web-service
docker tag worker-service:latest 057724841053.dkr.ecr.us-east-1.amazonaws.com/worker-service

docker push 057724841053.dkr.ecr.us-east-1.amazonaws.com/web-service:latest
docker push 057724841053.dkr.ecr.us-east-1.amazonaws.com/worker-service:latest

kubectl create secret docker-registry ecr-secret --docker-server=057724841053.dkr.ecr.us-east-1.amazonaws.com --docker-username=AWS --docker-password=$(aws ecr get-login-password --region us-east-1) -n multi-service-app

apply all files
 kubectl apply -f ...

# Running the App

## Using Docker Compose

1. **Clone the repository**  
   Download this repository to your local machine.

2. **Run the app with Docker Compose**  
   Navigate to the project directory where `docker-compose.yml` is located and execute:
   ```bash
   docker-compose up -d
   ```

3. **Access the application**  
   Open your browser and go to: [http://localhost:5001](http://localhost:5001)

4. **Stop the application**  
   To stop the running containers, execute:
   ```bash
   docker-compose down
   ```

---

## Using Kubernetes with Local Images

1. **Load Local Docker Images into Minikube**
   ```bash
   minikube image load worker-service:latest
   minikube image load web-service:latest
   ```

2. **Apply Kubernetes Configuration Files**
   ```bash
   kubectl apply -f .
   ```

3. **Access the Application**  
   Use the following command to retrieve the service URL:
   ```bash
   minikube service frontend-service -n multi-service-app
   ```

---

## Using Kubernetes with ECR Images

1. **Authenticate with ECR**
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your-ecr-repository-url>
   ```

2. **Tag and Push Images to ECR**
   ```bash
   docker tag web-service:latest <your-ecr-repository-url>/web-service:latest
   docker tag worker-service:latest <your-ecr-repository-url>/worker-service:latest

   docker push <your-ecr-repository-url>/web-service:latest
   docker push <your-ecr-repository-url>/worker-service:latest
   ```

3. **Create Kubernetes Secret for ECR**
   ```bash
   kubectl create secret docker-registry ecr-secret \
       --docker-server=<your-ecr-repository-url> \
       --docker-username=AWS \
       --docker-password=$(aws ecr get-login-password --region us-east-1) \
       -n multi-service-app
   ```

4. **Apply Kubernetes Configuration Files**
   ```bash
   kubectl apply -f .
   ```

5. **Access the Application**  
   Retrieve the service URL:
   ```bash
   minikube service frontend-service -n multi-service-app
   ```
1.**`minikube service`**:
    - It allows you to access a specific Kubernetes service running in Minikube.
    - This command retrieves the IP and port of the service and opens it in your default web browser (if possible).
minikube service frontend-service -n multi-service-app