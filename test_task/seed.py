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
    # "Specialist": 16801,
    # "Worker": 117649
}

employees_dict = {
    "CEO": [],
    "Vice President": [],
    "Directors": [],
    "Managers": [],
    "Team Leads": [],
    "Specialist": [],
    "Associates": []
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
    head_pos = "CEO"
    pos = "Vice President"
    for i in Employee.objects.filter(position=head_pos):
        employees = []
        head = i.uuid
        for _ in range(7):
            employee = generate_employee(pos, head)
            print(employee)
            employees.append(employee)
        Employee.objects.bulk_create(employees)
    head_pos = "Vice President"
    pos = "Director"
    for i in Employee.objects.filter(position=head_pos):
        employees = []
        head = i.uuid
        for _ in range(7):
            employee = generate_employee(pos, head)
            print
            employees.append(employee)
        Employee.objects.bulk_create(employees)
    head_pos = "Director"
    pos = "Manager"
    for i in Employee.objects.filter(position=head_pos):
        employees = []
        head = i.uuid
        for _ in range(7):
            employee = generate_employee(pos, head)
            print
            employees.append(employee)
        Employee.objects.bulk_create(employees)
    head_pos = "Manager"
    pos = "Team Lead"
    employees = []
    for i in Employee.objects.filter(position=head_pos):
        head = i.uuid
        for _ in range(7):
            employee = generate_employee(pos, head)
            employees.append(employee)
    Employee.objects.bulk_create(employees)
    # head_pos = "Team Lead"
    # pos = "Specialist"
    # for i in Employee.objects.filter(position=head_pos):
    #     employees = []
    #     head = i.uuid
    #     for _ in range(positions[head_pos]):
    #         employee = generate_employee(pos, head)
    #         employees.append(employee)
    #     Employee.objects.bulk_create(employees)
    # head_pos = "Specialist"
    # pos = "Worker"
    # for i in Employee.objects.filter(position=head_pos):
    #     employees = []
    #     head = i.uuid
    #     for _ in range(positions[head_pos]):
    #         employee = generate_employee(pos, head)
    #         employees.append(employee)
    #     Employee.objects.bulk_create(employees)


if __name__ == "__main__":
    generate_employees()
    print("Data seeded successfully.")
