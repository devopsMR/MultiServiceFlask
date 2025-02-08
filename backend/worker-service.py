import os
from flask import Flask, request, jsonify
from flask.cli import load_dotenv

# Load environment variables from .env file
load_dotenv()

worker_app = Flask(__name__)

@worker_app.route('/process', methods=['POST'])
def process_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input, 'text' is required"}), 400

    text = data['text']
    
    # Word count
    word_count = len(text.split())
    
    # Reverse text
    reversed_text = text[::-1]
    
    return jsonify({
        "word_count": word_count,
        "reversed_text": reversed_text
    })

if __name__ == '__main__':
    WORKER_HOST = os.getenv('WORKER_HOST')
    WORKER_PORT = os.getenv('WORKER_PORT')
    worker_app.run(host=WORKER_HOST, port=WORKER_PORT, debug=True)


