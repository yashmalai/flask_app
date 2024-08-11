from flask import Flask, redirect, url_for, render_template, request, session, flash, Blueprint
from .models import users, db
user_bp = Blueprint('user', __name__)

@user_bp.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved/")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email, user=user)
    else:
        flash("Please login first", "info")
        return redirect(url_for("login.login"))