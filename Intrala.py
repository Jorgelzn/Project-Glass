from MainFrame import *

class intralaFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/intrala/intrala.jpg",
        "music/aguas estancadas.mp3",prevDiaryEntry+"""-Esta isla parece totalmente deshabitada a primera vista\n""","intrala1","texts/intrala/intro",
        [[["inspeccionar la arena","ir a la ciudad","andar por la playa","Observar el mar"]],
        [["solo pasaba por aqui","te estaba buscando (mentir)","he aparecido aqui de repente","estoy buscando un tesoro"]]],
        [[5],[6],[1]],[False,False])

        self.changeObject(InventoryImages[1],ObjectsDesc[1])   #put map
        self.imgNPC1=ImageTk.PhotoImage(Image.open("images/npcStages/intrala/intralanpc1.jpg").resize((1000,int(0.7*800)), Image.ANTIALIAS))   #image of the frame


    def chooseNext(self):

        if self.loader:                                 
            intralaCity(self.parent,self.diaryNotes)                                #create intralaCity object just once
            self.loader=False

        if self.countDialogue==0 or self.countDialogue==10:                                                       #introduction dialogue
            selector=self.optionChooser(self.optionChecked[self.countDecisions])
            if selector[0]==1:
                self.changeObject(InventoryImages[2],ObjectsDesc[2])                    #add coind to inventory
                if self.events[0]:                                                      #SI HEMOS COGIDO LA MONEDA IR A OTRO DIALOGO
                    self.dialogueChanger(4) 
                else:
                    self.dialogueChanger(2)                                                 
                    self.events[0]=True                                                     
                    self.options[0][0][0]="tantear el medallon"                                               #change the option "inspeccionar la arena"
            elif selector[1]==1:
                self.dialogueChanger(1)                                                 
            elif selector[2]==1:
                if self.events[1]:                                                          #SI YA HEMOS HABLADO CON EL NPC IR A OTRO DIALOGO
                    self.dialogueChanger(11)
                else:
                    self.imageLabel["image"]=self.imgNPC1                                   #display npc
                    self.dialogueChanger(3,1,1)
                    self.events[1]=True                                                     #EVENTO DE NPC REALIZADO                                               
            elif selector[3]==1:
                self.dialogueChanger(5)                                                 

        elif self.countDialogue==1:                                                     #dialogue for changing zone
            self.zoneChanger("intrala2",10)                                                         #change to the zone pased as parameter                                                            

        elif self.countDialogue==3:                                                     #second decision dialogue
            selector=self.optionChooser(self.optionChecked[self.countDecisions])
            if selector[0]==1:                                                                  
                self.dialogueChanger(6)                                                             
            elif selector[1]==1:
                self.dialogueChanger(7)
            elif selector[2]==1:
                self.dialogueChanger(8)
            elif selector[3]==1:
                self.dialogueChanger(9)
                
        else:
            self.imageLabel["image"]=self.mainImage                                                 #hide npc
            self.dialogueChanger(10,0,2)
      
        
class intralaCity(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/intrala/intralaCity.jpg"
        ,"music/aguas estancadas.mp3","""-Esta ciudad esta llena de gente\n""","intrala2","texts/intrala/intralaCity")

    
    def chooseNext(self):
        pass #not implemented