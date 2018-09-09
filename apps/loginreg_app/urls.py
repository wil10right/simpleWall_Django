from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^sendit$', views.sendit),
    url(r'^comment$', views.comment),
    url(r'^welcome$', views.welcome),
    url(r'^reset$', views.reset),
]