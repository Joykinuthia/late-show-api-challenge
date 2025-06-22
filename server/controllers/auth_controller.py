from flask import Blueprint, jsonify

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify({'message': 'Login endpoint'})
