from flask import Blueprint, jsonify

episode_bp = Blueprint('episode', __name__, url_prefix='/episodes')

@episode_bp.route('/', methods=['GET'])
def get_episodes():
    return jsonify({'message': 'List of episodes'})
