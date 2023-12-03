from random import*
from tkinter import*
import tkinter as tk
#import pygame
#from pygame import *

animal="Lapin"                     #str(input("Choisissez entre un lapin, un chat et un chien. "))
sexe="Boi"                  #str(input("CHoisissez son sexe. "))
nom="Billy"            #str((input("Donnez lui un nom. ")))
année=2022
mois=["mort","janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
moisnum=0           #int(input("Choisissez son mois de naissance en numéro: "))
jourmax=32

if moisnum > 12 or moisnum <= 0:
    moisnum=int(input("Choisissez son mois de naissance en numéro: "))

elif (moisnum == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12):
    jourmax = 31

elif (moisnum == 4 or mois == 6 or mois == 9 or mois == 11):
    jourmax = 30

elif moisnum == 2:
    if année %  4 == 0 or année % 400 == 0:
        jourmax = 29
    elif année % 100 == 0 and année % 400 != 0 or année % 4 == 0:
        jourmax = 28


jour=int(input("Entrez le jour de naissance: "))

while jour > jourmax or jour <= 0:
    jour=int(input("Entrez le jour de naissance: "))


money=100
sante=1
faim=0
bonheur=0
energie=0
Nbfood=[]*5
Nbmedecin=[]*2
Nbtoys=[]*4
m=1                    #nombre déterminant la chance d'être malade
malade=0

"""
def jouer_lapin():
    jouer_animal(1)

def jouer_chat():
    jouer_animal(2)

def jouer_chien():
    jouer_animal(3)

def sexm():
    sex_animal(1)

def sexf():
    sex_animal(2)
"""

men = Tk()
men.geometry("1100x800")
men.title("Tamagochi main menu")
can=Canvas(men,width=1100,height=800,background='#DDDDDD')
can.grid(rowspan=25, columnspan=3,column=0)
x,y=550,400
xa=550
ya=400


can.create_text(550,40,text="TAMAGOCHI",fill='#ff33e0',font=("arial",50))

can.create_text(550,90,text="Choisissez votre animal:",fill='black',font=("arial",20))

lapin = PhotoImage(file='image/easter-rabbit.png')
chat = PhotoImage(file='image/cat-profile.png')
chien = PhotoImage(file='image/icone_homme_chien.png')



lap = Button (image = lapin)
lap.grid(row=5,column=0)

cha = Button (image = chat)
cha.grid(row=5,column=1)

dog = Button (image = chien)
dog.grid(row=5,column=2)

male = PhotoImage(file='image/male.png')
female = PhotoImage(file='image/female-symbol.png')

can.create_text(550,250,text="Choisissez son sexe:",fill='black',font=("arial",20))

male = Button (image = male )
male.grid(row=8,column=0)

female = Button (image = female)
female.grid(row=8,column=2)

can.create_text(550,490,text="Donnez lui un nom:",fill='black',font=("arial",20))

nommenu = tk.Entry(men)
nommenu.grid(row=11, column=1)

can.create_text(550,570,text="Sa date de naissance:",fill='black',font=("arial",20))

can.create_text(550,750,text=("1 pour nourrir; 2 pour jouer; 3 pour soigner; 4 pour aller chez le vétérinaire; 5 pour aller aux boutique"),fill='black',font=("aral",18))
can.create_text(550,775,text=("T pour continuer et avancer sur les jours. Vous pouvez cliquer sur les bouton."),fill='black',font=("aral",18))


men.mainloop()



fen = Tk()
fen.geometry("1250x800")
fen.title("Tamagochi")
can=Canvas(fen,width=1100,height=800,background='white')
can.grid(rowspan=10, column=0)
x,y=550,400
xa=550
ya=400




vendeurimg = PhotoImage(file='image/vendeur1.png')
img=can.create_image(550,400,image=vendeurimg)


if animal == "lapin" or animal == "Lapin" or  animal == "LAPIN":
        normal = PhotoImage(file='image/lapin1.png')
        sad = PhotoImage(file='image/lapin2.png')
        happy = PhotoImage(file='image/lapin3.png')
        sante=80
        faim=90
        bonheur=120
        energie=100

if animal == "chien" or animal == "Chien" or animal == "CHIEN":
        normal = PhotoImage(file='image/chien1.png')
        #sad = PhotoImage(file='image/chien2.png')
        #happy = PhotoImage(file='image/chien3.png')
        sante=120
        faim=120
        bonheur=130
        energie=110

if animal == "chat" or animal == "Chat" or animal == "CHAT":
        normal = PhotoImage(file='image/chat1.png')
        #sad = PhotoImage(file='image/chat2.png')
        #happy = PhotoImage(file='image/chat3.png')
        sante=100
        faim=100
        bonheur=80
        energie=75



can.create_rectangle(0,700,1100,800,fill='white')
can.create_text(550,725,text=("Bonjour cher employé(e) de AAPA! Heureux de vous rencontrer vous avez fait le choix de vous occuper d'un "+animal+" "+sexe+" que vous avez choisi de nommer "+nom+"."),fill='black',font=("aral",11))

can.create_rectangle(900,0,1100,50,fill='white')
can.create_text(1000,25,text=(str(nom)+" est en bonne santé"),fill='black',font=("arial",10))

can.create_rectangle(0,0,50,50,fill='white')
can.create_text(25,10,text=("année:"),fill='black',font=("arial",10))
can.create_text(25,40,text=(année),fill='black',font=("arial",10))

can.create_rectangle(0,100,70,150,fill='white')
can.create_text(35,110,text=("mois:"),fill='black',font=("arial",10))
can.create_text(35,140,text=(mois[moisnum]),fill='black',font=("arial",10))

can.create_rectangle(0,200,50,250,fill='white')
can.create_text(25,210,text=("jour:"),fill='black',font=("arial",10))
can.create_text(25,240,text=(jour),fill='black',font=("arial",10))




santemax=sante
faimmax=faim
bonheurmax=bonheur
energiemax=energie

can.create_rectangle(0,300,60,375,fill='white')
can.create_text(30,320,text=("Maladie:"),fill='black',font=("arial",10))
can.create_text(30,350,text=(str(m)+" %"),fill='black',font=("arial",10))

can.create_rectangle(100,0,175,50,fill='white')
can.create_text(137.5,10,text=("Nom:"),fill='black',font=("arial",10))
can.create_text(137.5,40,text=(str(nom)),fill='black',font=("arial",10))

can.create_rectangle(200,0,275,50,fill='white')
can.create_text(237.5,10,text=("Sexe:"),fill='black',font=("arial",10))
can.create_text(237.5,40,text=(str(sexe)),fill='black',font=("arial",10))

can.create_rectangle(300,0,375,50,fill='white')
can.create_text(337.5,10,text=("animal:"),fill='black',font=("arial",10))
can.create_text(337.5,40,text=(str(animal)),fill='black',font=("arial",10))

can.create_rectangle(400,0,475,50,fill='white')
can.create_text(437.5,10,text=("Faim:"),fill='black',font=("arial",10))
can.create_text(437.5,40,text=(str(faim)+"/"+str(faimmax)),fill='black',font=("arial",10))

can.create_rectangle(500,0,575,50,fill='white')
can.create_text(537.5,10,text=("Bonheur:"),fill='black',font=("arial",10))
can.create_text(537.5,40,text=(str(bonheur)+"/"+str(bonheurmax)),fill='black',font=("arial",10))


can.create_rectangle(600,0,675,50,fill='white')
can.create_text(637.5,10,text=("Energie:"),fill='black',font=("arial",10))
can.create_text(637.5,40,text=(str(energie)+"/"+str(energiemax)),fill='black',font=("arial",10))

can.create_rectangle(700,0,775,50,fill='white')
can.create_text(737.5,10,text=("Argent:"),fill='black',font=("arial",10))
can.create_text(737.5,40,text=(str(money)+" €"),fill='black',font=("arial",10))

can.create_rectangle(800,0,875,50,fill='white')
can.create_text(837.5,10,text=("Santé:"),fill='black',font=("arial",10))
can.create_text(837.5,40,text=(str(sante)+"/"+str(santemax)),fill='black',font=("arial",10))



def nourrir():
    global faim,faimmax,m,money
    can.create_rectangle(0,700,1100,800,fill='white')
    can.create_text(550,750,text=("J'ai donné à manger à "+nom+" j'espère que ça ira."),fill='black',font=("aral",20))
    if money < 10:
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=("Pas assez d'argent"),fill='black',font=("aral",20))

    if money >= 10:
        faim=faim+40
        money=money-10
        if faim == faimmax:
            can.create_rectangle(0,700,1100,800,fill='white')
            can.create_text(550,750,text=("Bon, il semble que "+nom+" ai l'estomac plein je devrais arrêter de donner à manger"),fill='black',font=("aral",20))
        if faim > faimmax:
            faim = faimmax
            can.create_rectangle(0,700,1100,800,fill='white')
            can.create_text(550,750,text=("Mince! Je lui ai trop donné à mangé! J'espère qu'il ne va pas tomber malade"),fill='black',font=("aral",20))
            m=m+5        #ici on réduit la fenêtre de maladie car plus m est grand plus il y a de chance d'être malade
    maladie()

    can.create_rectangle(0,300,60,375,fill='white')
    can.create_text(30,320,text=("Maladie:"),fill='black',font=("arial",10))
    can.create_text(30,350,text=(str(m)+" %"),fill='black',font=("arial",10))

    can.create_rectangle(400,0,475,50,fill='white')
    can.create_text(437.5,10,text=("Faim:"),fill='black',font=("arial",10))
    can.create_text(437.5,40,text=(str(faim)+"/"+str(faimmax)),fill='black',font=("arial",10))

    can.create_rectangle(700,0,775,50,fill='white')
    can.create_text(737.5,10,text=("Argent:"),fill='black',font=("arial",10))
    can.create_text(737.5,40,text=(str(money)+" €"),fill='black',font=("arial",10))

    if faim==0:
        can.create_rectangle(400,0,475,50,fill='white')
        can.create_text(437.5,10,text=("Faim:"),fill='red',font=("arial",10))
        can.create_text(437.5,40,text=(str(faim)+"/"+str(faimmax)),fill='red',font=("arial",10))


def jouer():
    global bonheur,bonheurmax,energie,energiemax,m,sante
    if energie > 0 and bonheur > 0:
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=("Mon "+animal+" semble bien s'être amusé."),fill='black',font=("arial",20))
        energie = energie - 20
        bonheur = bonheur + 15
    elif energie <= 0:
        energie = 0
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" est trop épuisé pour jouer. Il vaut mieux rentrer."),fill='black',font=("arial",20))
    elif bonheur <= 20:
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" est trop triste"),fill='black',font=("arial",20))
    elif bonheur == bonheurmax:
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" est hyper heureux!"),fill='black',font=("arial",20))
    if bonheur > bonheurmax:
        bonheur = bonheurmax
        sante=sante - 5
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" est tellement heureux qu'il s'est blessé!"),fill='black',font=("arial",20))

        can.create_rectangle(800,0,875,50,fill='white')
        can.create_text(837.5,10,text=("Santé:"),fill='black',font=("arial",10))
        can.create_text(837.5,40,text=(str(sante)+"/"+str(santemax)),fill='black',font=("arial",10))

    can.create_rectangle(500,0,575,50,fill='white')
    can.create_text(537.5,10,text=("Bonheur:"),fill='black',font=("arial",10))
    can.create_text(537.5,40,text=(str(bonheur)+"/"+str(bonheurmax)),fill='black',font=("arial",10))

    can.create_rectangle(600,0,675,50,fill='white')
    can.create_text(637.5,10,text=("Energie:"),fill='black',font=("arial",10))
    can.create_text(637.5,40,text=(str(energie)+"/"+str(energiemax)),fill='black',font=("arial",10))

    if bonheur==0:
                can.create_rectangle(500,0,575,50,fill='white')
                can.create_text(537.5,10,text=("Bonheur:"),fill='red',font=("arial",10))
                can.create_text(537.5,40,text=(str(bonheur)+"/"+str(bonheurmax)),fill='red',font=("arial",10))

    expression()

def soigner():
    global malade,money,m,bonheur,sante,santemax
    if sante == santemax :
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" a déjà toute sa santé."),fill='black',font=("arial",20))
    elif sante < santemax and money < 20:
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=("Vous ne pouvez soigner "+nom+" vous manquez d'argent (20€ minimum)"),fill='black',font=("arial",20))
    elif sante < santemax and money >=20:
        sante += (santemax * 0.4)
        if sante > santemax:
            sante = santemax
        bonheur += 10
        money -= 20
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" semble être en meilleur santé."),fill='black',font=("arial",20))
        expression()

    can.create_rectangle(700,0,775,50,fill='white')
    can.create_text(737.5,10,text=("Argent:"),fill='black',font=("arial",10))
    can.create_text(737.5,40,text=(str(money)+" €"),fill='black',font=("arial",10))

    can.create_rectangle(500,0,575,50,fill='white')
    can.create_text(537.5,10,text=("Bonheur:"),fill='black',font=("arial",10))
    can.create_text(537.5,40,text=(str(bonheur)+"/"+str(bonheurmax)),fill='black',font=("arial",10))

    can.create_rectangle(800,0,875,50,fill='white')
    can.create_text(837.5,10,text=("Santé:"),fill='black',font=("arial",10))
    can.create_text(837.5,40,text=(str(sante)+"/"+str(santemax)),fill='black',font=("arial",10))

def veterinaire():
    #veterinaireimg = PhotoImage(file='veterinaire.png')
    #img=can.create_image(550,400,image=normal)
    global malade,money,m,bonheur
    if malade == 0 :
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" n'est pas malade, si vous voulez le soignez aller dans 'soigner'."),fill='black',font=("arial",20))
    elif malade == 1 and money < 50:
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=("Vous ne pouvez pas guérir "+nom+" vous manquez d'argent (50€ minimum)"),fill='black',font=("arial",20))
    if malade == 1 and money >=50:
        malade = 0
        m=1
        bonheur=50
        money -= 50
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" semble être en meilleur santé."),fill='black',font=("arial",20))
        expression()
        can.create_rectangle(900,0,1100,50,fill='white')
        can.create_text(1000,25,text=("Votre "+animal+" est en bonne santé"),fill='black',font=("arial",10))

    can.create_rectangle(700,0,775,50,fill='white')
    can.create_text(737.5,10,text=("Argent:"),fill='black',font=("arial",10))
    can.create_text(737.5,40,text=(str(money)+" €"),fill='black',font=("arial",10))

    can.create_rectangle(0,300,60,375,fill='white')
    can.create_text(30,320,text=("Maladie:"),fill='black',font=("arial",10))
    can.create_text(30,350,text=(str(m)+" %"),fill='black',font=("arial",10))

    can.create_rectangle(500,0,575,50,fill='white')
    can.create_text(537.5,10,text=("Bonheur:"),fill='black',font=("arial",10))
    can.create_text(537.5,40,text=(str(bonheur)+"/"+str(bonheurmax)),fill='black',font=("arial",10))

    can.create_rectangle(0,700,1100,800,fill='white')
    can.create_text(550,750,text=("Bienvenue !"),fill='black',font=("arial",20))

def boutique():
    global img,vendeurimg,money
    f=1             #valeur de la fenêtre
    can.create_rectangle(0,700,1100,800,fill='white')
    can.create_text(550,750,text=("Bienvenue  Monsieur ! Si vous avez besoin d'aide, n'hésitez pas !"),fill='black',font=("arial",20))
    if f == 1:
        if money >= 15:
            vendeurimg = PhotoImage(file='image/vendeur1.png')
            img=can.create_image(550,400,image=vendeurimg)
            can.itemconfig(img, image=vendeurimg)
            can.coords(img,550,400)
            can.create_rectangle(200,150,450,600,fill='white')
            can.create_text(325,300,text=("PRODUIT"),fill='black',font=("arial",15))
        if money < 15:
            vendeurimg = PhotoImage(file='image/vendeur2.png')
            img=can.create_image(550,400,image=vendeurimg)
            can.itemconfig(img, image=vendeurimg)
            can.coords(img,550,400)
            can.create_rectangle(200,150,450,600,fill='white')
            can.create_text(325,300,text=("PAS ASSEZ D'ARGENT"),fill='black',font=("arial",15))
            can.create_rectangle(0,700,1100,800,fill='white')
            can.create_text(550,750,text=("Oh... Ne vous inquiétez pas, je vous garde ça pour la prochaine fois que vous revenez!"),fill='black',font=("arial",15))
        def quit():
            global f
            boutiqueboutonquit.destroy()
            produitun.destroy()
            produitdeux.destroy()
            produittrois.destroy()
            produitquatre.destroy()
            produitcinq.destroy()
            ban.destroy()
            f = 0
            expression()

        ban=Canvas(fen,width=1100,height=800,background='white')
        ban.grid(rowspan=1, column=0)

        produitun= Button (ban, text= "Bio",background="green",foreground="white",font=("Helvetica",10),command=quit)
        produitun.grid(row=0,column=0)
        produitdeux= Button (ban, text= "Moyen de gamme",background="dark green",foreground="white",font=("Helvetica",10),command=quit)
        produitdeux.grid(row=0,column=2)
        produittrois= Button (ban, text= "Bas de gamme",background="brown",foreground="white",font=("Helvetica",10),command=quit)
        produittrois.grid(row=0,column=4)
        produitquatre= Button (ban, text= "Jouet",background="pink",foreground="black",font=("Helvetica",10),command=quit)
        produitquatre.grid(row=0,column=6)
        produitcinq= Button (ban, text= "Jouet",background="pink",foreground="black",font=("Helvetica",10),command=quit)
        produitcinq.grid(row=0,column=8)
        boutiqueboutonquit= Button (fen, text= "Quitter la boutique",background="black",foreground="white",font=("Helvetica",10),command=quit)
        boutiqueboutonquit.grid(row=6,column=1)

    can.create_rectangle(700,0,775,50,fill='white')
    can.create_text(737.5,10,text=("Argent:"),fill='black',font=("arial",10))
    can.create_text(737.5,40,text=(str(money)+" €"),fill='black',font=("arial",10))

    if f == 0:
        expression()


def maladie():
    global m,malade
    risquemaladie=randint(0,101)
    if risquemaladie >= 0 and risquemaladie <= m:
        malade=1

def temps():
    global jour,jourmax,mois,moisnum,année
    if (moisnum == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12):
        jourmax = 31

    if (moisnum == 4 or mois == 6 or mois == 9 or mois == 11):
        jourmax = 30

    if moisnum == 2:
        jourmax = 28

    if jour > jourmax:
        jour = 1
        moisnum+=1
    if moisnum > 12:
        moisnum = 1
        année+=1


def joursuivant():
    global bonheur,faim,energie,energiemax,jour,jourmax,mois,moisnum,sante,money
    if sante > 0:
        jour= jour+1
        #evenement()
        if jour >= 1:
            salaire()
            faim = faim - 50
            expression()
            temps()
            maladie()
            if malade == 1:
                can.create_rectangle(900,0,1100,50,fill='white')
                can.create_text(1000,25,text=("Votre "+animal+" est malade"),fill='red',font=("arial",10))
                can.create_rectangle(0,700,1100,800,fill='white')
                can.create_text(550,750,text=(nom+" est malade."),fill='black',font=("arial",20))
                faim=faim-20
                energie=energie/2
                bonheur=25
                sante=sante-20
                expression()
            elif malade == 0:
                can.create_rectangle(900,0,1100,50,fill='white')
                can.create_text(1000,25,text=("Votre "+animal+" est en bonne santé"),fill='black',font=("arial",10))
            if faim <= 0:
                faim=0
                sante=sante-10
            energie = energiemax
            bonheur = bonheur - 50
            if bonheur <= 0:
                bonheur=0
            can.create_rectangle(0,0,50,50,fill='white')
            can.create_text(25,10,text=("année:"),fill='black',font=("arial",10))
            can.create_text(25,40,text=(année),fill='black',font=("arial",10))

            can.create_rectangle(0,100,70,150,fill='white')
            can.create_text(35,110,text=("mois:"),fill='black',font=("arial",10))
            can.create_text(35,140,text=(mois[moisnum]),fill='black',font=("arial",10))

            can.create_rectangle(0,200,50,250,fill='white')
            can.create_text(25,210,text=("jour:"),fill='black',font=("arial",10))
            can.create_text(25,240,text=(jour),fill='black',font=("arial",10))

            can.create_rectangle(0,300,60,375,fill='white')
            can.create_text(30,320,text=("Maladie:"),fill='black',font=("arial",10))
            can.create_text(30,350,text=(str(m)+" %"),fill='black',font=("arial",10))

            can.create_rectangle(400,0,475,50,fill='white')
            can.create_text(437.5,10,text=("Faim:"),fill='black',font=("arial",10))
            can.create_text(437.5,40,text=(str(faim)+"/"+str(faimmax)),fill='black',font=("arial",10))

            can.create_rectangle(500,0,575,50,fill='white')
            can.create_text(537.5,10,text=("Bonheur:"),fill='black',font=("arial",10))
            can.create_text(537.5,40,text=(str(bonheur)+"/"+str(bonheurmax)),fill='black',font=("arial",10))

            can.create_rectangle(600,0,675,50,fill='white')
            can.create_text(637.5,10,text=("Energie:"),fill='black',font=("arial",10))
            can.create_text(637.5,40,text=(str(energie)+"/"+str(energiemax)),fill='black',font=("arial",10))

            can.create_rectangle(800,0,875,50,fill='white')
            can.create_text(837.5,10,text=("Santé:"),fill='black',font=("arial",10))
            can.create_text(837.5,40,text=(str(sante)+"/"+str(santemax)),fill='black',font=("arial",10))

            can.create_rectangle(700,0,775,50,fill='white')
            can.create_text(737.5,10,text=("Argent:"),fill='black',font=("arial",10))
            can.create_text(737.5,40,text=(str(money)+" €"),fill='black',font=("arial",10))

            if bonheur==0:
                can.create_rectangle(500,0,575,50,fill='white')
                can.create_text(537.5,10,text=("Bonheur:"),fill='red',font=("arial",10))
                can.create_text(537.5,40,text=(str(bonheur)+"/"+str(bonheurmax)),fill='red',font=("arial",10))

            if faim==0:
                can.create_rectangle(400,0,475,50,fill='white')
                can.create_text(437.5,10,text=("Faim:"),fill='red',font=("arial",10))
                can.create_text(437.5,40,text=(str(faim)+"/"+str(faimmax)),fill='red',font=("arial",10))
    if sante <= 0:
        sante=0
        can.create_rectangle(0,0,1100,800,fill='black')
        can.create_text(550,300,text=(nom+" est MORT."),fill='red',font=("arial",30))
        can.create_text(550,500,text=("GAME OVER"),fill='red',font=("arial",50))

def salaire():
    global jour, money
    if jour % 5 == 0:
        money += 50
        if bonheur/bonheurmax == 1:
            money += 50
        elif bonheur/bonheurmax >= 0.8:
            money += 35
        elif bonheur/bonheurmax >= 0.7:
            money += 25
        elif bonheur/bonheurmax >= 0.6:
            money += 15
        elif bonheur/bonheurmax >= 0.4:
            money += 10
        else:
            money += 5


def expression():
    global bonheur,bonheurmax,sante,img
    if malade==1:
        img=can.create_image(550,400,image=sad)
        can.itemconfig(img, image=sad)
        can.coords(img,550,400)
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" a besoin de se faire soigner!"),fill='red',font=("arial",20))
    elif (bonheur >=0 and bonheur <= 20) :
        img=can.create_image(550,400,image=sad)
        can.itemconfig(img, image=sad)
        can.coords(img,550,400)
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" est triste."),fill='black',font=("arial",20))

    elif bonheur <= 0.75*bonheurmax:
        img=can.create_image(550,400,image=normal)
        can.itemconfig(img, image=normal)
        can.coords(img,550,400)
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" est normal."),fill='black',font=("arial",20))
    else:
        img=can.create_image(550,400,image=normal)
        can.itemconfig(img, image=normal)
        can.coords(img,550,400)
        can.create_rectangle(0,700,1100,800,fill='white')
        can.create_text(550,750,text=(nom+" est Heureux!"),fill='black',font=("arial",20))

if m >= 100:
    m=100

if money <= 0:
    money=0

if bonheur <= 0:
    bonheur=0
    can.create_rectangle(500,0,575,50,fill='white')
    can.create_text(537.5,10,text=("Bonheur:"),fill='red',font=("arial",10))
    can.create_text(537.5,40,text=(str(bonheur)+"/"+str(bonheurmax)),fill='red',font=("arial",10))

if faim <= 0:
    faim=0
    can.create_rectangle(400,0,475,50,fill='white')
    can.create_text(437.5,10,text=("Faim:"),fill='red',font=("arial",10))
    can.create_text(437.5,40,text=(str(faim)+"/"+str(faimmax)),fill='red',font=("arial",10))



nourrirbouton= Button (fen, text= "Nourrir",background="Brown",foreground="white",font=("Helvetica",10),command=nourrir)
nourrirbouton.grid(row=0,column=1)

jouerbouton= Button (fen, text= "Jouer",background="blue",foreground="white",font=("Helvetica",10),command=jouer)
jouerbouton.grid(row=1,column=1)

soignerbouton= Button (fen, text= "Soigner",background="light green",foreground="black",font=("Helvetica",10),command=soigner)
soignerbouton.grid(row=2,column=1)

veterinairebouton= Button (fen, text= "Vétérinaire ",background="green",foreground="white",font=("Helvetica",10),command=veterinaire)
veterinairebouton.grid(row=3,column=1)

boutiquebouton= Button (fen, text= "Boutique",background="red",foreground="white",font=("Helvetica",10),command=boutique)
boutiquebouton.grid(row=5,column=1)

godemain= Button (fen, text= "Aller à demain ",background="white",foreground="black",font=("Helvetica",10),command=joursuivant)
godemain.grid(row=7,column=1)

quitter= Button (fen, text= "Quitter le jeu",background="white",foreground="black",font=("Helvetica",10),command=fen.destroy)
quitter.grid(row=8,column=1)

def clavier(evt):
    if evt.keysym == '1' or evt.keysym == '&':
        nourrir()

    if evt.keysym == '2' or evt.keysym == 'é':
        jouer()

    if evt.keysym == '3' or evt.keysym == '"':
        soigner()

    if evt.keysym == '4':
        veterinaire()

    if evt.keysym == '5' or evt.keysym == '(':
        boutique()

    if evt.keysym == 't' or evt.keysym == 'T':
        joursuivant()

fen.bind_all('<Key>',clavier)

fen.mainloop()
