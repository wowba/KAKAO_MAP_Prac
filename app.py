from flask import Flask, render_template

from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")

@app.route("/")
def home():
    return render_template("index.html", CLIENT_ID=CLIENT_ID)


# Flask 시작

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)