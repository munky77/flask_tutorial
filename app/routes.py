from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Paul'}
    posts = [{'author': {'username': 'Paul'},
              'body': 'post numer 1!'},
             {'author': {'username': 'Paul'},
              'body': 'post numer 2!'}]
    return render_template('index.html', title='Home', user=user, posts=posts)