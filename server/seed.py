# Seed script for initial data
from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User
import datetime

def seed():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        # Add seed data here
        user1 = User(username='admin')
        user1.set_password('adminpass')
        db.session.add(user1)

        guest1 = Guest(name='John Doe', occupation='Comedian')
        guest2 = Guest(name='Jane Smith', occupation='Actor')
        db.session.add_all([guest1, guest2])

        episode1 = Episode(date=datetime.date(2025, 6, 1), number=1)
        episode2 = Episode(date=datetime.date(2025, 6, 2), number=2)
        db.session.add_all([episode1, episode2])

        db.session.flush()  # Ensure IDs are set

        appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
        appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
        db.session.add_all([appearance1, appearance2])

        db.session.commit()
        print('Database seeded!')

if __name__ == "__main__":
    seed()
