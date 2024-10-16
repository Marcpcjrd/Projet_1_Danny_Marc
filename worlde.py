from tkinter import *
from tkinter import font
from random import * 
import tkinter.ttk as ttk

fenetre = Tk()
fenetre.title("Worlde")
fenetre.geometry("800x900")


mots = [
    "table", "chien", "fleur", "banjo", "globe",
    "avion", "lampe", "route", "laser", "frise",
    "image", "pomme", "livre", "plage", "piano", 
    "canon", "gazon", "froid", "chaud", "danse",
    "fumer", "vague", "jeune", "ombre", "coupe",
    "plomb", "neige", "sable", "balle", "conte",
    "champ", "boule", "angle", "coeur", "aider",
    "crime", "bruit", "faute", "paire", "femme",
    "fruit", "temps", "lueur", "peine", "singe",
    "tapis", "vieux", "blond", "hiver", "point",
    "paris", "larme", "crier", "genre", "cause",
    "doute", "rouge", "maire", "cadre", "parle", 
    "clair", "monde", "poire" 
    ]


label_font = font.Font(size=50)

button_font = font.Font(size=25)

titre = Label(fenetre,font=label_font, text="Worlde")
titre.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

grille = Frame(fenetre)
grille.grid(row=1, column=0, columnspan=5, padx=100, pady=50)




cases = []
for i in range(25):
    cases.append(Label(grille, text=" ",width=3, height=1, font=label_font, borderwidth=1, relief="solid"))

def affiche_cases(i,j):
    l=0
    for k in range(i, j):
        cases[k].grid(row=i, column=l, padx=0, pady=0)
        l +=1

affiche_cases(0,5)
affiche_cases(5,10)
affiche_cases(10,15)
affiche_cases(15,20)
affiche_cases(20,25)


clavier = Frame(fenetre)
clavier.grid(row=7, column=0, columnspan=5, padx=5, pady=5)

alphabet=["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Y", "X", "C", "V", "B", "N", "M"]
lettres=[]
for n in range(26):
    lettres.append(Button(clavier, text=alphabet[n], width=2, height=1, font=button_font, command=lambda n=alphabet[n]:recuptxt(n)))
 
def affiche_lettres(i,j):
    l=0
    for k in range(i, j):
        lettres[k].grid(row=i, column=l, padx=2, pady=2)
        l +=1

affiche_lettres(0,10)
affiche_lettres(10,19)
affiche_lettres(19,26)


    
indice = 0
indice_mot = randint(0, len(mots)-1)
def recuptxt(text):
    lettre = text
    global indice, indice_mot
    if cases[indice].cget("text") == " ":
        cases[indice].config(text=lettre)
        indice +=1
    
    print(indice_mot)

    verif(indice_mot)
    
    for i in range(len(mots)):
        if cases[0].cget("text").lower() == mots[i][0] and cases[1].cget("text").lower() == mots[i][1] and cases[2].cget("text").lower() == mots[i][2] and cases[3].cget("text").lower() == mots[i][3] and cases[4].cget("text").lower() == mots[i][4]:
            if i == indice_mot:
                win()
            
        elif cases[5].cget("text").lower() == mots[i][0] and cases[6].cget("text").lower() == mots[i][1] and cases[7].cget("text").lower() == mots[i][2] and cases[8].cget("text").lower() == mots[i][3] and cases[9].cget("text").lower() == mots[i][4]:
            if i == indice_mot:
                win()
                
        elif cases[0].cget("text").lower() == mots[i][0] and cases[11].cget("text").lower() == mots[i][1] and cases[12].cget("text").lower() == mots[i][2] and cases[13].cget("text").lower() == mots[i][3] and cases[14].cget("text").lower() == mots[i][4]:
            if i == indice_mot:
                win()
                
        elif cases[0].cget("text").lower() == mots[i][0] and cases[16].cget("text").lower() == mots[i][1] and cases[17].cget("text").lower() == mots[i][2] and cases[18].cget("text").lower() == mots[i][3] and cases[19].cget("text").lower() == mots[i][4]:
            if i == indice_mot:
                win()
                
        elif cases[0].cget("text").lower() == mots[i][0] and cases[21].cget("text").lower() == mots[i][1] and cases[22].cget("text").lower() == mots[i][2] and cases[23].cget("text").lower() == mots[i][3] and cases[24].cget("text").lower() == mots[i][4]:
            if i == indice_mot:
                win()
        
    if indice == 25:
        lose()


n = 0
i = 0
def verif(indice):  
    print(mots[indice])
    global n, i

    if mots[indice][i%5] == cases[n].cget("text").lower(): 
        if i == n:        
            cases[n].config(bg="green")
            n += 1
            i += 1

    else:
        for j in range(5):
            if mots[indice][j] == cases[n].cget("text").lower():
                if j != n:
                    cases[n].config(bg="orange")                  
        i += 1
        n += 1
    print(n, i)


def win():
    win = ttk.Label(fenetre,font=("Arial", 50), text=f"Bravo !, le mot était {mots[indice_mot]}")
    win.grid(row=5, column=0, columnspan=5, padx=5, pady=5)
    
def lose():
    lose = Label(fenetre,font=label_font, text="Perdu !")
    lose.grid(row=5, column=0, columnspan=5, padx=5, pady=5)
        


fenetre.mainloop()
