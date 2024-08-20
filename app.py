from flask import Flask, redirect, url_for, render_template, request, session, flash, Blueprint
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from auth.logout import logout_bp
from auth.GetUserInfo import user_bp
from auth.login import login_bp
from auth.models import users
import os
import dotenv
from config import migrate, db

app = Flask(__name__)
app.secret_key = "secret"
dotenv.load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#время жизни сессии(убрать в теории)
app.permanent_session_lifetime = timedelta(minutes=7)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(user_bp, url_prefix="/auth")
app.register_blueprint(login_bp, url_prefix="/auth")
app.register_blueprint(logout_bp, url_prefix="/auth")

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