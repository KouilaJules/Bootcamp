from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def choise(request):
  animals = [
    {
      "id" :1,
      "name": "Dog",
      "legs": 4,
      "weight": 5.67,
      "height":4.2,
      "speed": 34,
      "family": 2
    },
    {
      "id": 2,
      "name": "Domestic Cat",
      "legs": 2,
      "weight": 5.67,
      "height":4.2,
      "speed": 34,
      "family": 1
    },
    {
      "id": 3,
      "name": "Panther",
      "legs": 2,
      "weight": 5.67,
      "height":4.2,
      "speed": 34,
      "family": 1 
    }
  ],
  families = [
    {
      "id": 1,
      "name": "Felidae"
    },
    {
      "id": 2,
      "name": "Caninae"
    }
  ]
  people = [
        {
            'id': 1,
            'name': 'Bob Smith',
            'age': 35,
            'country': 'USA'
        },
        {
            'id': 2,
            'name': 'Martha Smith',
            'age': 60,
            'country': 'USA'
        },
        {
            'id': 3,
            'name': 'Fabio Alberto',
            'age': 18,
            'country': 'Italy'
        },
        {
            'id': 4,
            'name': 'Dietrich Stein',
            'age': 85,
            'country': 'Germany'
        }
    ]
  context={
    "animals":animals,
    "famili":families,
    "per":people
  }
  return render(request, 'index.html',context)
