import sys
from flask import Flask

print("Starting Flask app...", file=sys.stderr)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from my CI/CD Pipeline!"

if __name__ == '__main__':
    print("Running on 0.0.0.0:5000", file=sys.stderr)
    app.run(host='0.0.0.0', port=5000, debug=True)
