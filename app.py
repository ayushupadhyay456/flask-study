from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from auth import auth



app=Flask(__name__)


db=SQLAlchemy()
DB_NAME='database.db'

app.config['SECRET_KEY'] = 'dev-key-placeholder'
app.register_blueprint(auth,url_prefix='/')
app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'

db.init_app(app)

if __name__=='__main__':
    app.run('0.0.0.0',debug=True)







