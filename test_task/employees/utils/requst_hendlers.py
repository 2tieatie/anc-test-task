from django.db import connection
from django.db.models import Q
from employees.models import Employee

N_PER_PAGE = 25


def search_employees(query):
    employees = Employee.objects.filter(
        Q(full_name__icontains=query) |
        Q(position__icontains=query) |
        Q(email__icontains=query)
    )

    return employees


def get_employees_by_position(position='all', page: int = 0, sort_by: str = '', increase: bool = True):
    if position == "all":
        sql_filter = "WHERE e.position IN ('CEO', 'Vice President')"
    else:
        employees = search_employees(position)
        uuid_list = [str(employee.uuid).replace('-', '') for employee in employees]
        if not uuid_list:
            return []
        uuid_list_str = "', '".join(uuid_list)
        sql_filter = f"WHERE e.uuid IN ('{uuid_list_str}')"

    if sort_by:
        order_direction = "ASC" if increase else "DESC"
        sql_sort = f"ORDER BY e.{sort_by} {order_direction}"
    else:
        sql_sort = ""

    limit = N_PER_PAGE
    offset = page * N_PER_PAGE

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
                {sql_sort}
                LIMIT {limit} OFFSET {offset};
            """
        cursor.execute(sql_query)

        result = cursor.fetchall()

    columns = [col[0] for col in cursor.description]
    employees_data = [dict(zip(columns, row)) for row in result]

    return employees_data


def get_subordinates(head_uuid):
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
            WHERE e.head = '{head_uuid}'
        """
        cursor.execute(sql_query)
        result = cursor.fetchall()

    columns = [col[0] for col in cursor.description]
    employees_data = [dict(zip(columns, row)) for row in result]
    return employees_data


def get_employee_info(uuid, head_name: bool):
    if head_name:
        head = 'h.full_name AS head_name,'
        join = ' LEFT JOIN employees_employee h ON e.head = h.uuid '
    else:
        head = 'e.head,'
        join = ''
    with connection.cursor() as cursor:
        sql_query = f""" 
            SELECT
                e.id,
                e.full_name,
                e.position,
                e.hire_date,
                e.email,
                {head}
                e.uuid
            FROM
                employees_employee e
            {join}
            WHERE e.uuid = '{uuid}'
        """
        cursor.execute(sql_query)
        result = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    employees_data = [dict(zip(columns, row)) for row in result]
    return employees_data