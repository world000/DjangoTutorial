from django.conf.urls import patterns, include, url
from view import hello, my_homepage_view, current_datetime, hours_ahead, display_meta
from books.views import search
from contact.views import contact, contact_thanks

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#     url(r'^$', 'DjangoTutorial.views.home', name='home'),
#     url(r'^DjangoTutorial/', include('DjangoTutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

    ('^$', my_homepage_view),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^meta/$', display_meta),
    (r'^mobile/$', 'DjangoTutorial.view.mobile'),
    
    (r'^search/$', search),
    
    (r'^contact/$', contact),
    (r'^contact/thanks/$', contact_thanks),
)
