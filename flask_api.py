from flask import Flask, jsonify, request
from run_all import printI

app = Flask(__name__)

# @app.route('/')
# def index():
#     return jsonify(printI())

@app.route('/get/run_all_ahi', methods = ['GET'])
def run_all():
    result = printI()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)