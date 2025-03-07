#Auteur: Even
#Date:31, janvier
#projet: 2048_GAME
#version:1.0

from idlelib.config_key import MOVE_KEYS
from tkinter import CallWrapper
from tkinter.messagebox import showinfo
import random

nmove=0
nmoves=0000
# tableau des labels
cases= [
        [" "," "," "," "],
        [" "," "," "," "],
        [" "," "," "," "],
        [" "," "," "," "],
]

# tableau des valeurs
game = [ [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
]

#couleurs
colors={
        0:"#FFFFFF",
        2:"#F0F0EB",
        4:"#FFF2CC",
        8:"#FFB366",
        16:"#FF8000",
        32:"#FF6666",
        64:"#FF0000",
        128:"#FFFF66",
        256:"#FFFF33",
        512:"#CCFF99",
        1024:"#B3FF66",
        2048:"#33FF3A",
        4096:"#99FFCC",
        8192:"#66B2FF",
}

#couleurs des lettres
lettrecouleur={
        0:"white",
        2:"black",
        4:"black",
        8:"black",
        16:"black",
        32:"black",
        64:"black",
        128:"black",
        256:"black",
        512:"black",
        1024:"black",
        2048:"black",
        4096:"black",
        8192:"black",
}


labels=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

dx=10 # distance horizontal entre les labels
dy=10# distance vertical entre les labels

#fonction du bouton quitter
def QUITTER():
        exit()

#permet de consulter des information sur le score
def scoreinfo():
        global nmoves
        print(nmoves)
        showinfo(title="info score", message="Votre Score est de " + str(nmoves*10))

#permet aux tuiles d'être en mouvement
def pack4(a,b,c,d):
        #retire les zéro
        nmove=0
        if c==0 and d!=0:
                c=d
                d=0
                nmove+=1
        if b==0 and c!=0:
                b=c
                c=d
                d=0
                nmove+=1
        if a == 0 and b != 0:
                a = b
                b = c
                c = d
                d = 0
                nmove += 1
        #fusione les tuiles
        if a == b and a != 0:
                a = 2 * a
                b = c
                c = d
                d = 0
                nmove += 1
        if b==c and b!=0:
                b=2*b
                c=d
                d=0
                nmove+=1
        if c==d and c!=0:
                c=2*c
                d=0
                nmove+=1
        return [a,b,c,d,nmove]

def move_down():
        [game[3][0],game[2][0],game[1][0],game[0][0],nmove]=pack4(game[3][0],game[2][0],game[1][0],game[0][0])
        [game[3][1],game[2][1],game[1][1],game[0][1],nmove]=pack4(game[3][1],game[2][1],game[1][1],game[0][1])
        [game[3][2],game[2][2],game[1][2],game[0][2],nmove]=pack4(game[3][2],game[2][2],game[1][2],game[0][2])
        [game[3][3],game[2][3],game[1][3],game[0][3],nmove]=pack4(game[3][3],game[2][3],game[1][3],game[0][3])

def move_up():
        [game[0][0],game[1][0],game[2][0],game[3][0],nmove]=pack4(game[0][0],game[1][0],game[2][0],game[3][0])
        [game[0][1],game[1][1],game[2][1],game[3][1],nmove]=pack4(game[0][1],game[1][1],game[2][1],game[3][1])
        [game[0][2],game[1][2],game[2][2],game[3][2],nmove]=pack4(game[0][2],game[1][2],game[2][2],game[3][2])
        [game[0][3],game[1][3],game[2][3],game[3][3],nmove]=pack4(game[0][3],game[1][3],game[2][3],game[3][3])

def move_left():
        [game[0][0],game[0][1],game[0][2],game[0][3],nmove]=pack4(game[0][0],game[0][1],game[0][2],game[0][3])
        [game[1][0],game[1][1],game[1][2],game[1][3],nmove]=pack4(game[1][0],game[1][1],game[1][2],game[1][3])
        [game[2][0],game[2][1],game[2][2],game[2][3],nmove]=pack4(game[2][0],game[2][1],game[2][2],game[2][3])
        [game[3][0],game[3][1],game[3][2],game[3][3],nmove]=pack4(game[3][0],game[3][1],game[3][2],game[3][3])

def move_right():
        [game[0][3],game[0][2],game[0][1],game[0][0],nmove]=pack4(game[0][3],game[0][2],game[0][1],game[0][0])
        [game[1][3],game[1][2],game[1][1],game[1][0],nmove]=pack4(game[1][3],game[1][2],game[1][1],game[1][0])
        [game[2][3],game[2][2],game[2][1],game[2][0],nmove]=pack4(game[2][3],game[2][2],game[2][1],game[2][0])
        [game[3][3],game[3][2],game[3][1],game[3][0],nmove]=pack4(game[3][3],game[3][2],game[3][1],game[3][0])

# faire apparaitre un 2 ou 4 sur une case vide
def tuiles_apparition(game):
        # trouver une case vide (aléatoire)
        case_vide=[]
        for li in range (4):
                for col in range (4):
                        if game[li][col]==0:
                                case_vide.append([li,col])
        [li,col]=random.choice(case_vide)
        # décider si 2 ou 4 (80%-20%)
        number = random.choice([2,2,2,2,4])
        # poser le résultat sur case vide
        game[li][col]=number
        print (game, li, col, number, case_vide)

def NOUVEAU():
    global game
    game = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
    print(game)
    tuiles_apparition(game)
    tuiles_apparition(game)
    print(game)
    display()

def display():
    global game
    for line in range(len(cases)):
        for col in range(len(cases[line])):
            #creation sans position et colorie les zéro en blanc
            labels[line][col].config( text=game[line][col], bg=colors[game[line][col]], fg=lettrecouleur[game[line][col]])