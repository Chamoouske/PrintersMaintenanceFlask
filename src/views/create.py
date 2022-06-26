from flask import render_template

def create_printer(error=False,saved=False, table_ok=False):
    return render_template('create.html', table_ok=table_ok, selected='new_printer', error=error, saved=saved)