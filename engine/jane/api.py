# all interfaces go through an HTTP API

from flask import Flask, request, jsonify
from .engine import step
app = Flask(__name__)


@app.route('/step', methods=['POST'])
def step_endpoint():
    data = request.get_json(force=True)
    input_string = data.get('input_string', '')
    output, history = step(input_string)
    return jsonify({"output": output, "history": history})


# basic ping endpoint
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify("pong")


def main():
    app.run(host='0.0.0.0', port=4000, debug=True)
