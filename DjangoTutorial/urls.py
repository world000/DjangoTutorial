from django.conf.urls import patterns, include, url
import books
import view
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

    ('^$', view.my_homepage_view),
    ('^hello/$', view.hello),
    ('^time/$', view.current_datetime),
    (r'^time/plus/(\d{1,2})/$', view.hours_ahead),
    (r'^meta/$', view.display_meta),
    (r'^mobile/$', 'DjangoTutorial.view.mobile'),
    
    (r'^book/', include('books.urls')),
    
    (r'^contact/$', contact),
    (r'^contact/thanks/$', contact_thanks),
    
    (r'^articles/(\d{4})/(\d{2})/$', view.year_archive),
    (r'^articles_group/(?P<year>\d{4})/(?P<month>\d{2})/$', view.month_archive, {'year' : 2014}),
)
