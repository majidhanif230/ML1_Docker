from flask import Flask

app = Flask(__name__)

@app.route('/')
def server1():
    return "Server 1"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
