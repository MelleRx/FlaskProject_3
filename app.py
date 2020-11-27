import json

from flask import Flask, render_template, request

import data
from init import db, migrate
from tables import Teacher, Request, Booking
from forms import BookingForm, RequestForm
from extraMethods import random_teachers, free_time

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:21Dima2001@127.0.0.1:5432/Flask_Project2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "kukulidi"
db.init_app(app)
migrate.init_app(app, db)

dict_to_json = {"teachers": data.teachers, "goals": data.goals}

with open("data.json", "w") as f:
    json.dump(dict_to_json, f)

with open("data.json", "r") as f:
    data_json = json.loads(f.read())


# @app.before_first_request
# def create_tables():
#     db.create_all()
#     d_j = data_json["teachers"]
#     for t in d_j:
#         teacher = Teacher(id=t["id"], name=t["name"], about=t["about"], rating=t["rating"], price=t["price"],
#                           picture=t["picture"], goals=t["goals"], free=t["free"])
#         db.session.add(teacher)
#     db.session.commit()
#     db.session.close()


@app.route("/")
def render_main():
    teachers = db.session.query(Teacher)
    random = random_teachers(teachers)
    return render_template("index.html", teachers=teachers, goals=data_json["goals"], random=random)


@app.route("/goals/<goal>/")
def render_goals(goal):
    teachers = db.session.query(Teacher)
    return render_template("goals.html", teachers=teachers, goal=goal)


@app.route("/teachers/")
def render_teachers():
    teachers = db.session.query(Teacher).all()
    return render_template("teachers.html", teachers=teachers, goals=data_json["goals"])


@app.route("/profile/<id_teacher>/")
def render_profiles(id_teacher):
    if id_teacher.isdigit():
        teachers = db.session.query(Teacher).all()
        id_t = int(id_teacher)
        time = free_time(teachers, id_t)
        return render_template("profile.html", teachers=teachers, id=id_t, time=time)
    else:
        return render_template("error.html"), 500


@app.route("/request_done/", methods=["GET", "POST"])
def render_request_done():
    form = RequestForm()
    if request.method == "POST":
        name = form.name.data
        phone = form.phone.data
        time = form.time.data
        goal = form.goal.data
        submit = form.submit.data
        with open("request.json", "r") as r:
            requests_json = json.load(r)
        requests_json.append({"goal": goal, "time": time, "name": name, "phone": phone})
        with open("request.json", "w") as w:
            json.dump(requests_json, w)
        with open("request.json", "r") as f:
            requests_json = json.loads(f.read())
        index = 0
        requests = Request(name=requests_json[index]["name"], phone=requests_json[index]["phone"],
                           time=requests_json[index]["time"], goal=requests_json[index]["goal"])
        db.session.add(requests)
        index += 1
        db.session.commit()
        return render_template("request_done.html", name=name, phone=phone, time=time, goal=goal, submit=submit)
    else:
        return render_template("request.html", form=form)


@app.route("/booking/<id_teacher>/<day>/<time>/", methods=["GET", "POST"])
def render_booking_done(id_teacher, day, time):
    form = BookingForm()
    if request.method == "POST":
        name = form.name.data
        phone = form.phone.data
        with open("booking.json", "r") as r:
            booking = json.load(r)
        booking.append({"day": day, "time": time, "name": name, "phone": phone})
        with open("booking.json", "w") as w:
            json.dump(booking, w)
        with open("booking.json", "r") as f:
            bookings_json = json.loads(f.read())
        index = 0
        bookings = Booking(name=bookings_json[index]["name"], phone=bookings_json[index]["phone"],
                           time=bookings_json[index]["time"], day=bookings_json[index]["day"])
        db.session.add(bookings)
        index += 1
        db.session.commit()
        return render_template("booking_done.html", day=day, time=time, name=name, phone=phone)
    else:
        teachers = db.session.query(Teacher)
        id_t = int(id_teacher)
        return render_template("booking.html", teachers=teachers, id=id_t, day=day, time=time,
                               form=form)


@app.errorhandler(404)
def render_not_found(error):
    return render_template("error.html", error=error), 404


@app.errorhandler(500)
def render_server_error(error):
    return render_template("error.html", error=error), 500


if __name__ == "__main__":
    app.run()
