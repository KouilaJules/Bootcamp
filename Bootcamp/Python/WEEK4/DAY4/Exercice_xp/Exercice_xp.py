#####Exercice 1############################
print("===========Exercice 1 ==========")
def display_message():
    return print("A la fin de cette formation nous serons des Developpeurs FULLstarK ")

display_message()

####Exercice 2##########
print("===========Exercice 2 ==========")
def favorite_book(title):
    return print(f"One of my favorite books is << {title} >>")

favorite_book("Monde doute")

###Exercice 3 ################
print("===========Exercice 3 ==========")
def describe_city(city,country):
    if city=='':
        city = 'Ouagadougou'
    return print(f"{city} is in {country}")

describe_city('','Burkina Faso')

###### Exercice 4 ############
print("===========Exercice 4 ==========")
from random import *
def aliaNomber(number):    
    if number in range(1,101):
        alianumb=randint(1,101)
        print(f"je suis un enfant de dieu {number} {alianumb}")
        if number!=alianumb:
            return print(f"Vous avez echouez: nombre entrer :{number} nombre aliatoire:{alianumb} ")        
        else:
            return print(f"Vous avez ressit: nombre entrer :{number} nombre aliatoire:{alianumb} ")        

    else:
       return print(f"le nombre {number} n'est pas compris entre 1 et 100") 

aliaNomber(45)          

####Exercice 5############
print("===========Exercice 5======")

def make_shirt(size,text):
    if size=='':
        size='XXXL'
    if text =='':
        text="J'aime Python"
            
    return print(f"The size of the shirt is {size} and the text is {text}")
 
make_shirt('','') 
   
####Exercice 6##########
print("==========Exercice 6==========")
  
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    print("La liste des magicains:")
    for i in magician_names:
        print(f"{i}")   
        
show_magicians()        

def make_great():
    for i in magician_names:
        y=magician_names.index(i)
        magician_names[y]=i+' the Great'

make_great()
show_magicians()

####Exercie 7##########
print("========Exercice 7========")

def get_random_temp():
    y =randint(-10,41)
    return y        

def main():
    temp=get_random_temp()
    print(f"La température actuelle est de {temp} degrés Celsius.")
    print("CONEIL:")
    if temp<0:
        print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    if temp in range(0,16):
        print("Assez froid ! N'oubliez pas votre manteau")
    if temp in range(16,24):
        print("beau temps ")  
    if temp in range(24,32):
        print("beau temps ")          
    if temp in range(32,40):
        print("if faut sortir avec un parasoleil")    
        
main()  

print("modification sur les fonctions") 

def get_random_temp(saison):
    if saison=='ete':
        y =randint(-10,16)
    if saison=='automne':
        y =randint(16,32)
    if saison=='hiver':
        y =randint(32,41)  
    return y        

def main():
    saison=input("Entrez la saison('ete' 'automne' 'hiver'): ")
    temp=get_random_temp(saison)
    print(f"La température actuelle est de {temp} degrés Celsius.")
    print("CONEIL:")
    if temp<0:
        print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    if temp in range(0,16):
        print("Assez froid ! N'oubliez pas votre manteau")
    if temp in range(16,24):
        print("beau temps ")  
    if temp in range(24,32):
        print("beau temps ")          
    if temp in range(32,40):
        print("if faut sortir avec un parasoleil")    
        
main()
