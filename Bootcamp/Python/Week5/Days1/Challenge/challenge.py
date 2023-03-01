class Farm:
    
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}
        
    def add_animal(self, animal_type, amount=1):
        if animal_type in self.animals:
            self.animals[animal_type] += amount
        else:
            self.animals[animal_type] = amount
        
    def get_info(self):
        animal_counts = []
        for animal_type, count in self.animals.items():
            animal_counts.append(f"{animal_type} : {count}")
        animal_counts.sort()
        info = f"{self.farm_name}'s farm\n" + "\n".join(animal_counts) + "\n\nE-I-E-I-0!"
        return info
    
    def get_animal_types(self):
        animal_types = list(self.animals.keys())
        animal_types.sort()
        return animal_types
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        animals = ", ".join(animal_types)
        return f"The {self.farm_name} farm has {animals}."
    

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())    