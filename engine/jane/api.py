# all interfaces go through an HTTP API

from flask import Flask, request, jsonify
from .engine import step
import uuid
app = Flask(__name__)


@app.route('/step/<session_id>', methods=['POST'])
def step_id_endpoint(session_id: str):
    input_string = request.get_data(as_text=True)
    output, history = step(session_id, input_string)
    return jsonify({"output": output, "history": history, "session_id": session_id})


@app.route('/step', methods=['POST'])
def step_endpoint():
    """raw /step endpoint that generates a new UUID id for the session.
       used to start a new session"""
    session_id = uuid.uuid4()
    return step_id_endpoint(session_id)


# basic ping endpoint
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify("pong")


def main():
    app.run(host='0.0.0.0', port=4000, debug=True)
