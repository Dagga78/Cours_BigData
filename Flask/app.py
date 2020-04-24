from flask import Flask, render_template, url_for, json, jsonify, request
import os
app = Flask(__name__)

with open('../data/books.json') as json_file:
    data = json.load(json_file)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/books')
def books():
	data = json.load(open(json_url))
	return jsonify(data)

@app.route('/books/<isbn>')
def book(isbn):
	for row in data:
		for attribute, value in row.items():
			if(attribute == "isbn" and value==isbn):
				return row

if __name__ == "__main__":
    app.run()