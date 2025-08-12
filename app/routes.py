from flask import jsonify, request
from app import db
from app.models import Carro


def init_routes(app):
    @app.route('/carros', methods=['GET'])
    def get_carros():
        carros = Carro.query.all()
        return jsonify([carro.to_dict() for carro in carros])

    @app.route('/carros', methods=['POST'])
    def create_carro():
        data = request.json
        novo_carro = Carro(
            marca=data['marca'],
            modelo=data['modelo'],
            ano=data['ano']
        )
        db.session.add(novo_carro)
        db.session.commit()
        return jsonify(novo_carro.to_dict()), 201