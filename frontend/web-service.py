import os
from flask import Flask, render_template, request, jsonify
import http.client
import json
from flask.cli import load_dotenv

# Load environment variables from .env file
load_dotenv()

web_app = Flask(__name__)

# Base URL of worker service
WORKER_HOST = os.getenv('WEB_WORKER_HOST')
WORKER_PORT = os.getenv('WEB_WORKER_PORT')
WORKER_URL = f"{WORKER_HOST}:{WORKER_PORT}"


@web_app.route('/')
def index():
    return render_template('index.html')


@web_app.route('/submit', methods=['POST'])
def submit_text():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        connection = http.client.HTTPConnection(f"{WORKER_URL}")
        payload = json.dumps({"text": text})
        headers = {'Content-Type': 'application/json'}

        connection.request("POST", "/process", body=payload, headers=headers)
        response = connection.getresponse()
        response_data = response.read().decode()

        if response.status != 200:
            return jsonify({"error": "Error communicating with backend"}), 500

        return jsonify(json.loads(response_data))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    WEB_HOST = os.getenv('WEB_HOST')
    WEB_PORT = os.getenv('WEB_PORT')
    web_app.run(host=WEB_HOST, port=WEB_PORT, debug=True)
