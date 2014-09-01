from django.conf.urls import patterns, url
from canvas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<canvas_id>\d+)/$', views.canvas, name='canvas'),
    url(r'^(?P<canvas_id>\d+)/add/(?P<box>\w+)/$', views.addItem, name='addItem'),
    url(r'^(?P<canvas_id>\d+)/(?P<item_id>\d+)/delete/$', views.deleteItem, name='deleteItem'),
)
