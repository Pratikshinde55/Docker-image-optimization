from flask import Flask
import sys

app = Flask(__name__)

#data = sys.argv[1]
data = sys.argv[1] if len(sys.argv) > 1 else 'Guest'

@app.route("/info")
def ps():
    return f"welcome to my world..mr.{data}..\n"

app.run(host='0.0.0.0', port=5000)
