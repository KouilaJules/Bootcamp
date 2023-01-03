### DEFI 1 ################
# print("=======DEFI 1=======")
# mot=input("Entrer un mot :")
# enu_mot=[]
# lists=[]
# dict_mot=dict()
# for i in enumerate(mot):
#     enu_mot.append(i)
# for i,j in enu_mot:
#    lists.append(j)
#    index =lists.index('s')

# print(index)

### DEFI 2 ##############

items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1000,
  "Fertilizer": 20
}
list_product=[]

print("======Menu ======\n")
for s,t in items_purchase.items():
    print(f"{s}: ${t}")

print("\n")
wallet=int(input("Entrer votre argent ($) pour connaitre la liste des produits aue vous pouvez acheter:"))
print("\n")
for i,j in items_purchase.items():
    if wallet>=j:
        list_product.append(i)
print("La liste des produit que vous pouvez acheter est:")        
if list_product !=[]:
    list_product.sort()
    print(list_product)    
else:
    print('RIEN')    