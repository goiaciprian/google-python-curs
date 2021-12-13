from django.db import models
from hr_manager.settings import AUTH_USER_MODEL
from django.core.validators import MinValueValidator
# Create your models here.


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(MyModel):
    class Meta:
        db_table = 'employers'

    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, default=1)
    employees = models.ManyToManyField(
        AUTH_USER_MODEL, through='Employee', related_name='employees')

    def get_employees_number(self):
        return self.employees.count()
    get_employees_number.short_description = 'Employees No.'

    def __str__(self):
        return f'{self.name}'


class Employee(MyModel):
    class Meta:
        db_table = 'employees'

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    wage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100.00,
        null=False,
        validators=[MinValueValidator(0.00)]
    )

    def first_name(self):
        return self.user.first_name
    first_name.short_description = 'First Name'
    first_name.admin_order_field = 'user__first_name'

    def last_name(self):
        return self.user.last_name
    last_name.short_description = 'Last Name'
    last_name.admin_order_field = 'user__last_name'   

    def employer_name(self):
        return self.employer.name
    employer_name.short_description = 'Employer'
    employer_name.admin_order_field = 'employer__name'
