import os
from dotenv import load_dotenv
import subprocess

load_dotenv()


def main():

    env = os.environ.copy()

    backend_process = subprocess.Popen(
        ["python", "backend/worker-service.py"], env=env
    )

    frontend_process = subprocess.Popen(
        ["python", "frontend/web-service.py"], env=env
    )

    backend_process.communicate()
    frontend_process.communicate()

if __name__ == "__main__":
    main()
