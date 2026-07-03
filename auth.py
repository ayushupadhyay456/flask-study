from flask import Flask,render_template,request,flash,redirect,url_for
from flask import Blueprint
from models import User
from werkzeug.security import generate_password_hash,check_password_hash




auth=Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])

def login():
    data=request.form
    print(data)
    return render_template('login.html',user=None)

@auth.route('/logout')
def logout():
    return 'this is logoit'

@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')


        if len(email)<4:
            flash('Email must be greater than 4 characters',category='error')
        elif len(firstName)<2:
            flash('First Name must be grater than 2 characters',category='error')
        elif password1 != password2:
            flash('Passwords do not match.',category='error')
        elif len(password1)<7:
             flash('Password must be atleast 7 letters',category='error')
        else:
            new_user=User(email=email,firstName=firstName,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User Added to database',category='success')
            return redirect(url_for('views.home'))
    return render_template('sign_up.html',user=None)