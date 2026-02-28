from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Is Alive 🚀"

@app.route("/health")
def health():
    return {"status": "running"}

def run():
    app.run(
        host="0.0.0.0",
        port=8000,
        threaded=True
    )

def keep_alive():
    t = Thread(target=run)
    t.start()