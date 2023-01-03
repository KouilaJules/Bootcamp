from random import shuffle

chaine= input("Entrer une chaine de caractere comportant 10 caractere:")
if len(chaine)<10 :
    print("chaine n'est pas assez longue")
elif len(chaine)>10 :
    print("Chaine trop longue")    
prmier_caractere= chaine[0]
dernier_caractere = chaine[-1]
print(f"Le premier caractere de la chaine est \"{prmier_caractere}\" et le dernier caractere est \"{dernier_caractere}\"")   

print("construisons la chaine par caractere") 
for i in range(len(chaine)+1):
    print(chaine[0:i])

###LA POARTIE DE LA BONUS
print('partie du BONUS....') 
a = []
for char in chaine:
    a.append(char)

    shuffle(a)
t= ""
for z in a:
    t = t + z

print(t)