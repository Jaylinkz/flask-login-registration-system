from flask import Flask, render_template, url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, loginForm
app = Flask(__name__)


app.config['SECRET_KEY']= 'dd727b4ebeb50af0670003ff2399aee4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

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
     form = RegistrationForm()
     if form.validate_on_submit():
          flash(f'Account created for {form.username.data}!','success')
          return redirect(url_for('hello'))
     return render_template('register.html',title='Register' ,form=form)



@app.route("/login", methods=['GET','POST'])
def login():
     form = loginForm()
     if form.validate_on_submit():
          if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
              flash('login successful','success')
              return redirect(url_for('hello'))
          else:
               flash('login Unsuccessful. please check username and password', 'danger')
     return render_template('login.html',title= 'Login' ,form=form)



if __name__=='__main__':
    app.run(debug=True)