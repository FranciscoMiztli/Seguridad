from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='cesar'),
    path('cesarEncrypted/', views.cesarEncrypted, name='cesarEncrypted'),
    path('cesarDecrypted/', views.cesarDecrypted, name='cesarDecrypted'),
]
