from flask import  render_template, url_for,flash, redirect, request
from flaskblog import app, db,bcrypt
from flaskblog.forms import RegistrationForm, loginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user,login_required





posts = [
    {'author':'musa',
    'title':'a boy',
    'content':'boyyyyyyyyyyyyyyyyy',
    'date_posted':'13/12//22'},
     {'author':'abdullllll',
    'title':'a feminist',
    'content':'feministttttt',
    'date_posted':'13/12//22'},
     {'author':'hadiza',
    'title':'a girl',
    'content':'girllllllllll',
    'date_posted':'13/12//22'} ]
   

@app.route('/')
def hello():
     return render_template('home.html',posts=posts)

@app.route('/about')
def about():
     return render_template('about.html',title='about')


@app.route("/register", methods=['GET','POST'])
def register():
     if current_user.is_authenticated:
          return redirect(url_for('hello'))
     form = RegistrationForm()
     if form.validate_on_submit():
          pass_entry = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
          new = User(username =form.username.data, email=form.email.data, password = pass_entry)
          db.session.add(new)
          db.session.commit()
          flash('Your account has been created, you can now login!','success')
          return redirect(url_for('login'))
     return render_template('register.html',title='Register' ,form=form)



@app.route("/login", methods=['GET','POST'])
def login():
     if current_user.is_authenticated:
          return redirect(url_for('hello'))
     form = loginForm()
     if form.validate_on_submit():
         user = User.query.filter_by(email=form.email.data).first()
         if user and bcrypt.check_password_hash(user.password,form.password.data):
              login_user(user, remember = form.remember.data)
              next_page = request.args.get('next')
              return redirect(next_page) if next_page else  redirect(url_for('hello'))
             # return redirect(url_for('hello'))

         else:
             flash('login Unsuccessful. please check email and password', 'danger')
     return render_template('login.html',title= 'Login' ,form=form)


@app.route("/logout")
def logout():
     logout_user()
     return redirect(url_for('hello'))


@app.route("/account")
@login_required
def account():
     image_file = url_for('static',filename='profile_images/' + current_user.image_file )
     return render_template('account.html',title= 'Account', image_file=image_file)



