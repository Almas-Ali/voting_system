from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('vote', views.vote, name='vote'),
    path('result', views.result, name='result'),
]
