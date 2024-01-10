"""
URL configuration for test_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from employees.views import employee_list, base_page, subordinates_list, employee_info

urlpatterns = [
    path('', base_page, name='base_page'),
    path('api/employees_by_pos/<str:position>/<int:page>/<str:sort>/<int:increase>/', employee_list, name='get_employees_by_position'),
    path('api/subordinates/<str:uuid>/', subordinates_list, name='get_subordinates'),
    path('api/employee_info/<str:uuid>/<int:head_name>/', employee_info, name='get_employee_info'),
]
