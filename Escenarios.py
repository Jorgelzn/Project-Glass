from MainFrame import *

class portal(mainFrame):

    def __init__(self, parent):
        super().__init__(parent,"images/portal.jpg","texts/portal.txt","music/test.mp3",1)
        self.mapButton["command"]=lambda:self.emptyfunc()      #not allowed to use map before going inside the portal
        self.decisionPoints=[16,17,18]
        self.optionChecked=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.options=[["poder","riquezas","conocimiento","experiencias"],
        ["mi familia","mis amigos","mi vida","no pienso dejar nada atras"],
        ["magia elemental","magia arcana","magia druidrica","necromancia y demonologia"],]


        for i in range(len(self.optionButtons)):
            self.optionButtons[i]["text"]=self.options[0][i]

    def chooseNext(self):
        if self.optionChecked[2][1] or self.optionChecked[1][2] or self.optionChecked[0][3]:
            self.nextF=2
        elif self.optionChecked[0][1] or self.optionChecked[1][3] or self.optionChecked[2][3]:
            self.nextF=3
        else:
            self.nextF=4

        if len(Zones)<5:                #apaño cutre pa que no se vuelvan a crear las frames una vez introducidas por primera vez en Zones
            morthenFrame(self.parent)
            intralaFrame(self.parent)
            kanilikFrame(self.parent)

        followFrame=Zones[self.nextF]                #variable para simplicidad de codigo
        followFrame.objects[0]["image"]=self.inventoryImages[1]      #when we go in the portal, the map is added
        followFrame.objects[0]["command"]=lambda:[followFrame.toggleElem(followFrame.descriptionFrame,0.1,0.15,0.7,0.8),followFrame.inventoryFrame.place_forget(),followFrame.setObjectDesc(followFrame.objects[0]["image"],followFrame.objectsDesc[0])]  #description of portal is added
        if followFrame.diaryNotes not in followFrame.diaryText["text"]:
            followFrame.diaryText["text"]+=followFrame.diaryNotes
        self.toggle(Zones[self.nextF])
        
class morthenFrame(mainFrame):

    def __init__(self, parent):
        super().__init__(parent,"images/morthen.jpg","texts/morthen.txt","music/wolf and moon.mp3",2)
        self.diaryNotes="""-Me encutro ante un enorme muro de hielo\n"""

class kanilikFrame(mainFrame):

    def __init__(self, parent):
        super().__init__(parent,"images/selvaKanilik.jpg","texts/kanilik.txt","music/elfos nocturnos.mp3",3)
        self.diaryNotes="""-Nunca antes habia visto una selva como esta\n"""


class intralaFrame(mainFrame):

    def __init__(self, parent):
        super().__init__(parent,"images/intrala.jpg","texts/intrala.txt","music/aguas estancadas.mp3",4)
        self.diaryNotes="""-Esta isla parece totalmente desabitada a primera vista\n"""