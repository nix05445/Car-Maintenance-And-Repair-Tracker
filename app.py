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

@app.route("/edit/<int:id>", methods=["GET", "POST"]) 
def edit(id):  
    entry = ServiceEntry.query.get_or_404(id) 

    if request.method == "POST": 
        entry.date = request.form["date"] 
        entry.mileage = request.form["mileage"] 
        entry.category = request.form["category"] 
        entry.work_done = request.form["work_done"] 
        entry.cost = request.form["cost"] or 0 

        db.session.commit() 
        return redirect("/") 

    entries = ServiceEntry.query.order_by(ServiceEntry.mileage.desc()).all() 

    return render_template("index.html", 
        entries=entries, 
        editing_entry=entry
    ) 

@app.route("/delete/<int:id>")
def delete(id):
    entry = ServiceEntry.query.get_or_404(id)
    
    db.session.delete(entry)
    db.session.commit()
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)    