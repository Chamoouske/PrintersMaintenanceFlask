import sys
from pathlib import Path

from flask import Flask
from views.home import homepage
from views.about import page_about
from views.create import create_printer

file = Path(__file__).resolve()
sys.path.append('.')
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

app = Flask(__name__,
        static_url_path='/views/static',
        static_folder='views/static',
        template_folder='views/templates'
    )

@app.route('/', methods=['GET'])
def home():
    return homepage()


@app.route('/cadastro')
def create_new_printer():
    return create_printer()

@app.route('/sobre')
def about_app():
    return page_about()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)