from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import *
urlpatterns = patterns('hungergames.views',

    url(r'^categories/$', CategoryGameTemplateView.as_view(), name='CategoryGameTemplateView'),    
    )