from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html', title='Analysis')

@app.route('/classify')
def classify():
    return render_template('classify.html', title='Classify')

@app.route('/detail')
def detail():
    return render_template('detail.html', title='Detail')




