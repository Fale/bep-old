from django.conf.urls import patterns, url
from wheel.views import pages

urlpatterns = patterns('',
    url(r'^$', pages.list, name='list'),
)
