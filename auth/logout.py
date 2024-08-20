from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session

logout_bp = Blueprint("logout", __name__)

@logout_bp.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Logged out, {user}", "info")

    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login.login"))