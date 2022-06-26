from flask import render_template

printers = {
        'identify':['123', '234', '567'],
        'model':['Epson', 'Brother', 'Teste2'],
        'sector': ['TI', 'Teste2', 'teste3'],
        'date_purchased': ['2-2-2', '1-1-1', '6-6-6'],
        'maintenances': [0, 5, 6]
    }

def homepage(table_ok):
    length = len(printers['identify'])
    return render_template('home.html', table_ok=table_ok, selected='home', printers=printers, length=length)

def create_printer(error=False,saved=False, table_ok=False):
    return render_template('create.html', table_ok=table_ok, selected='new_printer', error=error, saved=saved)

def page_about(table_ok=False):
    return render_template('about.html', table_ok=table_ok, selected='about')