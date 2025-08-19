from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.models import User

def init_auth_routes(app):
    
    @app.route('/register', methods=['POST'])
    def register():
        data = request.json
        
        if User.query.filter_by(username=data['username']).first():
            return jsonify({"erro": "Usuário já existe"}), 400
        
        user = User(username=data['username'])
        user.set_password(data['password'])
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({"mensagem": "Usuário criado com sucesso"}), 201
    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        user = User.query.filter_by(username=data['username']).first()
        
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=str(user.id))
            return jsonify({
                "access_token": access_token,
                "user": user.to_dict()
            }), 200
        
        return jsonify({"erro": "Credenciais inválidas"}), 401
    
    @app.route('/profile', methods=['GET'])
    @jwt_required()
    def profile():
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        return jsonify(user.to_dict())