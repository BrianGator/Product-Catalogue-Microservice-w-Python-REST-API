import os
from flask import Flask
from service.models import db

# Create Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI", "sqlite:///../development.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret-for-dev"

# Import routes and error handlers after app is created to avoid circular imports
from service import routes, models
from service.common import error_handlers

# Initialize SQLAlchemy
models.init_db(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
