from MainFrame import *

class intralaFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/intrala.jpg",["texts/intrala.txt","texts/intralatesting1.txt","texts/intralatesting2.txt"]
        ,"music/aguas estancadas.mp3",prevDiaryEntry+"""-Esta isla parece totalmente deshabitada a primera vista\n""",4,"intrala1",
        [["inspeccionar la arena","ir a la ciudad","quedarse en la playa","Observar el mar"]],
        [5])

        self.changeObject(InventoryImages[1],ObjectsDesc[1])   #put map

    def chooseNext(self):
        if self.countDialogue==0:  #only do this in first decision
            selector=self.optionChooser(self.optionChecked[0])
            if selector[0]==1:
                self.changeObject(InventoryImages[2],ObjectsDesc[2])
                self.dialogueChanger(2)
            elif selector[1]==1:
                self.dialogueChanger(1)

        elif self.countDialogue==1:
            intralaCity(self.parent,self.diaryNotes)
            self.nextF=len(Zones)-1
            Zones[0].playButton["command"]=lambda:Zones[0].toggle(Zones[self.nextF])   #if we go to title from next frame, if we touch play button we come back to that frame
            self.toggle(Zones[self.nextF])

        elif self.countDialogue==2:
            self.dialogueChanger(0)             #cuando acaba dialogo 2 ir a dialogo 0

class intralaCity(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/intralaCity.jpg",["texts/intrala.txt"]
        ,"music/aguas estancadas.mp3",prevDiaryEntry+"""-Esta ciudad esta llena de gente\n""",6,"intrala2")