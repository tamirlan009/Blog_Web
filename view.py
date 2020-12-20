from app import app
from flask import render_template,request,url_for
from models import Post
from flask_security import login_required

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/articles')
#@login_required
def articles():
    p = Post.query.all()
    return render_template('blog.html', articles = p)

@app.route('/articles/<slug>')
def detile(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    return render_template('post_detile.html', post = post)


@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404 
