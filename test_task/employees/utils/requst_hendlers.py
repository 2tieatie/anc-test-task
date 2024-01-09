from django.db import connection
from django.db.models import Q
from employees.models import Employee


def search_employees(query):
    employees = Employee.objects.filter(
        Q(full_name__icontains=query) |
        Q(position__icontains=query) |
        Q(email__icontains=query)
    )

    return employees


def get_employees_by_position(position='all'):
    if position == "all":
        sql_filter = "WHERE e.position IN ('CEO', 'Vice President');"
    else:
        employees = search_employees(position)
        uuid_list = [str(employee.uuid) for employee in employees]
        if not uuid_list:
            return []
        uuid_list_str = "', '".join(uuid_list)
        sql_filter = f"WHERE e.uuid IN ('{uuid_list_str}');"
        print(sql_filter)
    with connection.cursor() as cursor:
        sql_query = f""" 
            SELECT
              e.id,
              e.full_name,
              e.position,
              e.hire_date,
              e.email,
              h.full_name AS head_name,
              e.uuid
            FROM
              employees_employee e
            LEFT JOIN
              employees_employee h ON e.head = h.uuid
            {sql_filter}
        """
        cursor.execute(sql_query)
        columns = [col[0] for col in cursor.description]
        employees_data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return employees_data
