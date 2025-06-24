# Late Show API Challenge

This is a comprehensive Flask REST API for managing a Late Night TV show system, designed and implemented by Joyrose Kinuthia. This project demonstrates best practices in Python backend development, including MVC architecture, PostgreSQL integration, JWT authentication, and robust API documentation and testing.

---

## 📄 Description

This API allows you to manage late night TV show data, including users, guests, episodes, and guest appearances. It features:
- Secure user registration and login with JWT-based authentication
- Full CRUD for episodes, guests, and appearances
- Protected endpoints for sensitive actions
- PostgreSQL as the database backend
- Seed script for initial data
- Postman collections for easy API testing

---

## 📁 Folder Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
├── challenge-4-lateshow-alt.postman_collection.json
├── challenge-4-lateshow-another.postman_collection.json
├── Pipfile
├── .gitignore
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install Dependencies
```bash
pipenv install
pipenv shell
```

### 3. PostgreSQL Database Setup
- Ensure PostgreSQL is running.
- Create the database:

```sql
CREATE DATABASE late_show_db;
```

- Update `server/config.py` with your DB credentials if needed:
```
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
```

### 4. Environment Variables
- Optionally, set a custom JWT secret:
```bash
export JWT_SECRET_KEY=your-secret-key
```

### 5. Database Migration & Seeding
```bash
export FLASK_APP=server.app:create_app
flask db init         # Only once, if migrations/ doesn't exist
flask db migrate -m "initial migration"
flask db upgrade
python -m server.seed
```

### 6. Run the Server
```bash
FLASK_APP=server.app:create_app flask run
```

---

## 🔐 Authentication Flow

- **Register:** `POST /register` with `{ "username": "...", "password": "..." }`
- **Login:** `POST /login` with `{ "username": "...", "password": "..." }`
- **Receive JWT:** On successful login, you'll get `{ "access_token": "..." }`
- **Protected Routes:** Send the token in the `Authorization` header:
  - `Authorization: Bearer <access_token>`

---

## 🛣️ API Routes

| Route                        | Method | Auth Required | Description                        |
|------------------------------|--------|--------------|------------------------------------|
| `/register`                  | POST   | ❌           | Register a new user                |
| `/login`                     | POST   | ❌           | Log in and receive JWT             |
| `/episodes`                  | GET    | ❌           | List all episodes                  |
| `/episodes/<int:id>`         | GET    | ❌           | Get episode details + appearances  |
| `/episodes/<int:id>`         | DELETE | ✅           | Delete episode + appearances       |
| `/guests`                    | GET    | ❌           | List all guests                    |
| `/appearances`               | POST   | ✅           | Create a new appearance            |

### Sample Requests & Responses

#### Register
```
POST /register
{
  "username": "testuser",
  "password": "testpass"
}
Response: { "message": "User registered" }
```

#### Login
```
POST /login
{
  "username": "testuser",
  "password": "testpass"
}
Response: { "access_token": "..." }
```

#### Create Appearance (Protected)
```
POST /appearances
Headers: Authorization: Bearer <access_token>
{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
Response: { "id": 1, "rating": 5, "guest_id": 1, "episode_id": 1 }
```

#### Delete Episode (Protected)
```
DELETE /episodes/1
Headers: Authorization: Bearer <access_token>
Response: { "message": "Episode deleted" }
```

---

## 🧪 Testing with Postman

1. Import any of the provided Postman collections (e.g., `challenge-4-lateshow-alt.postman_collection.json`) into Postman.
2. Register and log in to get your JWT token.
3. For protected routes, set the `Authorization` header:
   - `Bearer <access_token>`
4. Test all endpoints as described above.

---

## 📝 Project Details

- **Database:** PostgreSQL (no SQLite)
- **Auth:** JWT (Flask-JWT-Extended)
- **Password Security:** Passwords are hashed
- **Cascade Delete:** Deleting an episode or guest deletes related appearances
- **Validation:** Appearance `rating` must be 1-5
- **Seed Data:** Provided in `server/seed.py`
- **MVC Structure:** Models, Controllers, App

---

## 📎 GitHub Repository

[GitHub Repo Link](https://github.com/Joykinuthia/late-show-api-challenge)

---
Joyrose Kinuthia

## © 2025 Late Show API Challenge
