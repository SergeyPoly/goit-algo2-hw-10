from typing import Set, List
from models import Teacher


def init_subjects() -> Set[str]:
    return {
        "Математика",
        "Фізика",
        "Хімія",
        "Інформатика",
        "Біологія",
    }


def init_teachers() -> List[Teacher]:
    return [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher(
            "Марія",
            "Петренко",
            38,
            "m.petrenko@example.com",
            {"Хімія"},
        ),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія",
            "Шевченко",
            29,
            "n.shevchenko@example.com",
            {"Біологія", "Хімія"},
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher(
            "Олена",
            "Гриценко",
            42,
            "o.grytsenko@example.com",
            {"Біологія"},
        ),
    ]
