from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("=========================================================")
    print("🚀 Heritage Treasures UNESCO Web Analytics Dashboard Live")
    print("   Running on http://127.0.0.1:5000")
    print("=========================================================")
    app.run(host='0.0.0.0', port=5000, debug=True)
