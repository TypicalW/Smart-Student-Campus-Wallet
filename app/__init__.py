from flask import (
    Flask,
    render_template,
    request,
    redirect, 
    url_for, 
    flash,
    session)
from app.extensions import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campus_wallet.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "my-secret-key"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/register", methods=["GET","POST"])
    def register():

        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            hashed_password = generate_password_hash(password)

            existing_user = User.query.filter_by(email=email).first()

            if existing_user:
                flash("Email Already in Use.","error")
                return redirect(url_for("register"))

            user = User(
                name=name,
                email=email,
                password=hashed_password                
            )

            try:
                db.session.add(user)
                db.session.commit()

                flash("Registration successful!", "success")
                return redirect(url_for("home"))

            except Exception:
                db.session.rollback()
                flash("Something went wrong. Please try again.", "error")
                return redirect(url_for("register"))

        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            user = User.query.filter_by(email=email).first()
            if not user:
                flash("No account found with that email.", "error")
                return redirect(url_for("login"))

            if not check_password_hash(user.password, password):
                flash("Incorrect password.", "error")
                return redirect(url_for("login"))
            
            session.permanent = True
            session["user_id"] = user.id

            flash("Login successful!", "success")
            return redirect(url_for("home"))
        

        return render_template("login.html")

    return app