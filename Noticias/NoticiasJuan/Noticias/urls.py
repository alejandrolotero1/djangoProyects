from django.urls import path
from . import views

urlpatterns = [
    path('', views.Noticias, name='Noticias'),
    path('',views.Index, name='Index' )
    
]