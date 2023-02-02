from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render



def choise(request):
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
    
    person = people.sort(key=lambda people: people.get('age'))
    context={
        "per":people,
        "pers":person
    
    }
    return render(request, 'index.html',context)

def people(request,id):
    peoples = [
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

    if peoples[' ']['id']==id:
        peo=peoples[i]
    context={'per':peo}
    return render(request,'people.html',context)