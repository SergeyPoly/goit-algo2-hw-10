from typing import List
from models import Teacher


def print_schedule(schedule: List[Teacher] | None) -> None:
    if not schedule:
        print("Неможливо покрити всі предмети наявними викладачами.")
        return

    print("Розклад занять:\n")
    for teacher in schedule:
        print(
            f"{teacher.first_name} {teacher.last_name}, "
            f"{teacher.age} років, email: {teacher.email}"
        )
        print(f"   Викладає предмети: " f"{', '.join(teacher.assigned_subjects)}\n")
