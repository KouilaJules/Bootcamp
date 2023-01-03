from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.animals, name='animals'),
    path('', views.family, name='family')
]
