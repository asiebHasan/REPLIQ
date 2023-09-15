# Generated by Django 4.2.5 on 2023-09-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.AlterModelManagers(
            name='company',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='company',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='username',
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]