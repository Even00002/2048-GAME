#Auteur: Even
#Date:31, janvier
#projet: 2048_GAME
#version:1.0

from tkinter import *
from tkinter import LabelFrame
import tkinter as tk
from backend_2048 import *


def start():
    global game
    tuiles_apparition(game)
    tuiles_apparition(game)
    display()

#affectation des touches aux fonctions, q pour quitter, le reste pour "tasser" dans une certaine direction
def key_pressed(event) :
    global nmoves, nmove, avant

    touche=event.keysym #récupérer le symbole de la touche
    if (touche=="Down" or touche=="s" or touche=="S"):
        move_down()
        #je garde les coordonées des cases vides dans apres
        apres = []
        for li in range(4):
            for col in range(4):
                if game[li][col] == 0:
                    apres.append([li, col])
        #je compare les coordonées de apres avec ce de avant si il sont pareille rien ne se passe mais si ils sont différents j'utilise la fonction tuiles_apparition()
        if apres == avant:
            print("true")
        elif apres != avant:
            print("false")
            tuiles_apparition(game)
            nmove = nmove + 1
        display()
    if (touche == "Up" or touche == "w" or touche == "W"):
        move_up()
        apres = []
        for li in range(4):
            for col in range(4):
                if game[li][col] == 0:
                    apres.append([li, col])
        if apres == avant:
            print("true")
        elif apres != avant:
            print("false")
            tuiles_apparition(game)
            nmove = nmove + 1
        display()
    if (touche == "Left" or touche == "a" or touche == "A"):
        move_left()
        apres = []
        for li in range(4):
            for col in range(4):
                if game[li][col] == 0:
                    apres.append([li, col])
        if apres == avant:
            print("true")
        elif apres != avant:
            print("false")
            tuiles_apparition(game)
            nmove = nmove + 1
        display()
    if (touche == "Right" or touche == "d" or touche == "D"):
        move_right()
        apres = []
        for li in range(4):
            for col in range(4):
                if game[li][col] == 0:
                    apres.append([li, col])
        if apres == avant:
            print("true")
        elif apres != avant:
            print("false")
            tuiles_apparition(game)
            nmove = nmove + 1
        display()

    nmoves=nmoves+1
    print("nombre de mouvement = " + str(nmoves))
    Btn_score.config(text="score: " + str(nmoves*10))
    avant = []
    for li in range(4):
        for col in range(4):
            if game[li][col] == 0:
                avant.append([li, col])

# creation de la fenêtre
window = Tk()
window.geometry("445x550")
window.title('2048 GAME')
window.configure(bg='#CDB79E')
#Titre
Label(bg='#FFEFDB',text="2048 GAME",width=26, height=3, font=("Arial", 22,)).grid(row=0,column=0,columnspan=4,padx=0,pady=0)
Frm_bouton=Frame(window, bg='#FFEFDB',width=448, height=60).grid(row=1, column=0,columnspan=4,padx=0,pady=0)
#bouton
Btn_Nouveau=Button(Frm_bouton, text="Nouveau", bg='#CDB79E', command="NOUVEAU").grid(row=1, column=0, padx=0, pady=15)
Btn_quitter=Button(Frm_bouton, text="Quitter", bg='#CDB79E', command=QUITTER).grid(row=1, column=1, padx=0, pady=15)
Btn_score=Button(Frm_bouton, text="score: " + str(nmoves*10), bg='#CDB79E', command=scoreinfo)
Btn_score.grid(row=1, column=2, padx=0, pady=15)
#creation et position du Label
for line in range(len(cases)):
    for col in range(len(cases[line])):
        # creation sans position
        labels[line][col] = Label (window, width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 16))
        # position du Label dans la fenêtre
        labels[line][col].grid (row=line+3,column=col,padx=dx,pady=dy)
start()
avant = []
for li in range(4):
    for col in range(4):
        if game[li][col] == 0:
            avant.append([li, col])


display()
window.bind('<Key>', key_pressed) #on traite les touches clavier
window.mainloop()


# , font=("Arial", 22)
# #FFEFDB