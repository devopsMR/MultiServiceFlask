FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV WEB_HOST="0.0.0.0"
ENV WEB_PORT=5001
ENV WEB_WORKER_HOST="127.0.0.1"
ENV WEB_WORKER_PORT=5002

EXPOSE 5001

CMD ["python", "web-service.py"]