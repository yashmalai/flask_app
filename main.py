from flask import Flask, redirect, url_for, render_template, request, session, flash, Blueprint
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from admin.logout import logout_bp
from admin.GetUserInfo import user_bp
from admin.login import login_bp
from admin.models import users, db

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=7)

db.init_app(app)

app.register_blueprint(user_bp, url_prefix="/admin")
app.register_blueprint(login_bp, url_prefix="/admin")
app.register_blueprint(logout_bp, url_prefix="/admin")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)