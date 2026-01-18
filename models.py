from typing import Set


class Teacher:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        email: str,
        can_teach_subjects: Set[str],
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects: Set[str] = set()

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"
