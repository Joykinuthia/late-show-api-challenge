from flask import Blueprint, jsonify

guest_bp = Blueprint('guest', __name__, url_prefix='/guests')

@guest_bp.route('/', methods=['GET'])
def get_guests():
    return jsonify({'message': 'List of guests'})
