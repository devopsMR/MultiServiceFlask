FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY worker-service.py /app/

ENV WORKER_HOST="0.0.0.0"
ENV WORKER_PORT=5002

EXPOSE 5002

CMD ["python", "worker-service.py"]