from flask import Flask,render_template,request
from flask import Blueprint


auth=Blueprint('auth',__name__)


@auth.route('/login',methods=['get','post'])

def login():
    data=request.form
    print(data)
    return render_template('login.html',user=None)

@auth.route('/Sign-up')

def signup():
    return render_template('sign_up.html',user=None)