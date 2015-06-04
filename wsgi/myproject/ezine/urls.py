from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.ezine_list),
    url(r'^ezine/(?P<pk>[0-9]+)/$', views.ezine_detail),
]
