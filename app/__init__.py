from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
cache = Cache()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    cache.init_app(app)
    jwt.init_app(app)

    from app.routes.bookings import booking_bp
    from app.auth import auth_bp
    app.register_blueprint(booking_bp)
    app.register_blueprint(auth_bp)

    return app
