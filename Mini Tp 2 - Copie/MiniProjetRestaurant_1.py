menus=[0]*4#Je crée un tableau pour rentrer mes valeurs de menus
nomReservation=""
while(bool(nomReservation)==False):# Je m'assure que le client rentre quelque chose avec un booléen et une boucle while
    nomReservation=input("A quel nom voulez vous faire votre réservation ? : ")
nomReservation=nomReservation.lower()
nomReservation=nomReservation.title()#Je mets la variable en minuscule puis en titre pour faire un titre si jamais les clients se sont trompés.


for i in range(4):# Je fais une boucle for pour aller plus vite
    while(menus[i]!=6 and menus[i]!=12 and menus[i]!=16 and menus[i]!=20):#Je m'assure que le menu rentré est bien égal à 6,12,16 ou 20 €
        menus[i]=int(input("A combien voulez vous votre menu, client "+ str(i+1)+" ? : "))
    i=i+1

nombreBoissons=int(input("Combien prendrez vous de boissons ? : "))
nombresCafes=int(input("Combien prendrez vous de cafés ? : "))

def cafesOfferts():
    """ Je définis une fonction CafesOfferts qui renvoie OUI ou NON en fonction du prix des menus"""
    totalMenus=0
    for i in range(4):#J'additionne le coût des menus
        totalMenus=totalMenus+menus[i]
        i=i+1
    if(totalMenus>35):
        return 'OUI'
    else:
        return 'NON'

def total(menus,nombreBoissons, nombresCafes):
    """ Je définis une fonction total qui donne le coût total selon que le coût des menus soit supérieur à 35 il compte les cafés gratuits sinon il ajoute leurs prix."""
    totalCout=0
    for i in range(4):
        totalCout=totalCout+menus[i]#J'ajoute le prix des menus avec une boucle for
        i=i+1
    if (totalCout>35):#Si le coût des menus est supérieur à 35 € je ne fais qu'ajouter le prix des boissons au menu
        totalCout=totalCout+(3*nombreBoissons)
        return totalCout
    else:#Sinon si le prix des menus est inferieur à 35 j'ajoute aussi le prix des cafés 
        totalCout=totalCout+(3*nombreBoissons)
        totalCout=totalCout+nombresCafes
        return totalCout

def affiche(nomReservation,menus,nombreBoissons,nombresCafes):
    """Je crée une fonction affiche qui affiche un récapitulatif de la commande"""
    print(80*"_","\nNom de la réservation : ", nomReservation)
    for i in range(4):#Je crée une boucle pour afficher les menus.
        print("Menu client", i+1, " : ",menus[i], "€")
    print("Nombre de boissons : ", nombreBoissons,"\nNombre de cafés : ", nombresCafes, "\n    Café(s) offert(s) : ", cafesOfferts(),"\nTotal : ", total(menus,nombreBoissons,nombresCafes),"€")
    return


affiche(nomReservation,menus,nombreBoissons,nombresCafes) # J'affiche le récapitulatif avec la fonction affiche






























            
        
    
