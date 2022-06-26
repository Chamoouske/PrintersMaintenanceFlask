import sys
from pathlib import Path

from flask import Flask, request
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

@app.route('/')
def home():
    return homepage()

@app.route('/cadastro')
def create_new_printer():
    return create_printer()

@app.route('/new_printer', methods=['POST'])
def new_printer():
    mac = request.form['mac']
    model = request.form['model']
    sector = request.form['sector']
    purchased_date = request.form['purchased_date']
    date_maintenance = request.form['date_maintenance']
    reason_maintenance = request.form['reason_maintenance']
    if mac == '' or model == '':
        return create_printer(error=True)
    mac = mac.replace("'", "[']")
    return create_printer(saved=True)

@app.route('/sobre')
def about_app():
    return page_about()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)