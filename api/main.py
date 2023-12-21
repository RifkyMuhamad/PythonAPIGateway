from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("DyoneStrankers use Flask")

@app.route("/about")
def about():
    return jsonify("DyoneStrankers in about")