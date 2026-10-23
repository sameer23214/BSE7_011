from flask import Flask
import socket, datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Hello from BSE7-11 (Docker Lab)</h1>
    <p>Owner: sameer12354we5</p>
    <p>Container ID: {socket.gethostname()}</p>
    <p>Time: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}</p>
    """

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
