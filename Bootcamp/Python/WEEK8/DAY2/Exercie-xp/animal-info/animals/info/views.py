from django.shortcuts import render
from info.models import Animals
from info.models import Familles

def animals(request):
  animals = Animals.objects.all()
  context= {
    "animal":animals
  }
  return render (request,"index.html",context)

def family(request):
  families = Familles.objects.all()
  contexte = {
    "family":families
  }
  return render (request,"index.html",contexte)