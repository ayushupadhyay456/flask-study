from flask import Flask,render_template,request,flash
from flask import Blueprint


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
            flash('User Added to datab base',category='success')
    return render_template('sign_up.html',user=None)