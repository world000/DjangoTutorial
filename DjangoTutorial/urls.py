from django.conf.urls import patterns, include, url
import view
from contact.views import contact, contact_thanks
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from books.models import Publisher
from feeds import LatestEntries, LatestEntriesByCategory

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feeds = {
    'latest': LatestEntries,
    'categories': LatestEntriesByCategory,
}

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
    (r'^unruly_passengers/$', 'DjangoTutorial.view.unruly_passengers_csv'),
    (r'^hello_pdf/$', 'DjangoTutorial.view.hello_pdf'),
    (r'^hello_video/$', 'DjangoTutorial.view.hello_video'),

    (r'^book/', include('books.urls')),
    (r'^publishers/$', list_detail.object_list, {'queryset':Publisher.objects.all(), 
                                                 'template_name': 'publisher_list_page.html', 
                                                 'template_object_name': 'publisher'}),
    
    (r'^contact/$', contact),
    (r'^contact/thanks/$', contact_thanks),
    
    (r'^articles/(\d{4})/(\d{2})/$', view.year_archive),
    (r'^articles_group/(?P<year>\d{4})/(?P<month>\d{2})/$', view.month_archive, {'year' : 2014}),
    
    (r'^about/$', direct_to_template, {'template' : 'about.html'}),
    (r'^about/(\w+)/$', 'books.views.about_pages'),
    
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)
