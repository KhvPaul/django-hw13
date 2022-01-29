import re
from datetime import datetime

from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail
from django.core.management import BaseCommand

from hw13.models import Author, Quote

import requests


def send_message():
    send_mail(
        subject='Parsing Warning',
        message=f'{datetime.now()}: Nothing more to parse',
        from_email="noreply@mysite.com",
        recipient_list=['mytestmailbox@mail.com'],
    )


# @worker_ready.connect
@shared_task
def parse_new_quotes():
    loop, page = 0, 1
    while loop != 5:
        r = requests.get(
            f'https://quotes.toscrape.com/page/{page}/')
        if r:
            soup = BeautifulSoup(r.text, features="html.parser").find_all('div', {'class': 'quote'})
            if soup:
                for quote in soup:
                    text = quote.find('span', {'class': 'text'}).text
                    if not Quote.objects.filter(text=text):
                        author_request = requests.get(f"https://quotes.toscrape.com{quote.find_all('a')[0]['href']}")
                        author_soup = BeautifulSoup(author_request.text, features="html.parser")
                        author = Author.objects.filter(name=quote.find('small', {'class': 'author'}).text)
                        if not author:
                            Author.objects.create(name=quote.find('small', {'class': 'author'}).text,
                                                  date_of_birth=datetime.strptime(author_soup.find(
                                                      'span', {'class': 'author-born-date'}).text, '%B %d, %Y').date(),
                                                  bio=re.sub(r'\s+', ' ',
                                                             author_soup.find('div',
                                                                              {'class': 'author-description'}
                                                                              ).text.replace('\n', '')))
                            Quote.objects.create(text=quote.find('span', {'class': 'text'}).text,
                                                 author=Author.objects.last())
                        else:
                            Quote.objects.create(text=quote.find('span', {'class': 'text'}).text, author=author[0])
                        loop += 1
                        # print(f'Added new quote: {Quote.objects.last().text} - {Quote.objects.last().author}')
                        if loop == 5:
                            break
                        page += 1 if quote == soup[-1] else 0
                    else:
                        page += 1 if quote == soup[-1] else 0
                        continue
            else:
                loop = 5
                # BaseCommand().stdout.write(BaseCommand().style.ERROR(f'No quotes on page'))
                send_message()
        else:
            loop = 5
            BaseCommand().stdout.write(BaseCommand().style.ERROR(f'Request status: [{r.status_code}]'))
            send_message()