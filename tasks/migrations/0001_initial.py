# Generated by Django 3.2.4 on 2021-06-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_task', models.CharField(max_length=150)),
                ('task_text', models.TextField()),
                ('decision', models.CharField(max_length=100)),
                ('number_of_points', models.PositiveIntegerField()),
            ],
        ),
    ]
