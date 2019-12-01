"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from FlaskWebProjectAssignment import app, db
from FlaskWebProjectAssignment.forms import LoginForm, RegistrationForm, FlightForm, HotelForm
from FlaskWebProjectAssignment.models import User,Order



@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    """Renders the home page."""
    
    return render_template(
        'index.html',
        title='Index Page',
        year=datetime.now().year,
    )




@app.route('/order')
def order():
    
    if current_user.is_authenticated:
        flash('Happy Travelling!')
    else:
        flash ('Login To Begin Your Travel Planning')
        return redirect(url_for('home'))
    
    form= FlightForm()
    if form.validate_on_submit():
        flight= Flight (start_location=form.start_location.data, end_location=form.end_location.data, passenger=form.passenger.data, Class=form.Class.data, Trip= form.Trip.data, start_date= form.start_date.data, end_date= form.end_date.data )
        db.session.add(flight)
        db.session.commit()
    return render_template(
        'order.html',
        title= "Order Page",
        form = form,
        year=datetime.now().year
        )

    return render_template(
        'order.html',
        title= "Order Page",
        form = form,
        year=datetime.now().year
        )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':   #"next"  and security check miguel's part V
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        flash('Congratulations, you are now a registered user!')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username = username).first_or_404()

    form = EditAddress()
    if form.validate_on_submit():        
        current_user.address = form.address.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        
        form.address.data = current_user.address 
    
    return render_template('user.html', title = 'Profile' , form = form, user=user)

@app.route('/test')
def test():    
    u = User(id= '1',username="Coroline", email="fuckboi@gmail.com")
    o = Order(customer = u)
    orders = Order.query.all()
    
    db.session.add(u)
    db.session.add(o)
    db.session.commit()
    for ord in orders:
        print(orders.id,orders.customer.id)


    return render_template(
    'layout.html',
    title = 'test',
    year = datetime.now().year,
    message='TestPage'           
           )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
