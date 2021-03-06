from django.db import models


class Task(models.Model):
    name_task = models.CharField(max_length=150)
    task_text = models.TextField()
    decision = models.CharField(max_length=100)

    number_of_points = models.PositiveIntegerField()
    complexity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.task_text[:10]}...' if len(self.task_text) > 20 else self.task_text

    # TODO: complexity
