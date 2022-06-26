from flask import render_template

printers = {
        'identify':['123', '234', '567'],
        'model':['Epson', 'Brother', 'Teste2'],
        'sector': ['TI', 'Teste2', 'teste3'],
        'date_purchased': ['2-2-2', '1-1-1', '6-6-6'],
        'maintenances': [0, 5, 6]
    }

def homepage():
    length = len(printers['identify'])
    return render_template('home.html', selected='home', printers=printers, length=length)