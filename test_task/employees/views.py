
from django.shortcuts import render
from django.http import JsonResponse
from employees.utils.requst_hendlers import get_employees_by_position, get_subordinates, get_employee_info


def base_page(request):
    employees_data = get_employees_by_position()
    return render(request, 'base.html', context={'employees_data': employees_data})


def employee_list(request, position: str = '', page: int = 0, sort: str = '', increase: int = 1):
    increase = bool(increase)
    employees_data = get_employees_by_position(position, page, sort, increase)
    return JsonResponse({'employees_data': employees_data}, safe=False)


def subordinates_list(request, uuid):
    subordinates_data = get_subordinates(uuid)
    return JsonResponse({'subordinates_data': subordinates_data}, safe=False)


def employee_info(request, uuid, head_name: int = 1):
    head_name = bool(head_name)
    employee_info_ = get_employee_info(uuid, head_name)
    return JsonResponse({'employee_info': employee_info_}, safe=False)

