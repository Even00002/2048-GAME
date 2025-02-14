from idlelib.config_key import MOVE_KEYS
from tkinter import CallWrapper
from tkinter.messagebox import showinfo

nmoves=0000
# tableau des labels
cases= [
        [" "," "," "," "],
        [" "," "," "," "],
        [" "," "," "," "],
        [" "," "," "," "],
]

# tableau des valeurs
game= [ [2,2,4,0],
        [0,0,0,0],
        [2,4,4,0],
        [0,0,0,0]
]

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




labels=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

dx=10 # distance horizontal entre les labels
dy=10# distance vertical entre les labels

def QUITTER():
        exit()

def scoreinfo():
        showinfo(title="info score", message="Votre Score est de " + str(nmoves))

def pack3(a,b,c):
        nmove=0
        if b==0 and c!=0:
                b=c
                c=0
                nmove+=1
        if a==0 and b!=0:
                a=b
                b=c
                c=0
                nmove+=1
        if b==c and b!=0:
                b=2*b
                c=0
                nmove+=1
        return [a,b,c,nmove]

def pack4(a,b,c,d):
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

