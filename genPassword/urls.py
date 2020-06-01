from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='genPassword'),
    path('password/', views.password, name='password'),
]
