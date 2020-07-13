from tkinter import*
maFenetre2=Tk()
maFenetre2.title("Veuillez rentrer votre commande")
maFenetre2.geometry('400x500+100+100')
maFenetre2.config(bg='white', cursor='star')#Je défini les paramètres de ma fenêtre


nomReservation=""#Je défini mes variables.
nombrePersonnes=0
Confirmation=False
nombreMenuEnfant=0

nomReservation=StringVar()
Label1=Label(maFenetre2,text="Sous quel nom voulez vous faire cette reservation ?",bg='white',fg='black',font=("Helvetica", '12','italic')).pack(fill=Y, padx=5,pady=5)
nomReservationEntree=Entry(maFenetre2,textvariable=nomReservation)
nomReservationEntree.focus_set()
nomReservationEntree.pack(fill=Y, padx=5,pady=5)

nombrePersonnes=IntVar()
Label2=Label(maFenetre2,text="Quel nombre de personnes voulez vous inviter ?",bg='white',fg='black',font=("Helvetica", '12','italic')).pack(fill=Y, padx=5,pady=5)
nombrePersonnesEntree=Entry(maFenetre2,textvariable=nombrePersonnes)
nombrePersonnesEntree.focus_set()
nombrePersonnesEntree.pack(fill=Y, padx=5,pady=5)#Je défini mes widgets Entrée
if(bool(str(nombrePersonnes.get()))==True):
    Confirmation=True

nombreMenuEnfant=0


def suite():
    """Je défini une fonction suite pour pouvoir faire apparaitre un nombre variable de menus""" 
    global menus
    global nombrePersonnes
    global nombreBoissons
    global nombresCafes
    if(Confirmation==True):#Je m'assure que le client à bien rentré le nombre de personnes.
        nombrePersonnes=int(nombrePersonnes.get())
        menus=[0]*nombrePersonnes
        for i in range(nombrePersonnes):
            menus[i]=IntVar()#Je défini mes menus en IntVar
        for i in range(nombrePersonnes):# Je fais une boucle pour aller plus vite        
            Label3=Label(maFenetre2,text="A combien voulez vous votre menu, client "+ str(i+1)+" ?",bg='white',font=("Helvetica", '12','italic')).pack(fill=Y, padx=5,pady=5)
            prixMenusEntree=Entry(maFenetre2,textvariable=menus[i])
            prixMenusEntree.focus_set()
            prixMenusEntree.pack(fill=Y, padx=5,pady=5)
            i=i+1
    nombreBoissons=IntVar()

    Label4=Label(maFenetre2,text="Combien prendrez vous de boissons ?",bg='white',fg='black',font=("Helvetica", '12','italic')).pack(fill=Y, padx=5,pady=5)
    nombreBoissonsEntree=Entry(maFenetre2,textvariable=nombreBoissons)
    nombreBoissonsEntree.focus_set()
    nombreBoissonsEntree.pack(fill=Y, padx=5,pady=5)

    nombresCafes=IntVar()
    
    Label5=Label(maFenetre2,text="Combien prendrez vous de cafés ?",bg='white',fg='black',font=("Helvetica", '12','italic')).pack(fill=Y, padx=5,pady=5)
    nombresCafesEntree=Entry(maFenetre2,textvariable=nombresCafes)
    nombresCafesEntree.focus_set()
    nombresCafesEntree.pack(fill=Y, padx=5,pady=5)

    BouttonAffiche=Button(maFenetre2,text="Afficher le récapitulatif",command=affiche,bg='white',fg='black',font=("Helvetica", '11','italic'),relief='groove').pack(fill=Y, padx=5,pady=5) # J'affiche le récapitulatif avec la fonction affiche
    return

buttonSuite=Button(maFenetre2, text="Pour remplir la suite ayez rempli le nombre de personnes invitées", command=suite, bg='white',fg='black',font=("Helvetica", '10','italic'),relief='groove').pack(fill=Y,padx=5,pady=5)
#Je fais un boutton retournant la fonction affiche quand on l'appui

def cafesOfferts():
    """ Je défini une fonction CafesOfferts qui renvoie OUI ou NON en fonction du prix des menus"""
    global nombreMenuEnfant
    nombreMenuEnfant=0
    totalMenus=0
    for i in range(int(nombrePersonnes)):
        totalMenus=totalMenus+menus[i].get()
        if(menus[i].get()==6):
            nombreMenuEnfant=nombreMenuEnfant+1
                
        i=i+1
    if(totalMenus>35 or nombreMenuEnfant<=int(nombrePersonnes)/2):
        return "OUI"
    else:
        return "NON"

def total():
    """ Je défini une fonction total qui donne le cout total en fonction de si le cout des menus est supérieur à 35 il comptes les cafés gratuits sinon ils ajoute leurs prix."""
    totalCout=0
    for i in range(int(nombrePersonnes)):
        totalCout=totalCout+menus[i].get()#J'ajoute le prix des menus avec une boucle
        i=i+1

    if(totalCout>35 or nombreMenuEnfant<=int(nombrePersonnes)/2):#Si le cout des menus est supérieur à 35 € je ne fais qu'ajouter le prix des boissons au menu
        totalCout=totalCout+(3*nombreBoissons.get())
        return totalCout
    else: #Sinon si le prix des menus est inferieur à 35 j'ajoute aussi le prix du menus 
        totalCout=totalCout+(3*nombreBoissons.get())
        totalCout=totalCout+nombresCafes.get()
        return totalCout

def affiche():
    global nomReservation
    maFenetre1=Tk()
    maFenetre1.title("Récapitulatif de la commande de "+nomReservation.get().lower().title())
    maFenetre1.geometry('400x'+str(250+25*nombrePersonnes)+'+100+100')
    maFenetre1.config(bg='white', cursor='star')
    """Je crée une fonction affiche qui affiche un récapitulatif de la commande"""
    label1=Label(maFenetre1,text="\nNom de la reservation : "+nomReservation.get().lower().title()+ "\nNombre de personnes invitées : "+str(nombrePersonnes),bg='white',fg='black',font=("Helvetica", '12','italic')).pack(fill=Y,padx=5,pady=5)
    for i in range(nombrePersonnes):#Je crée une boucle pour afficher les menus.
        label2=Label(maFenetre1,text="Menu client " +str(i+1)+" : "+str(menus[i].get())+"€",bg='white',fg='black',font=("Helvetica", '12','italic')).pack(fill=Y,padx=5,pady=5)
    label3=Label(maFenetre1,text="Nombre de boissons : "+str(nombreBoissons.get())+"\nNombre de cafés : "+str(nombresCafes.get())+"\n    Café(s) offert(s) : "+cafesOfferts()+"\nTotal : "+str(total())+"€\nTVA : "+str(float(((total()*10)/100)))+"€",bg='white',fg='black',font=("Helvetica", '12','italic')).pack(fill=Y,padx=5,pady=5)
    maFenetre1.mainloop()
    return

maFenetre2.mainloop()
