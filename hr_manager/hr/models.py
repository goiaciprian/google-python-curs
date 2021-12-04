from django.db import models

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
    wage = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class User(MyModel):
    class Meta:
        db_table = 'users'

    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.EmailField(max_length=255, unique=True)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Employee(MyModel):
    class Meta:
        db_table = 'employees'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
