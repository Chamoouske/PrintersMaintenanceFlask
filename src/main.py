import sys
from pathlib import Path

from flask import Flask, request, redirect
from controller.data_manager import create_tables_db, verify_tables
from views.home import homepage
from views.about import page_about
from views.create import create_printer

file = Path(__file__).resolve()
sys.path.append('.')
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

app = Flask(__name__,
        static_url_path='/static',
        static_folder='static',
        template_folder='views/templates'
    )

error = False
@app.route('/')
def home():
    global error
    error = verify_tables()
    return homepage(table_ok=error)

@app.route('/create_tables')
def create_tables():
    global error
    error = create_tables_db()
    return redirect('/')

@app.route('/cadastro')
def create_new_printer():
    global error
    return create_printer(table_ok=error)

@app.route('/new_printer', methods=['POST'])
def new_printer():
    identify = request.form['identify']
    model = request.form['model']
    sector = request.form['sector']
    purchased_date = request.form['purchased_date']
    date_maintenance = request.form['date_maintenance']
    reason_maintenance = request.form['reason_maintenance']
    if identify == '' or model == '':
        return create_printer(error=True)
    return create_printer(saved=True)

@app.route('/sobre')
def about_app():
    global error
    return page_about(table_ok=error)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)