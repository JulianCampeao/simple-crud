from core import *
from core.modules.controllers import *
from core.modules.data import db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados, se não existirem
    app.run(debug=True)