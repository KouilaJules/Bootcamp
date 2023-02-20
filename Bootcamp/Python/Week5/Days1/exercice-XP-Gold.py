
############Exercice1: Geometry########
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)

    def definition(self):
        return f"Un cercle est une forme géométrique avec tous les points de son périmètre à la même distance, appelée rayon, de son centre."
circle = Circle(5)
print(circle.perimeter())  # afficher le périmètre 31.41592653589793
print(circle.area())  # afficher la surface 78.53981633974483
print(circle.definition())  # imprimer "Un cercle est une figure géometrique avec tous les points de son périmètre à la même distance, appélée rayon, de son centre."


##########Exercice2: Custom List Class######################
