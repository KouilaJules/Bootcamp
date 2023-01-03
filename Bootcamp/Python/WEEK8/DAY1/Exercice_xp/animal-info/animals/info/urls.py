from django.urls import path
from . import views

urlpatterns = [
    path('',views.choise, name='choise'),
    
]