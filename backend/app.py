# backend/app.py
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from extensions import db

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # cria app.db dentro de backend/
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'secreta123'

    db.init_app(app)
    JWTManager(app)

    with app.app_context():
        from routes import bp as api_bp
        app.register_blueprint(api_bp)
        # importar models aqui registra as tabelas no metadata
        from models import Usuario, TipoPokemon, PokemonUsuario
        db.create_all()
        # print opcional pra ver no console:
        try:
            # Flask-SQLAlchemy >=3 removeu table_names(); usar inspector
            from sqlalchemy import inspect
            insp = inspect(db.engine)
            print("✅ Tabelas:", insp.get_table_names())
        except Exception as e:
            print("Aviso ao listar tabelas:", e)

    # importe rotas depois de criar o app (se já existir routes.py)
    try:
        import routes  # noqa: F401
    except Exception:
        pass

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
