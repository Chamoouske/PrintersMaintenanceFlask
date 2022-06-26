from flask import render_template

def page_about(table_ok=False):
    return render_template('about.html', table_ok=table_ok, selected='about')