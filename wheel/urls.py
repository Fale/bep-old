from django.conf.urls import patterns, url
from canvas.views import canvas, item, logout

urlpatterns = patterns('',
    url(r'^$', wheel.list, name='list'),
)
