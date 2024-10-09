# app/views.py
from flask import Blueprint, render_template, redirect, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from .models import User

main = Blueprint('main', __name__)

users = {}

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

@main.route('/challenges')
def challenges():
    return render_template('challenges.html')

@main.route('/tutorials/variables')
def variables():
    return render_template('tutorials/variables.html')

@main.route('/challenges/fizzbuzz')
def fizzbuzz():
    return render_template('challenges/fizzbuzz.html')
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users:
            flash('Username already exists.')
        else:
            user_id = str(len(users) + 1)
            users[username] = User(user_id, username, password)
            flash('Registration successful.')
            return redirect('/login')

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)

        if user and user.password == password:
            login_user(user)
            return redirect('/')
        else:
            flash('Invalid credentials.')

    return render_template('login.html')

@main.route('/profile')
@login_required
def profile():
    total_tutorials = 2  # Update as more tutorials are added
    return render_template('profile.html', total_tutorials=total_tutorials)

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        new_username = request.form.get('username')
        new_password = request.form.get('password')

        if new_username:
            current_user.username = new_username
        if new_password:
            current_user.password = generate_password_hash(new_password, method='sha256')

        flash('Profile updated successfully.')
        return redirect('/profile')

    return render_template('edit_profile.html')