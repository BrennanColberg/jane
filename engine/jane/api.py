# all interfaces go through an HTTP API

from flask import Flask, request, jsonify
from .engine import step
app = Flask(__name__)


@app.route('/step/<session_id>', methods=['POST'])
def step_endpoint(session_id):
    input_string = request.get_data(as_text=True)
    output, history = step(session_id, input_string)
    return jsonify({"output": output, "history": history, "session_id": session_id})


# basic ping endpoint
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify("pong")


def main():
    app.run(host='0.0.0.0', port=4000, debug=True)
