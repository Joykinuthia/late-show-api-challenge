from server.models import db

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.Text)
    # Add more fields as needed
