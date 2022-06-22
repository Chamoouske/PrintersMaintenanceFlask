from flask import render_template

def homepage():
    return render_template('home.html', selected='home')