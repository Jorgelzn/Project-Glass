from MainFrame import *

class iretZarFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/iret-zar.jpg","music/desert.mp3",prevDiaryEntry+"""-Este desierto parece infinito\n""","iretZarDesert","texts/iret-zar/intro",
        [[["Adentrarse en el desierto","Poner rumbo hacia las montañas","Seguir el rio","Observar el desierto"]]],
        [[9],[1]])

        self.changeObject(InventoryImages[1],ObjectsDesc[1]) #put map


    def chooseNext(self):

        if self.loader:                                 
            merchantCity(self.parent,self.diaryNotes)                                #create intralaCity object just once
            templeEntrance(self.parent,self.diaryNotes)
            banditCity(self.parent,self.diaryNotes)
            self.loader=False

        if self.countDialogue==0 or self.countDialogue==2:
            selector = self.optionChooser(self.optionChecked[self.countDecisions])

            if selector[0]==1:
                self.dialogueChanger(3)
            elif selector[1]==1:
                self.dialogueChanger(4)
            elif selector[2]==1:
                self.dialogueChanger(5)
            elif selector[3]==1:
                self.dialogueChanger(1)
        elif self.countDialogue==1:
            self.dialogueChanger(2,0,1)
        elif self.countDialogue==3:
            self.zoneChanger("templeEntrance",2,0,1,True)
        elif self.countDialogue==4:
            self.zoneChanger("banditCity",0)
        elif self.countDialogue==5:
            self.zoneChanger("merchantCity",0)

class merchantCity(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/cityEntrance.jpg"
        ,"music/desert.mp3","""-Hay una abrumadora calma en el ambiente\n""","merchantCity","texts/iret-zar/merchantCity")

    
    def chooseNext(self):
        pass #not implemented


class banditCity(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/banditCity.jpg"
        ,"music/desert.mp3","""-La gente de por aqui es rara\n""","banditCity","texts/iret-zar/banditCity")

    
    def chooseNext(self):
        pass #not implemented


class templeEntrance(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/templeEntrance.jpg"
        ,"music/mysticDesert.mp3","""-He encontrado la entrada de un templo en medio de la arena\n""","templeEntrance","texts/iret-zar/templeEntrance")

    
    def chooseNext(self):
        pass #not implemented


