from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ServiceEntry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    work_done = db.Column(db.String(200), nullable=False)
    cost = db.Column(db.Float, default=0)

    def __repr__(self):
        return f"<ServiceEntry {self.work_done}>"