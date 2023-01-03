"""maliste = []
maliste.append("Jules")
maliste.append("Arman")
maliste.append("Bruno")
maliste.append("Kini")
maliste.append("Franck")

print(maliste)
print(len(maliste))

print("le test sur les dictionnaires en python ")


Personne= dict()
Personne["Jules"]= ["gros","grand"]
Personne["Jean"]= ["gros","grand"]

print(Personne)

print(Personne["Jules"][1])

i=0
while i<=10:
    print(i)
    i=i+1
    
    
for i in range(0,111):
    print(i)
    
    
#######l'usage des boucles sur le liste#####
Liste =["armand","Roland","Pacome","Salif","Fanta","Sali","Armel"]

for i in range(len(Liste)):
    print(Liste[i])    

Liste =[{x**2:Liste[x]}for x in range(len(Liste))]
Liste

dicte=dict()
for i in range(len(Liste)):
    dicte[i*i]=Liste[i]   

for i in dicte:
    print(i,dicte[i])
    
##l'usge des foncfion ###

def somme(a,b):
    som= a+b
    print(f"la somme de {a} et{b} est egale a {som}")    

somme(4,6)    
nombre_paire=[]
def number_Paire(list_nombre):
    for i in range(len(list_nombre)):
        if list_nombre[i]%2==0:
            nombre_paire.append(list_nombre[i]) 
    print("les nombres paires de la liste sont:")
    print(nombre_paire)
    
number_Paire([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])


def sommes(*args): 
    print(sum(args))   
sommes(2,4,6)  

def diction (**Kwargs):
    for (i,j) in Kwargs.items():
        print((i,j))
        
diction(ribou=4,arman=12)
###l'usage des fonctions lambda####
maFonction= lambda s: s.upper()
print(maFonction("Moussa"))
    """
"""
class Voiture:
    marque = "Kia"
    def _init_(self):
        self.couleur = "Noir"      
voiture1 =Voiture()
print(f"{voiture1.couleur}")
"""
import psycopg2
#Variable de connection à la base de donnée
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'klju2001'
DATABASE = 'ibam'

#Connection au serveur

try:
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD)
    print("conection reussie!!")
except psycopg2.Error as e:
    print("connection refusé veillez verifir les paramettre de connection!!")
    
 #Validation des transaction
 
connection.autocommit = True
cursor = connection.cursor()

#Creation de la BD
cursor.execute('DROP DATABASE IF EXISTS {};'.format('ibam'))
cursor.execute("CREATE DATABASE ibam;")

#Coneection à la BD
try:
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    print("conection reussie!!")
except psycopg2.Error as e:
    print("connection refusé veillez verifir les paramettre de connection!!")
    
    
 #Creation de la table student    

#cursor.execute("CREATE TABLE student (name VARCHAR(255), firstname VARCHAR(255), phone VARCHAR(255), address VARCHAR(255));")

#Insertion des données
"""
values = [
      ('Peter', 'Grid', '77445511','Lowstreet 4'),
    ('All', 'Grid', '77445511','Lowstreet 4'),
    ('Vall', 'Grid', '77445511','Lowstreet 4'),
    ('Til', 'Grid', '77445511','Lowstreet 4'),
    ('TO', 'Grid', '77445511','Lowstreet 4'),
    ('KA', 'Grid', '77445511','Lowstreet 4'),
    ('DK', 'Grid', '77445511','Lowstreet 4'),
    ('SQAZ', 'Grid', '77445511','Lowstreet 4'),
    ('NAD', 'Grid', '77445511','Lowstreet 4'),
    ('AGe', 'Grid', '77445511','Lowstreet 4')
]
cursor.executemany("INSERT INTO student VALUES(%s,%s,%s,%s)", values)
connection.commit()
print(cursor.rowcount, "line was inserted.")

"""
#Lecture ds données

sql1 = "SELECT * FROM student;"
cursor.execute(sql1)
for data in cursor.fetchall() :
    print(data)
        
    
    
    
  