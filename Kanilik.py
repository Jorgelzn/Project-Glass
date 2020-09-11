from MainFrame import *

class kanilikFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/kanilik/selvaKanilik.jpg","music/forest.mp3",prevDiaryEntry+"""-Nunca antes habia visto una selva como esta\n""","kanilik1","texts/kanilik/intro",
        [[["Si, podrias ayudarme a bajar?","No gracias estoy bien","Que eres?","Porque deberia confiar en ti"]],
        [["Ir por el sendero de la derecha","Ir por el sendero de la izquierda","Observar los dos caminos","Observar la jungla"]]],
        [[13],[15],[12],[7],[3],[4],[1]])

        self.changeObject(InventoryImages[1],ObjectsDesc[1]) #put map
        self.imgNPC1=ImageTk.PhotoImage(Image.open("images/npcStages/kanilik/kaniliknpc1.jpg").resize((1000,int(0.7*800)), Image.ANTIALIAS))   #image of the frame

    def chooseNext(self):

        if self.loader:                                 
            iristhat(self.parent,self.diaryNotes)                                
            keran(self.parent,self.diaryNotes)
            self.loader=False
        
        
        if self.countDialogue==0:
            self.dialogueChanger(1,0,0)
            self.imageLabel["image"]=self.imgNPC1                                   #display npc
        elif self.countDialogue==1 or self.countDialogue==4 or self.countDialogue==5:
            selector=self.optionChooser(self.optionChecked[self.countDecisions])
            if selector[0]==1:
                self.dialogueChanger(2)
            elif selector[1]==1:
                self.dialogueChanger(3,1,2)
                self.imageLabel["image"]=self.mainImage  
            elif selector[2]==1:
                self.dialogueChanger(4,0,3)
            elif selector[3]==1:
                self.dialogueChanger(5,0,4)
        elif self.countDialogue==2:
            self.dialogueChanger(6,1,5)
            self.imageLabel["image"]=self.mainImage 
        elif self.countDialogue==3 or self.countDialogue==6 or self.countDialogue==11:
            selector=self.optionChooser(self.optionChecked[self.countDecisions])
            if selector[0]==1:
                self.dialogueChanger(7)
            elif selector[1]==1:
                self.dialogueChanger(8) 
            elif selector[2]==1:
                self.dialogueChanger(9)
            elif selector[3]==1:
                self.dialogueChanger(10)
        elif self.countDialogue==9 or self.countDialogue==10:
            self.dialogueChanger(11,1,6)
        elif self.countDialogue==7:
            self.zoneChanger("iristhat",11,1,6,True)
        elif self.countDialogue==8:
            self.zoneChanger("keran",11,1,6,True)


class iristhat(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/kanilik/iristhat.jpg"
        ,"music/elfos.mp3","""-Hay una abrumadora calma en el ambiente\n""","iristhat","texts/kanilik/iristhat")

    
    def chooseNext(self):
        pass #not implemented


class keran(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/kanilik/keran.jpg"
        ,"music/drums.mp3","""-Este sitio parece peligroso\n""","keran","texts/kanilik/keran")

    
    def chooseNext(self):
        pass #not implemented

