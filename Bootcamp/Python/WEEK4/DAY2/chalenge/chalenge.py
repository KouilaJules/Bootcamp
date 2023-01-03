print("======Chalenge1========")
number= int(input("Entrer nombre:"))
length= int(input("Entrer la taille de la liste:"))
list_number=[]
i= number
while len(list_number)<length:
    if i%number==0:
        list_number.append(i)
    i+=1     
 
print(f"number:{number} - length {length} - {list_number}")   


print("======chalenge2=======")
chaine= input("Entrer une chaine de caractere:")
final_string=""
set_chaine= set()
for i in chaine:
    set_chaine.add(i)
for t in set_chaine:
    final_string +=t
print(f"user\'s word:\"{chaine}\" - \"{final_string}\"")     