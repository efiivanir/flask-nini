from flask import render_template, flash, redirect, url_for, request
from app import app,db,admin_required
from app.forms import LoginForm,AddTherapistForm
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from app.models import Therapist



@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Therapist.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/view_therapists', methods=['GET'])
@login_required
@admin_required
def view_therapists():
    therapists = Therapist.query.all()
    return render_template('view_therapists.html',
                           title='View Therapists', therapists=therapists)


@app.route('/add_therapist', methods=['GET', 'POST'])
@login_required
@admin_required
def add_therapist():
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    form = AddTherapistForm()
    if form.validate_on_submit():
        user = Therapist(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('add_therapist.html', title='Add Therapist', form=form)

@app.route('/yad_davids')
@login_required
@admin_required
def yad_davids():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts)
