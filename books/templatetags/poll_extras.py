#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    "Removes all values of arg from the given string"
    return value.replace(arg, '')

@register.filter
def lower(value): # Only one argument.
    "Converts a string into all lowercase"
    return value.lower()