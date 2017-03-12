from django.conf.urls import url
from django.contrib import admin
from .views import path_redirect
urlpatterns = [
    url(r'^(?P<path>.*)', path_redirect),
]
