from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("index.html")
    
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


