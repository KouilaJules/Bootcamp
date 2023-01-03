board=[['','',''],['','',''],['','','']]
joeur1=[['x','x','x'],['','',''],['','','']]
joeur11=[['','',''],['x','x','x'],['','','']]
joeur12=[['','',''],['','',''],['x','x','x']]
joeur13=[['x','',''],['x','',''],['x','','']]
joeur14=[['','','x'],['','','x'],['','','x']]
joeur15=[['','x',''],['','x',''],['','x','']]
joeur16=[['x','',''],['','x',''],['','','x']]
joeur17=[['x','',''],['','x',''],['','','x']]

joeur2=[['o','o','o'],['','',''],['','','']]
joeur21=[['','',''],['o','o','o'],['','','']]
joeur22=[['','',''],['','',''],['o','o','o']]
joeur23=[['o','',''],['o','',''],['o','','']]
joeur24=[['','','o'],['','','o'],['','','o']]
joeur25=[['','o',''],['','o',''],['','o','']]
joeur26=[['o','',''],['','o',''],['','','o']]
joeur27=[['o','',''],['','o',''],['','','o']]

 
def verification1(j):
    if board==joeur1 or board==joeur11 or board==joeur12 or board==joeur13 or board==joeur14 or board==joeur15 or board==joeur16 or board==joeur17 :
        j=1
    return j  

def verification2(je):
    if board==joeur2 or board==joeur21 or board==joeur22 or board==joeur23 or board==joeur24 or board==joeur25 or board==joeur26 or board==joeur27:
       je=1
    return je  
             
def main():
    print("======LE JEUE DE TIC TAC TOE=====\n")
    print("VOUS DEVEZ PRECISEZ LA POSITION A LA QUELLE VOUS VOYULEZ PLACEZ VOTRE MARAQUE")
    print("Commencer:")
    print("*************")
    print("*   |   |   *")
    print("*-----------*")
    print("*   |   |   *")
    print("*-----------*")
    print("*   |   |   *")
    print("*************")
    i=1
    j=0
    je=0
    while i<=9:
        
        if i%2!=0:
            print("Joeur 1")
            position1= int(input("Entrez la position pour la marque(X): "))
            if position1==1:
                board[0][0]='x'
            if position1==2:
                board[0][1]='x'
            if position1==3:
                board[0][2]='x'
            if position1==4:
                board[1][0]='x' 
            if position1==5:
                board[1][1]='x'
            if position1==6:
                board[1][2]='x'
            if position1==7:
                board[2][0]='x' 
            if position1==8:
                board[2][1]='x'
            if position1==9:
                board[2][2]='x'                  
        else:
            print("Joeur 2")
            position2= int(input("Entrez la position pour la marque(O): "))
            if position2==1:
                board[0][0]='o'
            if position2==2:
                board[0][1]='o'
            if position2==3:
                board[0][2]='o'
            if position2==4:
                board[1][0]='o' 
            if position2==5:
                board[1][1]='o'
            if position2==6:
                board[1][2]='o'
            if position2==7:
                board[2][0]='o' 
            if position2==8:
                board[2][1]='o'
            if position2==9:
                board[2][2]='o' 
        print("*************")
        print(f"* {board[0][0]} | {board[0][1]} | {board[0][2]}  *")
        print("*-----------*")
        print(f"* {board[1][0]} | {board[1][1]} | {board[1][2]}  *")
        print("*-----------*")
        print(f"* {board[2][0]} | {board[2][1]} | {board[2][2]}  *")
        print("*************")
        joker1=verification1(j)
        joker2=verification2(je)
      
        if joker1==1:
            print("winner is JOEUR 1")
        
        if joker2==1:
            print("Winner is JOEUR 2")
             
        if i==9:
            print("None Winner is aquality") 
          
       
    
         
main()          