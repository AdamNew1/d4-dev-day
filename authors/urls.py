from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
app_name = 'study'
urlpatterns = [
    url(r'^authors', views.view_authors, name='authorindex'),
    url(r'^books$', views.view_ind_author, name='bookindex'),
    url(r'^add_author', views.add_author, name='add_author'),
    url(r'^add_book', views.add_book, name='add_book')
]
