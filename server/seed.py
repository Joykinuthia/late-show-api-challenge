# Script to seed the database with initial data
from server.models import db, Guest, Episode, Appearance, User
from server.app import app

with app.app_context():
    db.drop_all()
    db.create_all()
    # Add your seed data here
    print("Database seeded!")
