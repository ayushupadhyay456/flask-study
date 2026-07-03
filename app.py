from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# 1. Initialize DB extension
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    
    # 2. Configure app
    app.config['SECRET_KEY'] = 'dev-key-placeholder'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # 3. Bind the DB to this app
    db.init_app(app)
    
    # 4. IMPORT BLUEPRINTS HERE (Breaks circular dependency)
    from auth import auth
    from views import views  # assuming you have a views file too
    
    # 5. Register Blueprints
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    
    # 6. Import models and create tables inside the app context
    from models import User, Note
    create_database(app)
    
    return app

def create_database(app):
    # Checks if the database file exists in your project directory
    if not path.exists(path.join(path.abspath(path.dirname(__file__)), DB_NAME)):
        with app.app_context():
            db.create_all()
        print('Created Database!')

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)