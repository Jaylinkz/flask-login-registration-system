from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
#user login
@login_manager.user_loader
def load_user(user_id):
     return User.query.get(int(user_id))
#the below comment isn't for this project
#  write a function that takes an array and an integer as input, return any two numbers in the array that when sum up will be equal to the value of the integer


class User(db.Model,UserMixin):
     id = db.Column(db.Integer,primary_key = True)
     username = db.Column(db.String(20),unique = True,nullable=False)
     email = db.Column(db.String(120),unique = True,nullable=False)
     password = db.Column(db.String(60),nullable=False)
     image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
     posts = db.relationship('Post',backref='author', lazy=True)

     def __repr__(self):
          return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):

     id = db.Column(db.Integer,primary_key = True)
     title = db.Column(db.String(100),unique = True,nullable=False)
     date_posted = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
     content = db.Column(db.Text, nullable = False)
     User_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     def __repr__(self):
          return f"User('{self.title}','{self.date_posted}')"
