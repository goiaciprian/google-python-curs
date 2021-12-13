from django.contrib import admin
from django.urls import path
# from hr.views import add_new_employee, delete_user, employees, employees_redirect, fire_employee, merge_user, users, merge_employer, delete_employer_asd, homepage, employers


"""hr_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', homepage),
    # path('employers/', employers),
    # path('users/', users),
    # path('employees/', employees_redirect),
    # path('employees/<int:id_employer>', employees),
    # path('api/employers', merge_employer),
    # path('api/employers/<int:employer_id>', delete_employer_asd),
    # path('api/users', merge_user),
    # path('api/users/<int:user_id>', delete_user),
    # path('api/fire_employee', fire_employee),
    # path('api/hire_user', add_new_employee),
]
