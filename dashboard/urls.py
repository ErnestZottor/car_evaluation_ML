from django import urls
from django.urls import path
from .import views

urlpatterns = [
    path('', views.site, name='home'),
    path('predictions/', views.predictions, name='predictions')
]