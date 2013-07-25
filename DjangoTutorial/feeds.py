#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from blog.models import Entry

class LatestEntries(Feed):
    title = 'My Blogs'
    link = '/archive/'
    description = 'The latest news about stuff.'
    
    def items(self):
        return Entry.objects.order_by('-pub_date')[:5]

class LatestEntriesByCategory(Feed):
    title = 'My Blogs'
    link = '/archive/'
    description = 'The latest news about stuff.'
    
    def items(self):
        return Entry.objects.order_by('-pub_date')[:5]
