from flask import Flask 
from config import Config 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    from .extensions import db, migrate
    
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from .api import api_bp
    from .blog import blog_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(blog_bp)


app = create_app()