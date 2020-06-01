from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='transposicion'),
    path('transposicion/', views.transposicion, name='transposicionEncryp'),
    path('transposicionDecryp/', views.transposicionDecryp, name='transposicionDecryp'),
]
