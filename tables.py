from init import db

from sqlalchemy.dialects.postgresql import JSON


class Teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    about = db.Column(db.Text(), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String(), nullable=False)
    goals = db.Column(db.JSON)
    free = db.Column(db.JSON)
    bookings = db.relationship("Booking")


class Booking(db.Model):
    __tablename__ = "bookings"

    day = db.Column(db.String(), nullable=False)
    time = db.Column(db.DateTime)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False, primary_key=True)
    teachers_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    teacher = db.relationship("Teacher")


class Request(db.Model):
    __tablename__ = "requests"

    goal = db.Column(db.String(), nullable=False)
    time = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False, primary_key=True)


