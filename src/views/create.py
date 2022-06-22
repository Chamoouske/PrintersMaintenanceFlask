from flask import render_template

def create_printer():
    return render_template('create.html', selected='new_printer')