from django.urls import path

from django101.demo.views import home

urlpatterns = (
    path('', home),
)
