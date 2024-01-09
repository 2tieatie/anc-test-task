import os
import django
from faker import Faker
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_task.settings")
django.setup()

from employees.models import Employee

fake = Faker()

def generate_employee():
    return Employee(
        full_name=fake.name(),
        position=fake.job(),
        hire_date=fake.date_between(start_date='-5y', end_date='today'),
        email=fake.email(),
    )

def generate_employees(num_employees=100):
    employees = [generate_employee() for _ in range(num_employees)]
    Employee.objects.bulk_create(employees)
    print(Employee.objects.f)
if __name__ == "__main__":
    generate_employees()
    print("Data seeded successfully.")
