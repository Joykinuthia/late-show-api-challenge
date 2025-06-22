# Main entry point for the Flask app
from flask import Flask
from server.config import Config
from server.models import *
from server.controllers import register_blueprints

app = Flask(__name__)
app.config.from_object(Config)

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)
