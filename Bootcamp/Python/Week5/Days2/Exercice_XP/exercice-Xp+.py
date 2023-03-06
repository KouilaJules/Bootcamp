#Exercice 1 ##########

class Family:
    def __init__(self, nom_de_famille, membres):
        self.nom_de_famille = nom_de_famille
        self.membres = membres

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.membres.append(kwargs)
        print(f"Félicitations à la famille {self.nom_de_famille} pour l'arrivée du nouveau-né {kwargs['name']} !")

    def is_18(self, name):
        for membre in self.membres:
            if membre['name'] == name:
                return membre['age'] >= 18
        return False

    def family_presentation(self):
        print(f"La famille {self.nom_de_famille} est composée de :")
        for membre in self.membres:
            print(f"{membre['name']} ({membre['age']} ans, {membre['gender']}, {'enfant' if membre['is_child'] else 'adulte'})")

            
famille = Family("Doe", [{'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False}])
famille.born(name='Emma', age=0, gender='Female')
print(famille.is_18('Michael'))  # True
print(famille.is_18('Emma'))  # False
famille.family_presentation()            
            
##Exercice 2 #####       
 
class TheIncredibles(Family):
    
    def __init__(self, membres, nom_de_famille):
        super().__init__(membres, nom_de_famille)
        for membre in self.membres:
            membre['power'] = ''
            membre['incredible_name'] = ''
    
    def use_power(self, nom):
        for membre in self.membres:
            if membre['name'] == nom:
                if membre['age'] >= 18:
                    print(f"{membre['name']} peut utiliser son pouvoir : {membre['power']}.")
                else:
                    raise Exception(f"{membre['name']} n'a pas plus de 18 ans !")

    def incredible_presentation(self):
        super().family_presentation()
        for membre in self.membres:
            print(f"{membre['name']} : {membre['power']} - {membre['incredible_name']}")

# Données initiales
membres = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]
nom_de_famille = 'Incredibles'

# Instanciation de la classe
famille = TheIncredibles(membres, nom_de_famille)

# Appel de la méthode incredible_presentation
famille.incredible_presentation()

# Ajout de Baby Jack
famille.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown', incredible_name='BabyJack')

# Appel de la méthode incredible_presentation après l'ajout de Baby Jack
famille.incredible_presentation()           
            