from flask import Flask, render_template,jsonify

from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")

from pymongo import MongoClient

# localhost 용 MongoDB 연결
client = MongoClient("localhost", 27017)

# 서버용 MongoDB 연결
# client = MongoClient('mongodb://test:test@localhost', 27017)

db = client.mapCrawlingPrac
addresses = []

# html 렌더링
@app.route("/")
def home():
    return render_template("index.html", CLIENT_ID=CLIENT_ID)

# api

# 데이터 가져오기
@app.route("/map/marker", methods=["GET"])
def marker():
    shopdata = list(db.shops.find({},{"_id":False}))

    return jsonify({"shopdatas":shopdata})

# Flask 시작

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)