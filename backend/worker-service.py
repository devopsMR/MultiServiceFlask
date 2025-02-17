import os
from flask import Flask, request, jsonify
from flask.cli import load_dotenv
from db_connection import get_reversed_text_from_db, insert_text_into_db

# Load environment variables from .env file
load_dotenv()

worker_app = Flask(__name__)


@worker_app.route('/process', methods=['POST'])
def process_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input, 'text' is required"}), 400

    text = data['text']

    # Check if the text already exists in the database
    reversed_text = get_reversed_text_from_db(text)
    if reversed_text:
        return jsonify({
            "word_count": len(text.split()),
            "reversed_text": reversed_text,
            "source": "database"
        })

    # If text doesn't exist, process and insert into the database
    reversed_text = text[::-1]
    insert_text_into_db(text, reversed_text)

    return jsonify({
        "word_count": len(text.split()),
        "reversed_text": reversed_text,
        "source": "calculated"
    })


if __name__ == '__main__':
    WORKER_HOST = os.getenv('WORKER_HOST')
    WORKER_PORT = os.getenv('WORKER_PORT')
    worker_app.run(host=WORKER_HOST, port=WORKER_PORT, debug=True)
