import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw13_core.settings')

app = Celery('hw13_core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'add-quote-every-minute': {
        'task': 'hw13.tasks.parse_new_quotes',
        'schedule': crontab(),
        # 'schedule': crontab(hour='1-23/2'),
    },
}
