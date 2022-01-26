from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=1000, help_text='Author biography', blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Quote(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'
