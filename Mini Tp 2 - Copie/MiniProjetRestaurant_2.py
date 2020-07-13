nomReservation=""
while(bool(nomReservation)==False):# Je m'assure que le client rentre quelque chose avec un booléen.
    nomReservation=input("A quel nom voulez vous faire votre réservation ? : ")
nomReservation=nomReservation.lower()
nomReservation=nomReservation.title()#Je met la variable en minuscule puis en titre pour faire un titre si jamais les clients se sont trompés.

nombrePersonnes=int(input("Combien de personnes invitez vous "+nomReservation+" ? : "))
nombreMenuEnfant=0
menus=[0]*nombrePersonnes

for i in range(nombrePersonnes):# Je fais une boucle pour aller plus vite
    while(menus[i]!=6 and menus[i]!=12 and menus[i]!=16 and menus[i]!=20):#Je m'assure que le menu rentré est bien égal à 6,12,16 ou 20 €
        menus[i]=int(input("A combien voulez vous votre menu, client "+ str(i+1)+" ? : "))
    if(menus[i]==6):
        nombreMenuEnfant=nombreMenuEnfant+1
    i=i+1

nombreBoissons=int(input("Combien prendrez vous de boissons ? : "))
nombresCafes=int(input("Combien prendrez vous de cafés ? : "))

def cafesOfferts():
    """ Je défini une fonction CafesOfferts qui renvoie OUI ou NON en fonction du prix des menus"""
    totalMenus=0
    for i in range(nombrePersonnes):
        totalMenus=totalMenus+menus[i]
        i=i+1
    if(totalMenus>35 or nombreMenuEnfant<=nombrePersonnes/2):
        return 'OUI'
    else:
        return 'NON'

def total(menus,nombreBoissons, nombresCafes):
    """ Je défini une fonction total qui donne le cout total en fonction de si le cout des menus est supérieur à 35 il comptes les cafés gratuits sinon ils ajoute leurs prix."""
    totalCout=0
    for i in range(nombrePersonnes):
        totalCout=totalCout+menus[i]#J'ajoute le prix des menus avec une boucle
        i=i+1
    if (totalCout>35 or nombreMenuEnfant<=nombrePersonnes/2):#Si le cout des menus est supérieur à 35 € je ne fais qu'ajouter le prix des boissons au menu
        totalCout=totalCout+(3*nombreBoissons)
        return totalCout
    else:#Sinon si le prix des menus est inferieur à 35 j'ajoute aussi le prix du menus 
        totalCout=totalCout+(3*nombreBoissons)
        totalCout=totalCout+nombresCafes
        return totalCout

def TVA():
    TVA=float(((total(menus,nombreBoissons, nombresCafes)*10)/100))
    return TVA

def affiche(nomReservation,menus,nombreBoissons,nombresCafes):
    """Je crée une fonction affiche qui affiche un récapitulatif de la commande"""
    print(80*"_","\nNom de la reservation : ",nomReservation, "\nNombre de personnes invitées : ",nombrePersonnes)
    for i in range(nombrePersonnes):#Je crée une boucle pour afficher les menus.
        print("Menu client", i+1, " : ",menus[i], "€")
    print("Nombre de boissons : ",nombreBoissons,"\nNombre de cafés : ",nombresCafes, "\n    Café(s) offert(s) : ",cafesOfferts(),"\nTotal : ",total(menus,nombreBoissons,nombresCafes),"€\nTVA : ",float(TVA()),"€")
    return


affiche(nomReservation,menus,nombreBoissons,nombresCafes) # J'affiche le récapitulatif avec la fonction affiche
