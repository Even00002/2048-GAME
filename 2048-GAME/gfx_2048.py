from tkinter import *
from backend_2048 import *




# creation de la fenêtre
window = Tk()
window.geometry("425x425")
window.title('2048 GAME')
window.configure(bg='#CDB79E')
# Titre
Label(bg='#FFEFDB',text="2048 GAME",width=25, height=3, font=("Arial", 22)).grid(row=0,column=0,columnspan=4,padx=0,pady=0)

#creation et position du Label
for line in range(len(cases)):
    for col in range(len(cases[line])):
        # creation sans position
        labels[line] = Label (window, text =cases[line][col], width=10, height=5, borderwidth=1, relief="solid", font=("Arial", 10), bg="#FFFFFF")
        # position du Label dans la fenêtre
        labels[line].grid (row=line+1,column=col,padx=dx,pady=dy)

window.mainloop()
