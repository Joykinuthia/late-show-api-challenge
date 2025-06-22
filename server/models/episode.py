from server.models import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    air_date = db.Column(db.Date)
    # Add more fields as needed
