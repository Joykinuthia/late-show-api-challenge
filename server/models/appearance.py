from server.models import db

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
    # Add more fields as needed
