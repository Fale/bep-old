from django.conf.urls import patterns, url
import wheel.views

urlpatterns = patterns('',
    url(r'^$', wheel.views.list, name='list'),
)
