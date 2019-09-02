from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<slug>[\w_-]+)$', views.category,  name='category'),
    url(r'^produto/(?P<slug>[\w_-]+)$', views.product,  name='product'),
]
