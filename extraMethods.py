from random import shuffle


def random_teachers(teachers):
    lst = list(range(1, teachers.count()))
    shuffle(lst)
    return lst


def free_time(teachers, id_t):
    result = {
        "Понедельник": [],
        "Вторник": [],
        "Среда": [],
        "Четверг": [],
        "Пятница": [],
        "Суббота": [],
        "Воскресенье": [],
    }
    english_russian_days = {
        "mon": "Понедельник",
        "tue": "Вторник",
        "wed": "Среда",
        "thu": "Четверг",
        "fri": "Пятница",
        "sat": "Суббота",
        "sun": "Воскресенье",
    }
    for day, time in teachers[id_t].free.items():
        for key, value in time.items():
            if not value:
                continue
            result[english_russian_days[day]].append(key)

    return result
