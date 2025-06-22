# Late Show API Challenge

This project is a RESTful API for managing guests, episodes, and appearances for a late show. Built with Flask and SQLAlchemy.

## Project Structure

```
server/
├── app.py                # Main Flask app entry point
├── config.py             # Configuration settings
├── seed.py               # Database seeding script
├── models/               # SQLAlchemy models
│   ├── __init__.py
│   ├── guest.py
│   ├── episode.py
│   ├── appearance.py
│   └── user.py
├── controllers/          # Flask Blueprints/controllers
│   ├── __init__.py
│   ├── guest_controller.py
│   ├── episode_controller.py
│   ├── appearance_controller.py
│   └── auth_controller.py
migrations/               # Database migrations (Alembic/Flask-Migrate)
challenge-4-lateshow.postman_collection.json  # Postman API collection
README.md                 # Project documentation
```

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy flask-migrate
   ```
2. Set up the database and run migrations.
3. Run the app:
   ```bash
   python server/app.py
   ```

## API Endpoints
- `/guests/` - Manage guests
- `/episodes/` - Manage episodes
- `/appearances/` - Manage appearances
- `/auth/` - Authentication endpoints

See the Postman collection for example requests.
