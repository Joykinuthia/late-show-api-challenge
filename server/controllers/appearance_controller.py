from flask import Blueprint, jsonify

appearance_bp = Blueprint('appearance', __name__, url_prefix='/appearances')

@appearance_bp.route('/', methods=['GET'])
def get_appearances():
    return jsonify({'message': 'List of appearances'})
