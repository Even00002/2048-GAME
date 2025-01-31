from tkinter import *
from backend_2048 import *




# creation de la fenêtre
window = Tk()
window.geometry("500x600")
window.title('2048 GAME')

# Titre
Label(text="2048 GAME",width=25, height=3, font=("Arial", 10)).grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#creation et position du Label
for line in range(len(cases)):
    for col in range(len(cases[line])):
        # creation sans position
        labels[line][col] = Label (window, text =cases[line][col], width=15, height=3, borderwidth=1, relief="solid", font=("Arial", 10), bg="#FFFFFF")
        # position du Label dans la fenêtre
        labels[line][col].grid (row=line+1,column=col,padx=dx,pady=dy)

window.mainloop()
