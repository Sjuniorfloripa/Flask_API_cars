from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.models import Carro


def init_routes(app):

    @app.route('/carros', methods=['GET'])
    @jwt_required()
    def get_carros():
        carros = Carro.query.all()
        return jsonify([carro.to_dict() for carro in carros])

    @app.route('/carros', methods=['POST'])
    @jwt_required()
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

    @app.route('/carros/<int:id>', methods=['GET'])
    @jwt_required()
    def get_carro(id):
        carro = Carro.query.get(id)
        if not carro:
            return jsonify({"erro": "Carro não encontrado"}), 404
        return jsonify(carro.to_dict()), 200

    @app.route('/carros/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_carro(id):
        carro = Carro.query.get(id)
        if not carro:
            return jsonify({"erro": "Carro não encontrado"}), 404
        
        data = request.json
        carro.marca = data['marca']
        carro.modelo = data['modelo']
        carro.ano = data.get('ano', carro.ano)
        
        db.session.commit()
        return jsonify(carro.to_dict()), 200

    @app.route('/carros/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_carro(id):
        carro = Carro.query.get(id)
        if not carro:
            return jsonify({"erro": "Carro não encontrado"}), 404
        
        db.session.delete(carro)
        db.session.commit()
        return '', 204