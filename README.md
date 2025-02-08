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
The `minikube image load` command is used to load a local Docker image into the Minikube Kubernetes cluster
minikube image load worker-service:latest 
minikube image load web-service:latest
1. **`minikube service`**:
    - It allows you to access a specific Kubernetes service running in Minikube.
    - This command retrieves the IP and port of the service and opens it in your default web browser (if possible).
minikube service frontend-service -n multi-service-app
