from typing import List, Set
from models import Teacher


def create_schedule(subjects: Set[str], teachers: List[Teacher]):
    uncovered_subjects = set(subjects)
    remaining_teachers = teachers[:]
    schedule: List[Teacher] = []

    while uncovered_subjects:
        best_teacher = None
        best_covered_subjects = set()

        for teacher in remaining_teachers:
            covered = teacher.can_teach_subjects & uncovered_subjects

            if not covered:
                continue

            if (
                best_teacher is None
                or len(covered) > len(best_covered_subjects)
                or (
                    len(covered) == len(best_covered_subjects)
                    and teacher.age < best_teacher.age
                )
            ):
                best_teacher = teacher
                best_covered_subjects = covered

        if best_teacher is None:
            return None

        best_teacher.assigned_subjects = best_covered_subjects
        schedule.append(best_teacher)

        uncovered_subjects -= best_covered_subjects
        remaining_teachers.remove(best_teacher)

    return schedule
