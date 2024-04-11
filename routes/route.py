from flask import Flask
from app import app

@app.route('/')
def index():
    return "Hello, this is the homepage!"

@app.route('/about')
def about():
    return "About page"

@app.route('/contact')
def contact():
    return "Contact page"
