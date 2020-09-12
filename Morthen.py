from MainFrame import *

class morthenFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/morthen/morthen.jpg","music/morthen.mp3",prevDiaryEntry+"""-Estoy en el borde de un acantilado de hielo\n""","acantiladoMorthen","texts/morthen/acantilado",
        [[["Ir a la ciudad","Observar el mar","Observar las montañas","Asomarse al acantilado"]]],
        [[10],[1]])

        self.changeObject(InventoryImages[1],ObjectsDesc[1]) #put map


    def chooseNext(self):
        if self.loader:                                 
            vikingCity(self.parent,self.diaryNotes)
            self.loader=False

        if self.countDialogue==0:
            self.dialogueChanger(1,0,1)   
        if self.countDialogue==1:
            selector=self.optionChooser(self.optionChecked[self.countDecisions])
            
            if selector[0]==1:
                self.dialogueChanger(2)
            elif selector[1]==1:
                self.dialogueChanger(3)
            elif selector[2]==1:
                self.dialogueChanger(4)
            elif selector[3]==1:
                self.dialogueChanger(5)

        elif self.countDialogue==2:
            self.zoneChanger("vikingCity",1,0,1,True)

        elif self.countDialogue==3 or self.countDialogue==4 or self.countDialogue==5:
            self.dialogueChanger(1,0,1)



class vikingCity(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/morthen/vikingCity.jpg"
        ,"music/viking.mp3","""-Da la sensacion de que aqui no vive nadie\n""","vikingCity","texts/morthen/vikingCity")

    
    def chooseNext(self):
        pass #not implemented