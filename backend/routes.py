# backend/routes.py
from flask import jsonify, Blueprint, request
import requests

bp = Blueprint('api', __name__)

@bp.route('/')
def home():
    return jsonify({"msg": "API Pokémon Flask ativa!"})

# 🔹 Listar pokémons (com paginação)
@bp.route('/pokemons', methods=['GET'])
def listar_pokemons():
    limit = request.args.get('limit', 20)
    offset = request.args.get('offset', 0)
    url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}'
    r = requests.get(url)
    data = r.json()

    # Simplifica os dados
    resultados = []
    for item in data['results']:
        detalhes = requests.get(item['url']).json()
        resultados.append({
            'id': detalhes['id'],
            'nome': detalhes['name'],
            'imagem': detalhes['sprites']['front_default'],
            'tipos': [t['type']['name'] for t in detalhes['types']]
        })

    return jsonify(resultados)

# 🔹 Buscar pokémon por nome ou ID
@bp.route('/pokemons/<nome_ou_id>', methods=['GET'])
def buscar_pokemon(nome_ou_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome_ou_id.lower()}'
    r = requests.get(url)

    if r.status_code != 200:
        return jsonify({'erro': 'Pokémon não encontrado'}), 404

    dados = r.json()
    return jsonify({
        'id': dados['id'],
        'nome': dados['name'],
        'imagem': dados['sprites']['front_default'],
        'tipos': [t['type']['name'] for t in dados['types']]
    })
