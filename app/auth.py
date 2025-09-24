from flask import Blueprint, render_template as render, redirect, url_for, flash, request
from .forms import LoginForm, RegisterForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from . import db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi!', 'success')
        return redirect(url_for('main.index'))
    return render('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Muvaffaqiyatli kirdingiz!', 'success')
            return redirect(next_page or url_for('main.index'))
        else:
            flash('Yaroqsiz elektron pochta yoki parol.', 'warning')
    return render('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Siz tizimdan chiqdingiz.', 'info')
    return redirect(url_for('auth.login'))
