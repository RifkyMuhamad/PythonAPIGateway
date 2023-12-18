from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DyoneStrankers use Flask"

@app.route("/about")
def about():
    return "DyoneStrankers in about"