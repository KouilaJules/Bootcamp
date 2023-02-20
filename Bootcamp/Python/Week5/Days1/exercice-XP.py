
########Exercice1:Cats###############
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat("Minou", 3)
cat2 = Cat("Miss", 5)
cat3 = Cat("Bobby", 2)

def find_oldest_cat(cats):
    oldest_cat = None
    for cat in cats:
        if not oldest_cat:
            oldest_cat = cat
        elif cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat
cats = [cat1, cat2, cat3]
oldest_cat = find_oldest_cat(cats)
print(f"Le chat le plus âgé est {oldest_cat.name}, et a {oldest_cat.age} ans.")

############Exercice2:Dogs#############
class Dog:
  def __init__(self, name, height):
    self.name = name
    self.height = height

  def bark(self):
    print(f"{self.name} goes woof!")

  def jump(self):
    print(f"{self.name} jumps {self.height * 2} cm high!")

# Create objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Print details and call methods
print(f"{davids_dog.name} is {davids_dog.height} cm tall")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall")
sarahs_dog.bark()
sarahs_dog.jump()

# Check which dog is bigger
if davids_dog.height > sarahs_dog.height:
  print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
else:
  print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")

##############Exercice3:Who’s the song producer?######
class Song:
  def __init__(self, lyrics):
    self.lyrics = lyrics

  def sing_me_a_song(self):
    for line in self.lyrics:
      print(line)

# create an object of the Song class
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

# call the sing_me_a_song method on the object
stairway.sing_me_a_song()

#############Exercice4:Afternoon at the Zoo##############
class Zoo:
  def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

  def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

  def get_animals(self):
        for animal in self.animals:
            print(animal)

  def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

  def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            if animal[0] not in groups:
                groups[animal[0]] = [animal]
            else:
                groups[animal[0]].append(animal)
        return groups

  def get_groups(self):
        groups = self.sort_animals()
        for key in groups:
            print(key, ":", ", ".join(groups[key]))


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Giraffe")  # This should not add a duplicate Giraffe

# Get the animals in the zoo
ramat_gan_safari.get_animals()

# Sell the Elephant
ramat_gan_safari.sell_animal("Elephant")

# Get the animals in the zoo again
ramat_gan_safari.get_animals()

# Get the groups of animals in the zoo
ramat_gan_safari.get_groups()
