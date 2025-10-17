# backend/models.py
from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column('IDUsuario', db.Integer, primary_key=True)
    nome = db.Column('Nome', db.String(100), nullable=False)
    login = db.Column('Login', db.String(50), unique=True, nullable=False)
    email = db.Column('Email', db.String(100), unique=True, nullable=False)
    senha = db.Column('Senha', db.String(100), nullable=False)
    dt_inclusao = db.Column('DTInclusao', db.DateTime)
    dt_alteracao = db.Column('DTAlteracao', db.DateTime)

    pokemons = db.relationship('PokemonUsuario', backref='usuario', lazy=True)

class TipoPokemon(db.Model):
    __tablename__ = 'tipopokemon'
    id = db.Column('IDTipoPokemon', db.Integer, primary_key=True)
    descricao = db.Column('Descricao', db.String(50), nullable=False)

class PokemonUsuario(db.Model):
    __tablename__ = 'pokemonusuario'
    id = db.Column('IDPokemonUsuario', db.Integer, primary_key=True)
    usuario_id = db.Column('IDUsuario', db.Integer, db.ForeignKey('usuario.IDUsuario'), nullable=False)
    tipo_id = db.Column('IDTipoPokemon', db.Integer, db.ForeignKey('tipopokemon.IDTipoPokemon'))
    codigo = db.Column('Codigo', db.String(50))
    nome = db.Column('Nome', db.String(100))
    imagem_url = db.Column('ImagemUrl', db.String(255))
    grupo_batalha = db.Column('GrupoBatalha', db.Boolean, default=False)
    favorito = db.Column('Favorito', db.Boolean, default=False)
