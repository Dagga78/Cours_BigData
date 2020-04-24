from flask import Flask, render_template, url_for, json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

df = pd.read_csv("../data/labels.csv", ",", encoding='utf-8', low_memory=False)

@app.route('/')
def index():
    return "Hello world!"

@app.route('/labels')
def labels():
    return df.to_string()

if __name__ == "__main__":
    app.run()