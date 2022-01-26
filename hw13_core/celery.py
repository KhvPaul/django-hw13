import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw13_core.settings')

app = Celery('hw13_core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
