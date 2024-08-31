##############################################################################################################################################################
##############################################################################################################################################################
######################################   GUI PART    #########################################################################################################
##############################################################################################################################################################
##############################################################################################################################################################
import tkinter
import tkinter.messagebox

import customtkinter

import pyperclip

import time




customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"




class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=270,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============
        #Label Password input
        self.label = customtkinter.CTkLabel(master=self.frame_left,
                                            text="Password input",
                                            width=500,
                                            height=30,
                                            font=("Roboto", 24))
        self.label.place(relx=0.5, rely=0.1, anchor=tkinter.N)

        #Input Nome sito/app
        self.input1 = customtkinter.CTkEntry(master=self.frame_left,
                                             placeholder_text="Site / App",
                                             width=250,
                                             height=40,
                                             border_width=2,
                                             corner_radius=10)
        self.input1.place(relx=0.5, rely=0.25, anchor=tkinter.N) # 1

        #Input Nome utente (se presente)
        self.input2 = customtkinter.CTkEntry(master=self.frame_left,
                                             placeholder_text="Username / Email",
                                             width=250,
                                             height=40,
                                             border_width=2,
                                             corner_radius=10)
        self.input2.place(relx=0.5, rely=0.45, anchor=tkinter.N) # 3

        #Input Mai rubato l'account?
        self.input3 = customtkinter.CTkEntry(master=self.frame_left,
                                             placeholder_text="Have stolen",
                                             width=250,
                                             height=40,border_width=2,
                                             corner_radius=10)
        self.input3.place(relx=0.5, rely=0.65, anchor=tkinter.N) # 5

        #Input Password
        self.input4 = customtkinter.CTkEntry(master=self.frame_left,
                                             placeholder_text="Password",
                                             width=250,
                                             height=40,

                                             border_width=2,
                                             corner_radius=10)
        self.input4.place(relx=0.5, rely=0.85, anchor=tkinter.N) # 7
        
        # ============ frame_right ============

        #Button Generate
        self.pw=""
        self.button1 = customtkinter.CTkButton(master=self.frame_right,
                                               width=180,
                                               height=50,
                                               border_width=0,
                                               corner_radius=8,
                                               font=("Robot", 17),
                                               text="Generate",
                                               command=self.button_event) #evento dopo aver cliccato il bottone
                                            
        self.button1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #Label with password (initially invisible)
        self.pw_label = customtkinter.CTkLabel(master=self.frame_right,
                                               width=180,
                                               height=50,
                                               font=("Roboto", 21),
                                               text= " "
                                               )
        self.pw_label.place(relx=0.5, rely=0.80, anchor=tkinter.CENTER)

    
    #functions:
    #if "Generate" button is pressed
    def button_event(self):
        self.pw = program()
        self.pw_label.configure(text=program())

        #Button Copy (initially invisible)
        self.copy_button = customtkinter.CTkButton(master=self.frame_right,
                                                   width=50,
                                                   height=30,
                                                   font=("Robot", 14),
                                                   text="Copy",
                                                   command=self.button_event2)
        self.copy_button.place(relx=0.50, rely=0.90, anchor=tkinter.CENTER)

        
        

    #if "Copy" button is pressed
    def button_event2(self):
        self.copy_button.configure(text_color="Black")
        self.pw
        pyperclip.copy(self.pw)
        
##############################################################################################################################################################
##############################################################################################################################################################










##############################################################################################################################################################
##############################################################################################################################################################
###################################### PASSWORD PART #########################################################################################################
##############################################################################################################################################################
##############################################################################################################################################################
#librerie
from hashlib import sha256, md5
import random

from os import system, name

import pyperclip



def loop(parola):
    i=0
    parola_loop = ""

    for char in parola:
            i+=1

    i=(32/i)+1
    i=int(i)
    for _ in range(i):
            parola_loop+=parola

    return parola_loop

def randomPerc(perc1, perc2, ns_, p1_, p2_, p3_, seed1):
    random.seed(seed1)
    number = random.uniform(perc1,perc2)

    return number

def charCounter(password_, charList):

    total = 0
    i = 0
    for i in range(32):
        
        if password_[i] in charList:
            total +=1 
    
    return total

def changeChar(totM, totUc, totSc, totNb, totLc, perc, seed1, listM ,listUc, listSc, listNb, listLc, password_, tup):
    while totM < perc - 2 or totM > perc + 2:
        position = random.uniform(0,31)
        position = int(position)

        if totM < perc - 2:
            if password_[position] not in listM:
                if password_[position] in listUc:
                    totLc-=1
                elif password_[position] in listSc:
                    totSc-=1
                elif password_[position] in listNb:
                    totNb-=1
                else:
                    totLc-=1
            password_[position] = random.choice(listM)
            totM+=1
        if totM > perc + 2:
            if password_[position] in listM:
                password_[position] = random.choice(listLc)
                totM-=1
                totLc+=1

    if listM == listUc:
        totUc = totM
    elif listM == listSc:
        totSc = totM
    elif listM == listNb:
        totNb = totM
    else:
        totLc = totM

    tup = (password_, totUc, totSc, totNb, totLc)

    return tup

def clear():

    #windows
    if name == 'nt':
        _ = system('cls')

    #mac/linux
    else:
        _ = system('clear')

def program():
    #input base
    ns = app.input1.get()
    p1 = app.input2.get()
    p2 = app.input3.get()
    p3 = app.input4.get()
    clear()

    listUc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K" , "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y","Z"] #uc = upper case
    listLc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k" , "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"] #lc = lower case
    listNb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    listSc = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "}", "|", "~"]



    #1A PARTE (lavoro sugli input base in maniera basilare):
    #Encodo gli input di base in sha256
    ns_ = sha256(ns.encode('utf-8')).hexdigest()
    p1_ = sha256(p1.encode('utf-8')).hexdigest()
    p2_ = sha256(p2.encode('utf-8')).hexdigest()
    p3_ = sha256(p3.encode('utf-8')).hexdigest()
    seed = ""

    #Metto in loop gli input di base
    ns_loop = ""
    ns_loop = loop(ns)
    p1_loop = ""
    p1_loop = loop(p1)
    p2_loop = ""
    p2_loop = loop(p2)
    p3_loop = ""
    p3_loop = loop(p3)



    #2A PARTE (faccio una prima password):
    #Creo un seed usando le parole encodate in sha256 unendole carattere per carattere
    for i in range(63): #63 e non 64 perchè ho il cazzo lungo

        seed += ns_[i]
        seed += p1_[i]
        seed += p2_[i]
        seed += p3_[i]

    #Tramite il seed creo una password
    password = md5(seed.encode('utf-8')).hexdigest()                                    
    password_ = list(password) #rendo la password una lista divisa per caratteri



    #3A PARTE (setuppo la 4A parte facendo tutti i calcoli matematici del caso):
    #Creo dei numeri randomici tra due limiti per ogni tipologia di caratteri
    percUc = int(randomPerc(22, 28, ns_, p1_, p2_, p3_, seed))
    percSc = int(randomPerc(28, 33, ns_, p1_, p2_, p3_, seed))
    percNb = int(randomPerc(18, 23, ns_, p1_, p2_, p3_, seed))
    percLc = ((100 - percUc) - percSc) - percNb

    #Creo la percenutale effettiva
    percUc = (32*percUc) / 100
    percSc = (32*percSc) / 100
    percNb = (32*percNb) / 100
    percLc = (32*percLc) / 100

    #Conto a quanto ammontano ogni tipologia di carattere nella password
    totUc = charCounter(password_, listUc)
    totSc = charCounter(password_, listSc)
    totNc = charCounter(password_, listNb)
    totLc = charCounter(password_, listLc)



    #4A PARTE (creo la password definitiva mettendo caratteri speciali e maiuscole):
    check = 0
    tup = (password_, totUc, totSc, totNc, totLc)
    while check == 0:
        
        if totUc < percUc - 2 or totUc > percUc + 2:
            check = 0
            tup = changeChar(totUc, totUc, totSc, totNc, totLc, percUc, seed, listUc, listUc, listSc, listNb, listLc, password_, tup)   
            password_ = tup[0]
            totUc = tup[1]
            totSc = tup[2]
            totNc = tup[3]
            totLc = tup[4]
        else:
            check = 1

        if totSc < percSc - 2 or totSc > percSc + 2:
            check = 0
            tup = changeChar(totSc, totUc, totSc, totNc, totLc, percSc, seed, listSc, listUc, listSc, listNb, listLc, password_, tup)
            password_ = tup[0]
            totUc = tup[1]
            totSc = tup[2]
            totNc = tup[3]
            totLc = tup[4]

        if totNc < percNb - 2 or totNc > percNb + 2:
            check = 0
            tup =  changeChar(totNc, totUc, totSc, totNc, totLc, percNb, seed, listNb, listUc, listSc, listNb, listLc, password_, tup)
            password_ = tup[0]
            totUc = tup[1]
            totSc = tup[2]
            totNc = tup[3]
            totLc = tup[4]

        if totLc < percLc - 2 or totLc > percLc + 2:
            check = 0
            tup = changeChar(totLc, totUc, totSc, totNc, totLc, percLc, seed, listLc, listUc, listSc, listNb, listLc, password_, tup)
            password_ = tup[0]
            totUc = tup[1]
            totSc = tup[2]
            totNc = tup[3]
            totLc = tup[4]
        
    password = "".join(password_)

    return password
##############################################################################################################################################################
##############################################################################################################################################################









##############################################################################################################################################################
##############################################################################################################################################################
######################################      MAIN      ########################################################################################################
##############################################################################################################################################################
##############################################################################################################################################################

if __name__ == "__main__":
    app = App()
    app.minsize( width = 500,
                 height = 350
    )
    app.mainloop()
##############################################################################################################################################################
##############################################################################################################################################################
