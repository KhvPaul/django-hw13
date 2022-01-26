from django.urls import path

from . import views

urlpatterns = [
    path('', views.QuoteListView.as_view(), name='quotes'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]