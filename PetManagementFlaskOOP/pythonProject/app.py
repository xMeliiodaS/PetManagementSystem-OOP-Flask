from flask import Flask, render_template, request, redirect, url_for

from load_json import load_data, save_data

app = Flask(__name__)
data = load_data()


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/owner')
def owner_page():
    return render_template('owner_page.html')
