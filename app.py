from flask import Flask, render_template, request, redirect
from models import db, ServiceEntry

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    entries = ServiceEntry.query.order_by(ServiceEntry.mileage.desc()).all()

    return render_template(
        "index.html",
        entries=entries,
)

@app.route("/add", methods=["POST"])
def add():

    entry = ServiceEntry(
        date=request.form["date"],
        mileage=request.form["mileage"],
        category=request.form["category"],
        work_done=request.form["work_done"],
        cost=request.form["cost"] or 0
    )

    db.session.add(entry)
    db.session.commit()

    return redirect("/")