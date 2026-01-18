from data import init_subjects, init_teachers
from scheduler import create_schedule
from printer import print_schedule


def main():
    subjects = init_subjects()
    teachers = init_teachers()

    schedule = create_schedule(subjects, teachers)
    print_schedule(schedule)


if __name__ == "__main__":
    main()
