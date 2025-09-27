from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, User, Trip, TripPassenger, Rating, Report
from forms import RegisterForm, LoginForm, TripForm, ReportForm, RatingForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
import os
import requests

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = "login"

# Setup Flask-Admin
admin = Admin(app, name="Admin Movilidad", template_mode="bootstrap4")
class AdminModelView(ModelView):
    def is_accessible(self):
        from flask import abort
        if not (current_user.is_authenticated and current_user.is_admin):
            abort(403)
        return True

admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Trip, db.session))
admin.add_view(AdminModelView(Report, db.session))
admin.add_view(AdminModelView(Rating, db.session))

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("Correo ya registrado", "warning")
            return redirect(url_for("register"))
        user = User(email=form.email.data, name=form.name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registro exitoso. Inicia sesión.", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Credenciales inválidas", "danger")
            return redirect(url_for("login"))
        login_user(user)
        flash("Bienvenido " + (user.name or user.email), "success")
        return redirect(url_for("index"))
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada", "info")
    return redirect(url_for("index"))

# Crear viaje
@app.route("/trips/create", methods=["GET", "POST"])
@login_required
def create_trip():
    form = TripForm()
    if form.validate_on_submit():
        trip = Trip(
            origin=form.origin.data,
            destination=form.destination.data,
            departure_time=form.departure_time.data,
            seats=form.seats.data,
            driver_id=current_user.id
        )
        db.session.add(trip)
        db.session.commit()
        flash("Viaje creado con éxito", "success")
        return redirect(url_for("list_trips"))
    return render_template("create_trip.html", form=form)

# Listar viajes
@app.route("/trips")
@login_required
def list_trips():
    trips = Trip.query.filter(Trip.departure_time >= datetime.utcnow()).all()
    return render_template("trips.html", trips=trips)

# Ver viaje y unirse
@app.route("/trips/<int:trip_id>", methods=["GET", "POST"])
@login_required
def trip_detail(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    report_form = ReportForm()
    rating_form = RatingForm()
    already_joined = TripPassenger.query.filter_by(trip_id=trip.id, user_id=current_user.id).first()
    if request.method == "POST":
        if "join" in request.form:
            # Unirse
            current_passengers = TripPassenger.query.filter_by(trip_id=trip.id).count()
            if current_passengers >= trip.seats:
                flash("No hay cupos disponibles", "warning")
            elif already_joined:
                flash("Ya estás en este viaje", "info")
            else:
                tp = TripPassenger(trip_id=trip.id, user_id=current_user.id)
                db.session.add(tp)
                db.session.commit()
                flash("Te has unido al viaje", "success")
            return redirect(url_for("trip_detail", trip_id=trip.id))

        if "report" in request.form and report_form.validate_on_submit():
            r = Report(
                trip_id=trip.id,
                reporter_id=current_user.id,
                reported_driver_id=trip.driver_id,
                reason=report_form.reason.data
            )
            db.session.add(r)
            db.session.commit()
            flash("Reporte enviado. El administrador lo revisará.", "success")
            return redirect(url_for("trip_detail", trip_id=trip.id))

        if "rate" in request.form and rating_form.validate_on_submit():
            # Verifica que el pasajero haya participado (esto es demo: comprueba TripPassenger)
            tp = TripPassenger.query.filter_by(trip_id=trip.id, user_id=current_user.id).first()
            if not tp:
                flash("Solo pasajeros que hicieron el viaje pueden calificar", "warning")
            else:
                rating = Rating(
                    trip_id=trip.id,
                    passenger_id=current_user.id,
                    driver_id=trip.driver_id,
                    stars=rating_form.stars.data,
                    comment=rating_form.comment.data
                )
                db.session.add(rating)
                db.session.commit()
                flash("Gracias por la calificación", "success")
            return redirect(url_for("trip_detail", trip_id=trip.id))

    current_passengers = TripPassenger.query.filter_by(trip_id=trip.id).count()
    seats_left = max(trip.seats - current_passengers, 0)
    driver = User.query.get(trip.driver_id)
    return render_template("trip_detail.html", trip=trip, seats_left=seats_left, driver=driver,
                           already_joined=already_joined, report_form=report_form, rating_form=rating_form)

# Ruta optimizada (stub): integra Google Maps Directions API para producción
@app.route("/trips/<int:trip_id>/route")
@login_required
def get_route(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    api_key = app.config.get("GOOGLE_MAPS_API_KEY")
    if not api_key:
        return {"error":"No API key configured. Set GOOGLE_MAPS_API_KEY in env."}, 400

    # Este es un ejemplo básico usando Directions API (requiere direcciones en formato address o lat,lng)
    params = {
        "origin": trip.origin,
        "destination": trip.destination,
        "key": api_key,
        "departure_time": "now"
    }
    r = requests.get("https://maps.googleapis.com/maps/api/directions/json", params=params)
    if r.status_code != 200:
        return {"error":"Error contacting Google Maps API"}, 500
    data = r.json()
    # Para demo devolvemos la ruta recibida
    return data

# Perfil simple
@app.route("/profile")
@login_required
def profile():
    # Mostrar viajes creados y los que se unió
    created = Trip.query.filter_by(driver_id=current_user.id).all()
    joined = TripPassenger.query.filter_by(user_id=current_user.id).all()
    return render_template("profile.html", created=created, joined=joined)

if __name__ == "__main__":
    # crear DB si no existe
    with app.app_context():
        db.create_all()
    app.run(debug=True)
