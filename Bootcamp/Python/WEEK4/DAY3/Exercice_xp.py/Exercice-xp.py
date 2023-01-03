#####EXERCICE 1################
print("======EXERCICE 1 =======")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictio =dict(zip(keys,values))
print(dictio)


##EXERCICE 2 #######
print("======EXERCICE 2 =======")
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
Prixperson = dict()
for i,j in family.items():
    if j<3 :
        Prixperson[i]= 0
    elif j in range(3,13):
        Prixperson[i]= 10
    else :
        Prixperson[i]= 15      

prix=[]     
print("LE PRIX QUE PERSONNE DE LA FAMILLE DOIT PAYER:")   
for i,j in Prixperson.items():
    print(f"{i} : {j}$")
    prix.append(j)
TOTALprix=sum(prix)    
    
print(f"Le total a payer est: {TOTALprix}$ ") 
#===============Bonus=============== 
print("======VOYER ENTRER LA PERSONNE QUI VEUT LE BILLET ET SON AGE=====")
famiDict= dict()
i=1
etat=''
while etat!='q':
    person=input(f"Entrer la personne {i}:")
    age =int(input("Entrer son age:"))
    famiDict[person]=age
    etat=input("Entrer \'q\' pour arreter la saisi and any key continu the the saisi:")
    i+=1
Prixperson = dict()
for i,j in famiDict.items():
    if j<3 :
        Prixperson[i]= 0
    elif j in range(3,13):
        Prixperson[i]= 10
    else :
        Prixperson[i]= 15      

prix=[]     
print("LE PRIX QUE PERSONNE DE LA FAMILLE DOIT PAYER:")   
for i,j in Prixperson.items():
    print(f"{i} : {j}$")
    prix.append(j)
TOTALprix=sum(prix)    
    
print(f"Le total a payer est: {TOTALprix}$ ") 

###EXERCICE 3####################
print("======EXERCICE 3 =======")
brand= {
    "name": 'Zara', 
    "creation_date": 1975 ,
    "creator_name": ['Amancio Ortega Gaona'],
    "type_of_clothes":['men', 'women', 'children', 'home' ],
    "international_competitors": ['Gap', 'H&M', 'Benetton' ],
    "number_stores": 7000 ,
    "major_color":{
        "France": 'blue', 
        "Spain":'red', 
        "US": ['pink', 'green']

    }
}    

##modification du noombre de magasin a 2
brand["number_stores"]= 2
print("EXPLIVATIOIN SUR LES CLIENT DE ZARA")
print("ZARAS est une marque des vetements des hommes,des femmes ,des enfant et aussi une marque pour les outils de maisons \n")

##CREATION DE LA NOUVELLE CLEF VALEURS DANS LE DICTIONNAIRE
brand["country_creation"]='Spain'
if 'international_competitors' in brand:
    brand['international_competitors']=['Desigual']
    
###suppression des informations sur la date de creation 
brand.pop("creation_date")

##Impression du dernier concurent international
dernier=brand['international_competitors'].pop() 
brand['international_competitors'].append(dernier)
print(f"Le dernier concurent international est: {dernier}") 
longuer= len(brand)

##impression des clefs du dictionnaire
for i in brand:
    print(i) 

#CREATION D'UN NOUVEAU DICRIONNAIRE 
more_on_zara={
    "creation_date": 1975,
    "number_stores": 10000
}

for i,j in more_on_zara.items():
    brand[i]=j
stock=brand["number_stores"]
print(f"le nombre de stock est:{stock}")    

###Exercice 4 ###################
print("======EXERCICE 4 =======")
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
print("1er resultat\n")
s=0
disney_users_A= dict()
for i in users:
    disney_users_A[i]=s
    s+=1
print(disney_users_A)

print("2eme resultat\n")
s=0
disney_users_B= dict()
for i in users:
    disney_users_B[s]=i
    s+=1
print(disney_users_B)

print("3eme resultat\n")
users.sort()
s=0
disney_users_C= dict()
for i in users:
    disney_users_C[i]=s
    s+=1
print(disney_users_C)

#les caracteres dont les noms contiennent la lettre "i"
print("Les noms qui contiennent le caractere \'i\' ")
s=0
lettre_i=dict() 
for i in users:
    if 'i' in i:
        lettre_i[i]=s
        s+=1
print(lettre_i)

print("Les noms qui contiennent le caractere \'m\' ou \'p\' ")
s=0
lettre_m_p=dict() 
for i in users:
    if 'M'== i[0] or 'P'== i[0]:
        lettre_m_p[i]=s
        s+=1
print(lettre_m_p)
