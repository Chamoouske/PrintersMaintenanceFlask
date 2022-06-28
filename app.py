import sys
from pathlib import Path
file = Path(__file__).resolve()
sys.path.append('.')
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


from src.main import app


if __name__ == '__main__':
    app.run(debug=True)