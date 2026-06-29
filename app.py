from flask import Flask 
from flask_wtf import FlaskForm

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'


@app.route('/hello')
def helloee():
    return 'this is the hello page'

if __name__=='__main__': 
    app.run(host='0.0.0.0',debug=True)





