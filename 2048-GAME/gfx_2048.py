from tkinter import *
from tkinter import LabelFrame
import tkinter as tk
from backend_2048 import *

#affectation des touches aux fonctions, q pour quitter, le reste pour "tasser" dans une certaine direction
def key_pressed(event) :
    touche=event.keysym #récupérer le symbole de la touche
    if (touche=="Down" or touche=="s" or touche=="S"):
        move_down()
        display()
    if (touche == "Up" or touche == "w" or touche == "W"):
        move_up()
        display()
    if (touche == "Left" or touche == "a" or touche == "A"):
        move_left()
        display()
    if (touche == "Right" or touche == "d" or touche == "D"):
        move_right()
        display()

def display():
    for line in range(len(cases)):
        for col in range(len(cases[line])):
            # creation sans position
            labels[line][col].config( text=game[line][col], bg=colors[game[line][col]])
            # position du Label dans la fenêtre

# creation de la fenêtre
window = Tk()
window.geometry("445x550")
window.title('2048 GAME')
window.configure(bg='#CDB79E')
# Titre
Label(bg='#FFEFDB',text="2048 GAME",width=26, height=3, font=("Arial", 22)).grid(row=0,column=0,columnspan=4,padx=0,pady=0)
Frm_bouton=Frame(window, bg='#FFEFDB',width=448, height=60).grid(row=1, column=0,columnspan=4,padx=0,pady=0)
Btn_Nouveau=Button(Frm_bouton, text="Nouveau", bg='#CDB79E').grid(row=1, column=0, padx=0, pady=15)
Btn_quitter=Button(Frm_bouton, text="Quitter", bg='#CDB79E', command=QUITTER).grid(row=1, column=1, padx=0, pady=15)
Btn_score=Button(Frm_bouton, text="score: " + str(nmoves), bg='#CDB79E', command=scoreinfo).grid(row=1, column=2, padx=0, pady=15)
#creation et position du Label
for line in range(len(cases)):
    for col in range(len(cases[line])):
        # creation sans position
        labels[line][col] = Label (window, width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 16))
        # position du Label dans la fenêtre
        labels[line][col].grid (row=line+3,column=col,padx=dx,pady=dy)

display()
window.bind('<Key>', key_pressed) #on traite les touches clavier
window.mainloop()


# , font=("Arial", 22)
# #FFEFDB