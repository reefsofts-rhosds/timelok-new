from flask import Flask, jsonify
import locklib 

app = Flask(__name__)

@app.route('/lock', methods=['GET'])
def lock():
    # Lock the computer
    locklib.lock()

@app.route('/unlock', methods=['GET'])
def unlock():
    # Maybe a short description?
    locklib.unlock()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)