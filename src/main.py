import sys
from pathlib import Path

from flask import Flask, request, redirect

from src.controller.validate_fields import validate_fields
from src.controller.db_manager import *
from src.views.pages import *

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
    model = request.form['model']
    sector = request.form['sector']
    date_purchased = request.form['date_purchased']
    count_maintenances = request.form['count_maintenances']
    dates_maintenances = []
    reasons = []
    if model == '':
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
    saved = validate_fields(model, date_purchased, sector, dates_maintenances, reasons)
    if saved:
        return create_printer(saved=True,table_ok=table_exist)
    else:
        return create_printer(error=True,table_ok=table_exist)

@app.route('/sobre')
def about_app():
    global table_exist
    table_exist = create_tables_db()
    return page_about(table_ok=table_exist)

@app.route('/<id_printer>')
def details_printer(id_printer):
    global table_exist
    table_exist = create_tables_db()
    id_printer = int(id_printer)
    printer = verify_printer(id_printer)
    if not printer:
        return redirect('/not_exist')
    maintenances = get_maintenances(id_printer)
    return show_printer_info(printer=printer, maintenances=maintenances, table_ok=table_exist)

@app.route('/new_maint', methods=['POST'])
def add_maintenances_printer():
    id_printer = request.form['id_printer']
    id_printer = int(id_printer)
    date_maint = request.form['date_maint']
    reason_maint = request.form['reason_maint']
    if reason_maint != '':
        save_maintenances([[date_maint, reason_maint]], id_printer)
    return redirect(f'/{id_printer}')

@app.route('/delete_maint', methods=['POST'])
def delete_maint():
    id_maint = request.form['id_maint']
    id_printer = request.form['id_printer']
    id_maint = int(id_maint)
    id_printer = int(id_printer)
    if delete_maintenance(id_maint,id_printer):
        return redirect(f'/{id_printer}')
    return redirect('/')

@app.route('/edit_maint', methods=['GET'])
def edite_maint():
    global table_exist
    table_exist = create_tables_db()
    id_maint = request.args['id_maint']
    id_printer = request.args['id_printer']
    id_maint = int(id_maint)
    id_printer = int(id_printer)
    date_maint = request.args['date_maintenance']
    reason = request.args['reason']
    return edit_maintenance([id_maint, id_printer, date_maint, reason], table_ok=table_exist)

@app.route('/update_maint', methods=['POST'])
def update_maintenance():
    id_printer = request.form['id_printer']
    id_maint = request.form['id_maint']
    id_maint = int(id_maint)
    id_printer = int(id_printer)
    date_maint = request.form['date_maint']
    reason_maint = request.form['reason_maint']
    if reason_maint != '':
        update_maintenances([id_maint, date_maint, reason_maint])
    return redirect(f'/{id_printer}')

@app.route('/edit_printer', methods=['GET'])
def edit_printer():
    global table_exist
    table_exist = create_tables_db()
    id_printer = request.args["id_printer"]
    id_printer = int(id_printer)
    model = request.args["model"]
    sector = request.args["sector"]
    date_purchased = request.args["date_purchased"]
    return edit_printer_page([id_printer, model, sector, date_purchased], table_ok=table_exist)

@app.route('/update_printer', methods=['POST'])
def update_printer_page():
    global table_exist
    table_exist = create_tables_db()
    id_printer = request.form['id_printer']
    id_printer = int(id_printer)
    model = request.form['model']
    sector = request.form['sector']
    date_purchased = request.form['date_purchased']
    if not verify_printer(id_printer):
        return redirect('/not_exist')
    if model == '':
        return redirect(f'/{id_printer}')
    update_printer([id_printer, model, sector, date_purchased])
    return redirect(f'/{id_printer}')


@app.route('/<id_printer>', methods=['POST'])
def delete_printer(id_printer):
    global table_exist
    table_exist = create_tables_db()
    id_printer = request.form['id_printer']
    id_printer = int(id_printer)
    printer = verify_printer(id_printer)
    if not printer:
        return redirect('/not_exist')
    delete_printer_db(id_printer)
    return redirect('/')

@app.route('/not_exist')
def printer_not_exist():
    global table_exist
    table_exist = create_tables_db()
    return page_not_exist(table_ok=table_exist)
