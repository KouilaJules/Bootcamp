

###exercice 1####
print("===========Exercice 1=======")
my_fav_numbers = {1,2,3,4,5}
my_fav_numbers.add(6)
my_fav_numbers.add(7)
print(my_fav_numbers)
my_fav_numbers.remove(7)
print(my_fav_numbers)
friend_fav_numbers={10,11,12,13}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


##exercice 2###
print("===========Exercice 9=======")
#il n'est pas possible d'ajouter plus d'entiers au tuple
print("il n'est pas possible d'ajouter plus d'emtier au tuple")


####exercice 3##
print("===========Exercice 3=======")
basket =["Banana","Apples","Oranges","Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.append("Apples")
print(basket)
num =basket.count("Apples")
print(f"il y'a {num} fois de Apples")
basket.clear()

for i in range(len(basket)):
    print(basket[i])
    
    
###exercice 4###   
print("===========Exercice 4=======")
#un float est reel il peut etre un entier ou un nombre a virgule 
# non 
step = 0.5
rnge = 5     # NOTE range = 1, i.e. span of data points
N = int(rnge / step)
lispro=[ x / pow(step,-1) for x in range(3, N + 1) ]    
print(lispro)

##Exercice 5####
print("===========Exercice 5=======")

for i in range(1,21):
    print(i)
    
for i in range(1,21):
    if i%2==0:
        print(i)   
 
 
###Exercice 6####
print("===========Exercice 6=======")
print("Entrer \'Jules\'pour quitter la boucle")
user_name=""
while user_name != "Jules":
    user_name=input("Input your Name:")        
    
    
###Exercice 7####
print("===========Exercice 7=======")

chaine_fruit=input("Entrer vos fruit preferes par ex \" apple mango cherry\":")
list_fruit=chaine_fruit.split()
nouveau_fruit=input("Entrer le nom de n'importe quel fruit:")
if nouveau_fruit in list_fruit:
    print("Vous avez choisi l'un de vos fruit preferes !Prendre plaisir!")  
else :
    print("Vous avez choisi un nouveau fruit. J'espere que tu apprecies") 


##Exercie 8 ###
print("===========Exercice 8=======")
garniture_liste=[]
garniture=""
while garniture !="quitter":
    garniture=input("Entrer un serie de garniture de pizza et saisir \'quitter\' pour quitter:")
    if garniture!="quitter":
        print("Cette garnuture seras ajouter a votre pizza")
        garniture_liste.append(garniture)         
        
garniture_nombre= len(garniture_liste)
total=  garniture_nombre*(10+2.5)
print(garniture_liste)
print(f"Le prix total est: {total}") 
 

#####Exercice 9####
print("===========Exercice 9=======")
total=0
nombre_personne=int(input("Entrer le nombre de personne qui un bullet:"))
for i in range(1,nombre_personne+1):
    age =int(input(f"Entrer l'age de la personne {i}:"))
    if age<3:
        billet= 0  
    if age in range(3,13):
        billet= 10
    elif age>12:
        billet =15       
    total=  total + billet
print(f"le cout total de tous les billet de la est : {total}$") 

print("PARTIE du CINEMA")
list_adolescent=["Armel","Armel","Arsene"]
i= 1
while i <=len(list_adolescent):
    print(f"adolescent {i}")
    nom_ado= input("Entrer votre Nom: ")
    age_ado=int(input("Entrer votre age:"))
    if age not in range(16,22):
       list_adolescent.pop(nom_ado)
    i= i+1  
print(f"la liste total est {list_adolescent}")     


####Xercice 10#####
print("===========Exercice 10=======")
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich","Pastrami sandwich","Pastrami sandwich"]
finished_sandwiches=[]
ques="oui"
while ques=="oui":
    sandwich= input("what sandwich is made and input \"none\" to exit:")
    if sandwich in sandwich_orders:
        finished_sandwiches= sandwich_orders.pop(sandwich)
    if sandwich=="none":
        ques=sandwich    
for i in finished_sandwiches:
    print(f"I made your {i}")    


###Exercice 11###
print("===========Exercice 11=======")
print("la charcuterie n'a plus de pastrami")
p="Pastrami sandwich"
while p in sandwich_orders:
    finished_sandwiches = sandwich_orders.remove(p)

print("la finale est :",finished_sandwiches)

