from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='choise'),
    path('family/<int:id>', views.family, name="family"),
    path('anima/<int:id>', views.animals, name="anima")
    
]