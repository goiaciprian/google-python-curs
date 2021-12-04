# Generated by Django 3.2.9 on 2021-12-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_employer_wage'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, unique=True)),
                ('last_name', models.EmailField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
