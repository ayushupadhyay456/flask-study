from flask import Flask 
from auth import auth



app=Flask(__name__)

app.config['SECRET_KEY'] = 'dev-key-placeholder'
app.register_blueprint(auth,url_prefix='/')



if __name__=='__main__':
    app.run('0.0.0.0',debug=True)







