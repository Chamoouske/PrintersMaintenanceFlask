from flask import render_template

def create_printer(error=False,saved=False):
    return render_template('create.html', selected='new_printer', error=error, saved=saved)