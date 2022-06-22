from flask import render_template

def page_about():
    return render_template('about.html', selected='about')