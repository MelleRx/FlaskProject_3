from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import InputRequired, Length


class BookingForm(FlaskForm):
    name = StringField("Вас зовут:", [InputRequired(message="Введите имя!")])
    phone = StringField("Ваш телефон:", [Length(min=12, max=12, message="Неправильный формат телефона, убедитесь, "
                                                                        "что вы вводите +7...")])
    submit = SubmitField("Записаться на пробный урок")


class RequestForm(FlaskForm):
    name = StringField("Вас зовут:", [InputRequired(message="Введите имя!")])
    phone = StringField("Ваш телефон:", [Length(min=12, max=12, message="Неправильный формат телефона, убедитесь,"
                                                                        " что вы вводите +7...")])
    time = RadioField("Сколько времени есть?", choices=[("1:30", "1-2 часа в неделю"), ("4:00", "3-5 часов в неделю"),
                                                        ("6:00", "5-7 часов в неделю"), ("8:30", "7-10 часов в неделю")])
    goal = RadioField("Какая цель занятий?", choices=[("work", "Для работы"), ("move", "Для переезда"),
                                                      ("learn", "Для школы"), ("travel", "Для путешествий")])
    submit = SubmitField("Найдите мне преподавателя")
