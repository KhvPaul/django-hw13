from celery import shared_task
import requests


@shared_task
def parse_new_quotes():
    r = requests.get('https://quotes.toscrape.com')
