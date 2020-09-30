from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Kate'}
    posts = [
        {
            'author': {'username':'Lana'},
            'body': 'The park is awesome'
        },
        {
            'author': {'username':'Kate'},
            'body': 'I need to concentrate on this more'
        }
    ]
    return render_template('index.html',title="Home",user=user,posts=posts)