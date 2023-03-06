###Exercice 1#############

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass

bengal = Bengal('Bengie', 2)
chartreux = Chartreux('Charlie', 3)
siamese = Siamese('Sia', 1)

all_cats = [bengal, chartreux, siamese]

sara_pets = Pets(all_cats)
sara_pets.walk()


###Exercice 2 ##############
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} aboie"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if self_score > other_score:
            return f"{self.name} a gagné le combat"
        elif other_score > self_score:
            return f"{other_dog.name} a gagné le combat"
        else:
            return "Match nul"
        
# creer des Chiens       
chien1 = Dog("Max", 4, 12) 
chien2 = Dog("Copain", 2, 10) 
chien3 = Dog("Rocky", 3, 15)       


#Exercice 3 ########
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        names = [self.name]
        for dog in args:
            names.append(dog.name)
        print(f"{' '.join(names)} jouent ensemble")

    def do_a_trick(self):
        if self.trained:
            tricks = ["fait un tonneau", "se dresse sur ses pattes arrière",
                      "te serre la main", "fait le mort"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} ne peut pas faire un tour car il n'est pas dressé!")
                       
            
# Créer quelques chiens
dog1 = PetDog("Fido", 3, 15)
dog2 = PetDog("Rex", 5, 20)
dog3 = PetDog("Lassie", 2, 10)

# Entraîner le premier chien
dog1.train()

# Faire jouer les chiens ensemble
dog2.play(dog1, dog3)

# Faire faire un tour aux chiens entraînés
dog1.do_a_trick()
dog2.do_a_trick()             
        