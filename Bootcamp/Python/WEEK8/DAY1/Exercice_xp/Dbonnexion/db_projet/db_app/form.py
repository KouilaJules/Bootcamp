from django import forms
from db_app.models import Locataire

class LocataireForm(forms.ModelForm):
    
    class Meta:
        model =Locataire
        fields ='__all__'