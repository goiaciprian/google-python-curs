from django.contrib import admin
from .models import Employee, Employer

# Register your models here.


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_employees_number')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if(user.is_superuser):
            return queryset

        return queryset.filter(user=user)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employer_name')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if(user.is_superuser):
            return queryset

        return queryset.filter(user=user)
