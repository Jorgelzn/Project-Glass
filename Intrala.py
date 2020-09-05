from MainFrame import *

class intralaFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/intrala.jpg",["texts/intrala.txt","texts/intralatesting1.txt","texts/intralatesting2.txt","texts/intralatesting3.txt"]
        ,"music/aguas estancadas.mp3",prevDiaryEntry+"""-Esta isla parece totalmente deshabitada a primera vista\n""",4,"intrala1",
        [[["inspeccionar la arena","ir a la ciudad","quedarse en la playa","Observar el mar"]],
        [["Observar el mar","Ir a la ciudad","mirar el cielo","Andar"]]],
        [[5],[2]])

        self.changeObject(InventoryImages[1],ObjectsDesc[1])   #put map
        self.imgNPC1=ImageTk.PhotoImage(Image.open("images/intralanpc1.jpg").resize((1000,int(0.7*800)), Image.ANTIALIAS))   #image of the frame
        self.labelNPC1 = Label(self.graphicFrame,image=self.imgNPC1,bg="#325062",borderwidth=5,relief="ridge") 
    def chooseNext(self):
        if self.countDialogue==0:                                                       #introduction dialogue
            selector=self.optionChooser(self.optionChecked[self.countDecisions])
            if selector[0]==1:
                self.changeObject(InventoryImages[2],ObjectsDesc[2])                    #add coind to inventory
                self.dialogueChanger(2)                                                 #go to dialogue 2
            elif selector[1]==1:
                self.dialogueChanger(1)                                                 #go to dialogue 1
            elif selector[2]==1:
                self.labelNPC1.place(rely=0,relx=0,relwidth=1,relheight=1)              #display npc
                self.dialogueChanger(3,1)                                               #go to dialogue 3
            elif selector[3]==1:
                self.dialogueChanger(0)                                                 #go to dialogue 0

        elif self.countDialogue==1:                                                     #dialogue for changing zone
            if self.loader:                                 
                intralaCity(self.parent,self.diaryNotes)                                #create intralaCity object just once
                self.loader=False

            self.nextF=6
            Zones[0].playButton["command"]=lambda:Zones[0].toggle(Zones[self.nextF],True)       #if we go to title from next frame, if we touch play button we come back to that frame
            self.copyingObjects(Zones[self.nextF])                                              #copy objects to next zone
            self.dialogueChanger(0,0)                                                           #reset the dialogue of the actual zone
            self.toggle(Zones[self.nextF])                                                      #change to the next zone

        elif self.countDialogue==2:                                                             #transition dialogue
            self.dialogueChanger(0)                                                             #cuando acaba dialogo 2 ir a dialogo 0

        elif self.countDialogue==3:                                                     #second decision dialogue
            selector=self.optionChooser(self.optionChecked[self.countDecisions])
            self.labelNPC1.place_forget()                                                        #hide npc
            if selector[1]==1:                                                                  
                self.dialogueChanger(1)                                                          #go to city dialogue
            else:
                self.dialogueChanger(0)                                                          #go to dialogue 0
        
        
class intralaCity(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/intralaCity.jpg",["texts/intralaCity.txt"]
        ,"music/aguas estancadas.mp3",prevDiaryEntry+"""-Esta ciudad esta llena de gente\n""",6,"intrala2")

    
    def chooseNext(self):
        Zones[0].playButton["command"]=lambda:Zones[0].toggle(Zones[4],True)        #if we go to title from next frame, if we touch play button we come back to that frame
        self.dialogueChanger(0,0)                                                   #reset dialogue of actual frame
        Zones[4].diaryText["text"]=self.diaryNotes                                  #update diary notes
        self.toggle(Zones[4])                                                       #go to next frame
        