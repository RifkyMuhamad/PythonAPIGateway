from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "DyoneStrankers use Flask"
    })

@app.route("/about")
def about():
    return jsonify({
        "message": "DyoneStrankers in about"
    })