import os
from django.conf import settings
from celery import Celery
from time import sleep

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_celery_project.settings')

app = Celery('my_celery_project')

# Use the correct module path for settings
app.config_from_object('my_celery_project.settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task
def add(x, y):
    sleep(20)
    return x + y
