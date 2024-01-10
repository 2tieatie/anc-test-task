import os
import django
from faker import Faker
from django.utils import timezone
import uuid

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_task.settings")
django.setup()

from employees.models import Employee

fake = Faker()
positions = {
    "CEO": 1,
    "Vice President": 7,
    "Director": 49,
    "Manager": 343,
    "Team Lead": 2401,
    "Specialist": 16801,
    "Worker": 117649
}


def generate_employee(position: str, head: uuid.UUID):
    return Employee(
        full_name=fake.name(),
        position=position,
        hire_date=fake.date_between(start_date='-5y', end_date='today'),
        email=fake.email(),
        head=head
    )


def generate_employees(num_employees: int = 100):
    Employee.objects.all().delete()
    ceo = generate_employee("CEO", uuid.uuid4())
    ceo.head = ceo.uuid
    ceo.save()
    for index, i in enumerate(positions.keys()):
        head_pos = i
        try:
            pos = list(positions.keys())[index + 1]
        except IndexError:
            break
        employees = []
        for empl in Employee.objects.filter(position=head_pos):
            head = empl.uuid
            for _ in range(7):
                employee = generate_employee(pos, head)
                employees.append(employee)
        Employee.objects.bulk_create(employees)


if __name__ == "__main__":
    generate_employees()
    print("Data seeded successfully.")
