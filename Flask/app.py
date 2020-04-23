from flask import Flask
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/books')
def books():
    df = pd.read_json("../data/books.json")
    df.to_json()

if __name__ == "__main__":
    app.run()