from flask import Flask, redirect, url_for, render_template, request, session, flash, Blueprint
from .models import users, db

login_bp = Blueprint('login', __name__)

@login_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash(f"Logged in as {user}", "info")
        return redirect(url_for('user.user'))
    else:
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user.user"))
        return render_template("login.html")
    
    