import os
from dotenv import load_dotenv
import subprocess

# Load environment variables from the .env file into os.environ
load_dotenv()


def main():
    # Pass all environment variables (including .env) explicitly
    env = os.environ.copy()

    # Start the backend process with the full environment
    backend_process = subprocess.Popen(
        ["python", "backend/worker-service.py"], env=env
    )

    # Start the frontend process with the full environment
    frontend_process = subprocess.Popen(
        ["python", "frontend/web-service.py"], env=env
    )

    # Optionally, wait for processes to complete
    backend_process.communicate()
    frontend_process.communicate()


if __name__ == "__main__":
    main()
