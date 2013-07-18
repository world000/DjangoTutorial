from django.conf.urls import patterns
from books.views import search

urlpatterns = patterns('',
    (r'^search/', search),         
)
