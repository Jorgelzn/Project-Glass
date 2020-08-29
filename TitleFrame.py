from Frame import *
from Escenarios import portal

class titleFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/title.jpg","music/wind spirit.mp3",0)
        print("TITLE")
        portal(self.parent)

        self.playButton=Button(self.myFrame,text="Explore",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggle(Zones[1]))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)

        self.restartButton=Button(self.myFrame,text="New Adventure",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:[self.toggle(Zones[1]),self.newAdventure()])
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

        mixer.music.load(self.song)
        mixer.music.play()

    def newAdventure(self):
        for i in range(1,len(Zones)):
            Zones[i].reset()
        self.playButton["command"]=lambda:Zones[0].toggle(Zones[1])

    def creditsToggle(self):
        self.creditsText.place(rely=0.1,relx=0.3,relwidth=0.4,relheight=0.7)
        self.titleButton.place(rely=0.7,relx=0.3,relwidth=0.4,relheight=0.1)
        self.playButton.place_forget()
        self.restartButton.place_forget()
        self.creditsButton.place_forget()

    def backFromCredits(self):
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)
        self.restartButton.place(rely=0.85,relx=0.4,relwidth=0.2,relheight=0.1)
        self.creditsButton.place(rely=0.90,relx=0.05,relwidth=0.1,relheight=0.05)
        self.creditsText.place_forget()
        self.titleButton.place_forget()

