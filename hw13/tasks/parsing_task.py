# import re
# import requests
#
# from datetime import datetime
#
# from celery import shared_task
#
# from bs4 import BeautifulSoup
#
# from django.core.mail import send_mail
#
# from hw13.models import Author, Quote
#
#
# def send_message():
#     send_mail(
#         subject='Parsing Warning',
#         message=f'{datetime.now()}: Nothing more to parse',
#         from_email="noreply@mysite.com",
#         recipient_list=['mytestmailbox@mail.com'],
#     )
#
#
# # @worker_ready.connect
# @shared_task
# def parse_new_quotes():
#     quotes_on_page_count = len(BeautifulSoup(
#         requests.get(
#             'https://quotes.toscrape.com/page/1/').text, features="html.parser").find_all('div', {'class': 'quote'}))
#
#     r = requests.get(
#         f'https://quotes.toscrape.com/page/{(Quote.objects.all().count() // quotes_on_page_count) + 1}/')
#     if BeautifulSoup(r.text, features="html.parser").find_all('div', {'class': 'quote'}):
#         soup = BeautifulSoup(r.text, features="html.parser").find_all('div', {'class': 'quote'})
#         for i in range(5):
#             try:
#                 quote = soup[Quote.objects.count() % 10]
#                 author_request = requests.get(f"https://quotes.toscrape.com{quote.find_all('a')[0]['href']}")
#                 author_soup = BeautifulSoup(author_request.text, features="html.parser")
#                 author = Author.objects.filter(name=quote.find('small', {'class': 'author'}).text)
#                 if not author:
#                     Author.objects.create(name=quote.find('small', {'class': 'author'}).text,
#                                           date_of_birth=datetime.strptime(author_soup.find(
#                                               'span', {'class': 'author-born-date'}).text, '%B %d, %Y').date(),
#                                           bio=re.sub(r'\s+', ' ',
#                                                      author_soup.find('div',
#                                                                       {'class': 'author-description'}).text.replace(
#                                                          '\n', ''))
#                                           )
#
#                     Quote.objects.create(
#                                         text=quote.find('span', {'class': 'text'}).text, author=Author.objects.last())
#                 else:
#                     Quote.objects.create(text=quote.find('span', {'class': 'text'}).text, author=author[0])
#             except IndexError:
#                 send_message()
#                 # os.system('celery -A hw13_core purge')
#                 # os.system('y')
#     else:
#         send_message()
#         # os.system('celery -A hw13_core purge')
#         # os.system('y')
