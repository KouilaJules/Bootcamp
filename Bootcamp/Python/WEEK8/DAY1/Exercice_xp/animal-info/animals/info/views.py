
from django.shortcuts import render, get_object_or_404
from .models import Animal, Family

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'info/animal_detail.html', {'animal': animal})

def family_detail(request, family_id):
    family = get_object_or_404(Family, id=family_id)
    animals = Animal.objects.filter(family=family)
    return render(request, 'info/family_detail.html', {'family': family, 'animals': animals})

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'info/animal_list.html', {'animals': animals})