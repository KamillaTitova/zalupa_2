from datetime import datetime

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user

from src import db, bcrypt
from src.users.models import User

from .forms import LoginForm, RegisterForm

users_bp = Blueprint('users', __name__,
                     template_folder='templates',
                     static_folder='static',
                     url_prefix='/users')


@users_bp.route('/', methods=["GET"])
def users_list():
    title = 'Список пользователей - МВ проект \'Scripts DataBase\' - Камила Титова'
    if current_user.is_authenticated:
        if current_user.is_admin:
            users = User.query.all()
            return render_template('users/users_list.html', title=title, users=users)
        else:
            flash("You do not have permission to view this page.", "danger")
    return render_template('core/index.html', title=title)


@users_bp.route("/current_user", methods=["GET"])
@login_required
def get_user():
    title = 'Профиль пользователя - МВ проект \'Scripts DataBase\' - Камила Титова'
    return render_template('users/profile.html', user=current_user, title=title)


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        if not current_user.is_admin:
            flash("You are already registered.", "info")
            return redirect(url_for("core.home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=form.password.data,
                    mv_user_id=form.mv_user_id.data)
        db.session.add(user)
        db.session.commit()
        if not user.is_admin:
            login_user(user)
            flash("You registered and are now logged in. Welcome!", "success")
            return redirect(url_for("core.home"))
        else:
            flash(f"User {user.email} successfully registered!", "success")
    return render_template("users/register.html", form=form)


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("core.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form["password"]):
            login_user(user)
            current_user.last_login_on = datetime.now()
            db.session.commit()
            return redirect(url_for("core.home"))
        else:
            flash("Invalid email and/or password.", "danger")
            return render_template("users/login.html", form=form)
    return render_template("users/login.html", form=form)


@users_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("users.login"))
