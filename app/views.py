"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
from flask import Flask
import os
import time
import datetime
from flask import render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Required

from app import db
from app.models import Profile

class ProfileForm(Form):
  
  first_name = TextField('First Name', validatrs=[Required()])
  last_name = TextField('Last Name', validatrs=[Required()])
  image = FileField('image', validatrs=[Required()])
  age = BooleanField('age', validatrs=[Required()])
  sex = TextField('sex', validatrs=[Required()])

###
# Routing for your application.
###
image = UploadSet('image', IMAGES)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile/')
def profile_add():
  form = ProfileForm()
  if request.method == "POST" and 'image' in request.files:
    time = request.form['time']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    sex = request.form['sex']
    age = request.form['age']
    filename = photos.save(request.files['image'])
    rec = Photo(filename=filename, user=g.user.id)
    rec.store()
    flash("Photo saved.")
    newprofile = Profile(first_name,last_name,sex,age,image,time)
    db.session.add(newprofile)
    db.session.commit()
    return redirect(url_for('show', id=rec.id))
    return "{} {} this was sucessfully added to the database".format(first_name,last_name)
  return render_template('add_profile.html', form=form, time=time_info())

def time_info():
  now = time.strftime("%a %d %b %Y")
  return now

@app.route('/profiles/')
def profile_list():
    profile = Profile.query.all()  
    url = photos.url(image.filename)
    return "list of profiles"
  return render_template('list_profile.html', profiles=profiles, url=url, image=image)

@app.route('/profile/<int:id>/')
def profile_view(id):  
    profile = Profile.query.get(id)
  return render_template('view_profile.html', profile=profile)
  return "profile {}".format(id)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
