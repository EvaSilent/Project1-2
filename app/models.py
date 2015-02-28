from . import db

class Profile(db.Model):
  
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(20), unique=True)
  last_name = db.Column(db.String(20), unique=True)
  sex = db.Column(db.String(7), unique=True)
  age = db.Column(db.String(2), unique=True)
  image = db.Column(db.LargeBinary,unique=True)
  time = db.Column(db.String(10), unique=True)
  
  def __init__(self, first_name, last_name, age, sex, image, time):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.sex = sex
    self.image = image
    self.time = time
    
  def __repr__(self):
    return '<Profile %r %r>' % (self.last_name,self.first_name,self.sex,self.age,self.image,self.time)