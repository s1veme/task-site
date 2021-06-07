import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'necicada.settings')

app = Celery('necicada')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.beat_schedule = {
#    'check-basedata-leader': {
#        'task': 'leaderboard.tasks.check_table_leader',
#        'schedule': 60.0,
#    }
# }
