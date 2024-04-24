from flask import render_template, url_for, redirect, flash
from flask_blog import app
from flask_blog.forms import registration_form, login_form
from flask_blog.models import User, Post
posts = [
    {
        'author': 'Isaac reyes',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Joe Potato',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registration_form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'pass':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
