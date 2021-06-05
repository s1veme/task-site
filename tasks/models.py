from django.db import models


class Task(models.Model):
    task_text = models.TextField()
    decision = models.CharField(max_length=100)

    number_of_points = models.PositiveIntegerField()

    # TODO: complexity По
