from MainFrame import *

class iretZarFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/iret-zar.jpg","music/desert.mp3",prevDiaryEntry+"""-Este desierto parece infinito\n""","iretZarDesert","texts/iret-zar/intro",
        [[["Adentrarse en el desierto","Poner rumbo hacia las montañas","Seguir el rio","Observar el desierto"]]],
        [[9],[1]])

        self.changeObject(InventoryImages[1],ObjectsDesc[1]) #put map


    def chooseNext(self):

        if self.loader:                                 
            merchantCity(self.parent,self.diaryNotes)                               
            desertEvent(self.parent,self.diaryNotes)
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
            self.zoneChanger("desertEvent",2,0,1)
        elif self.countDialogue==4:
            self.zoneChanger("banditCity",2,0,1,True)
        elif self.countDialogue==5:
            self.zoneChanger("merchantCity",2,0,1,True)

class merchantCity(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/cityEntrance.jpg"
        ,"music/merchants.mp3","""-Seguro que en esta ciudad hago buenos contactos\n""","merchantCity","texts/iret-zar/merchantCity")

    
    def chooseNext(self):
        pass #not implemented


class banditCity(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/banditCity.jpg"
        ,"music/bandits.mp3","""-La gente de por aqui es rara\n""","banditCity","texts/iret-zar/banditCity")

    
    def chooseNext(self):
        pass #not implemented


class templeEntrance(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/templeEntrance.jpg"
        ,"music/mysticDesert.mp3","""-He encontrado la entrada de un templo en medio de la arena\n""","templeEntrance","texts/iret-zar/templeEntrance")

    
    def chooseNext(self):
        pass #not implemented



class desertEvent(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/sandstorm.jpg","music/desert.mp3","""-Ha aparecido una tormenta de arena de la nada\n""","desertEvent","texts/iret-zar/desertEvent",
        [[["Adentrarse en la tormenta","Volver atras","Observar a lo lejos","Protegerse de la arena"]],
        [["Ir hacia el norte","Ir hacia el este","Ir hacia el oeste","Ir hacia el sur"]]],
        [[4],[2,5,7,9],[1]])     #SI TIENES UN DIALOGO CON VARIAS DECISIONES PONER ESAS [DECISIONES] EN LA MISMA POSICION QUE EN EL ARRAY DE PUNTOS DE DECISION 
                                #EN ESTE CASO [DECISION A DONDE IR (NORTE....) POSICION 1]-> [CUATRO PUNTOS DE DECISION 2,4,7,9 PARA ESE DIALOGO POSICION 1]
                                #si no se bugea por la forma en la que structuré las variables de mainframe

    def chooseNext(self):

        if self.loader:                                 
            templeEntrance(self.parent,self.diaryNotes)                                
            self.loader=False

        if self.countDialogue==0 or self.countDialogue==6:
            selector = self.optionChooser(self.optionChecked[self.countDecisions])
            if selector[0]==1:
                self.dialogueChanger(1,1,1)
            elif selector[1]==1:
                self.dialogueChanger(2)
            elif selector[2]==1:
                self.dialogueChanger(3)
            elif selector[3]==1:
                self.dialogueChanger(4)

        elif self.countDialogue==1:
            selector=self.optionChooser(self.optionChecked[self.countDecisions],[0,3,3,2])   #orden norte sur sur oeste
            if selector==4:       
                self.dialogueChanger(5)
            else:
                self.dialogueChanger(7)

        elif self.countDialogue==2:
            self.zoneChanger("iretZarDesert",0,0,0)
        elif self.countDialogue==3 or self.countDialogue==4 or self.countDialogue==7:
            self.dialogueChanger(6,0,2)
        elif self.countDialogue==5:
            self.zoneChanger("templeEntrance",0,0,0,True)
