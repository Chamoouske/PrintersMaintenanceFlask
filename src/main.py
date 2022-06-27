import sys
from pathlib import Path

from flask import Flask, request, redirect

from controller.validate_fields import validate_fields
from controller.db_manager import *
from views.pages import *

file = Path(__file__).resolve()
sys.path.append('.')
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

app = Flask(__name__,
        static_url_path='/static',
        static_folder='static',
        template_folder='views/templates'
    )

table_exist = False
printers = []
@app.route('/')
def home():
    global table_exist
    global printers
    table_exist = create_tables_db()
    if table_exist:
        printers = get_printers()
    return homepage(table_ok=table_exist, printers=printers)

@app.route('/create_tables')
def create_tables():
    global table_exist
    table_exist = create_tables_db()
    return redirect('/')

@app.route('/cadastro')
def create_new_printer():
    global table_exist
    table_exist = create_tables_db()
    return create_printer(table_ok=table_exist)

@app.route('/new_printer', methods=['POST'])
def new_printer():
    global table_exist
    table_exist = create_tables_db()
    identify = request.form['identify']
    model = request.form['model']
    sector = request.form['sector']
    date_purchased = request.form['date_purchased']
    count_maintenances = request.form['count_maintenances']
    dates_maintenances = []
    reasons = []
    if identify == '' or model == '':
        return create_printer(error=True,table_ok=table_exist)
    for i in range(int(count_maintenances)):
        try:
            dates_maintenances.append(request.form[f'date_maint_{i}'])
            reasons.append(request.form[f'reason_maint_{i}'])
            if reasons[-1] == '':
                reasons.pop()
                dates_maintenances.pop()
        except:
            pass
    saved = validate_fields(identify,model, date_purchased, sector, dates_maintenances, reasons)
    if saved:
        return create_printer(saved=True,table_ok=table_exist)
    else:
        return create_printer(error=True,table_ok=table_exist)

@app.route('/sobre')
def about_app():
    global table_exist
    table_exist = create_tables_db()
    return page_about(table_ok=table_exist)

@app.route('/<identify>')
def details_printer(identify):
    global table_exist
    table_exist = create_tables_db()
    printer = verify_printer(identify)
    if not printer:
        return redirect('/not_exist')
    maintenances = get_maintenances(identify)
    return show_printer_info(printer=printer, maintenances=maintenances, table_ok=table_exist)

@app.route('/edit_printer', methods=['POST'])
def add_maintenances_printer():
    identify = request.form['identify']
    date_maint = request.form['date_maint']
    reason_maint = request.form['reason_maint']
    if reason_maint != '':
        save_maintenances([[date_maint, reason_maint]], identify)
    return redirect(f'/{identify}')

@app.route('/not_exist')
def printer_not_exist():
    return "Não existe mané"

if __name__ == '__main__':
    app.run(debug=True)