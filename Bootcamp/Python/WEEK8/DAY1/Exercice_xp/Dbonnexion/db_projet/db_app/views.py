from django.shortcuts import render
from db_app.models import Locataire
from db_app.form import LocataireForm


def index(request):
    #Recuperer et afficher les donnees
    locataires = Locataire.objects.all()

    #Enregistrement de donnees
    #test si la request est une soumission 
    if request.method == 'POST':
        #on initialise l
        form = LocataireForm(request.POST)
        if form.is_valid():
            form.save()
            form =LocataireForm()       
    else:
        form =LocataireForm()
    context = {"Locataires":locataires, "form":form}    
    return render(request, "index.html",context)