from Frame import *
from Escenarios import portal

class titleFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/landscapes/title.jpg","music/wind spirit.mp3",0,"title")
        print("TITLE")

        #global InventoryImages
        InventoryImages.append(ImageTk.PhotoImage(Image.open("images/objects/question.png").resize((70,114)))) 
        InventoryImages.append(ImageTk.PhotoImage(Image.open("images/objects/map.jpg").resize((150,150))))
        InventoryImages.append(ImageTk.PhotoImage(Image.open("images/objects/coin.png").resize((150,150))))
        InventoryImages.append(ImageTk.PhotoImage(Image.open("images/objects/rune.png").resize((250,200))))
        InventoryImages.append(ImageTk.PhotoImage(Image.open("images/objects/amulet.jpg").resize((150,150))))
        InventoryImages.append(ImageTk.PhotoImage(Image.open("images/objects/ring.jpg").resize((150,150))))
        
        portal(self.parent)                             #create portal frame in order to be accessible by the explore and new game buttons in Zone[1]


        #DISPLAY BUTTONS
        self.playButton=Button(self.myFrame,text="Play",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggle(Zones[1],True))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)

        self.restartButton=Button(self.myFrame,text="New Adventure",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:[self.newAdventure(),self.toggle(Zones[1],True)])
        self.restartButton.place(rely=0.85,relx=0.4,relwidth=0.2,relheight=0.1)

        self.creditsButton=Button(self.myFrame,text="Credits",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.creditsToggle())
        self.creditsButton.place(rely=0.90,relx=0.05,relwidth=0.1,relheight=0.05)


        self.creditsText=Label(self.myFrame,text="""Programmer and Designer:
Jorge Lizcano

Images:
Chris Cold
Luka Mivsek
Hira Bilal
Matt Sanz
Brendon Paes

Music:
BrunuhVille
Two Steps From Hell""",fg="#4FC6B2",bg="#325062")

        self.titleButton = Button(self.myFrame,text="Back",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15))
        self.titleButton["command"]=lambda:self.backFromCredits()

        mixer.music.load(self.song)                 #load title frame music
        mixer.music.play(-1)


    def newAdventure(self):                         #method used to start the game from the beginning
        Zones.clear()                               #delete all the frames from the Zones array
        InventoryImages.clear()                     #delete all images from inventory images array
        Zones.append(titleFrame(self.parent))       #create the titleframe object and add it to the array of Zones so the game would start as it was a new game
        Zones.pop()                                 #there is a bug that adds an extra frame to the Zones array so we pop it


    def creditsToggle(self):                                                        #method to display the credits box
        self.creditsText.place(rely=0.1,relx=0.3,relwidth=0.4,relheight=0.7)
        self.titleButton.place(rely=0.7,relx=0.3,relwidth=0.4,relheight=0.1)
        self.playButton.place_forget()
        self.restartButton.place_forget()
        self.creditsButton.place_forget()

    def backFromCredits(self):                                                      #method to hide the credits box
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)
        self.restartButton.place(rely=0.85,relx=0.4,relwidth=0.2,relheight=0.1)
        self.creditsButton.place(rely=0.90,relx=0.05,relwidth=0.1,relheight=0.05)
        self.creditsText.place_forget()
        self.titleButton.place_forget()

