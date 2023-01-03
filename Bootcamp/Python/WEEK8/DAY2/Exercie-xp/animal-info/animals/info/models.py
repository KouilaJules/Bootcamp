from django.db import models

class Animals(models.Model):
    nom = models.CharField(max_length=200,null=True)
    legs= models.CharField(max_length=200,null= True)
    weight = models.IntegerField(),
    height = models.IntegerField(),
    speed  = models.CharField(max_length=200, null=True),
    family = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.nom

class Familles(models.Model):
    nom = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.nom    
# Create your models here.
