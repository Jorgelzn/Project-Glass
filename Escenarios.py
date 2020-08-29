from MainFrame import *

class portal(mainFrame):

    def __init__(self, parent):
        super().__init__(parent,"images/portal.jpg","texts/portal.txt","music/test.mp3","""-He decidido adentrarme en el bosque en busca del portal que me llevará a Entoras
Despues de varios dias de camino, encotre lo que buscaba\n""",1,[["poder","riquezas","conocimiento","experiencias"],
        ["mi familia","mis amigos","mi vida","no pienso dejar nada atras"],
        ["magia elemental","magia arcana","magia druidrica","necromancia y demonologia"],
        ["Los resuelvo por la fuerza","Utilizo mi ingenio","Intento no meterme en problemas","Todo se puede resolver hablando"]])

        self.mapButton["command"]=lambda:self.emptyfunc()      #not allowed to use map before going inside the portal
        self.decisionPoints=[16,17,18,19]
        self.optionChecked=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def chooseNext(self):
        if self.optionChecked[2][1] or self.optionChecked[1][2] or self.optionChecked[0][3] or self.optionChecked[3][1] or self.optionChecked[0][2]:
            self.nextF=2
        elif self.optionChecked[0][1] or self.optionChecked[1][3] or self.optionChecked[2][3] or self.optionChecked[3][2] or self.optionChecked[3][1]:
            self.nextF=4
        else:
            self.nextF=3

        if len(Zones)<5:                #apaño cutre pa que no se vuelvan a crear las frames una vez introducidas por primera vez en Zones
            morthenFrame(self.parent,self.diaryNotes)
            intralaFrame(self.parent,self.diaryNotes)
            kanilikFrame(self.parent,self.diaryNotes)

        followFrame=Zones[self.nextF]                #variable para simplicidad de codigo
        followFrame.objects[0]["image"]=self.inventoryImages[1]      #when we go in the portal, the map is added
        followFrame.objects[0]["command"]=lambda:[followFrame.toggleElem(followFrame.descriptionFrame,0.1,0.15,0.7,0.8),followFrame.inventoryFrame.place_forget(),followFrame.setObjectDesc(followFrame.objects[0]["image"],followFrame.objectsDesc[0])]  #description of portal is added

        Zones[0].playButton["command"]=lambda:Zones[0].toggle(Zones[self.nextF])   #if we go to title from next frame, if we touch play button we come back to that frame
        self.toggle(Zones[self.nextF])
        
class morthenFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/morthen.jpg","texts/morthen.txt","music/wolf and moon.mp3",prevDiaryEntry+"""-Me encuentro ante un enorme muro de hielo\n""",2)

class kanilikFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/selvaKanilik.jpg","texts/kanilik.txt","music/elfos nocturnos.mp3",prevDiaryEntry+"""-Nunca antes habia visto una selva como esta\n""",3)



class intralaFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/intrala.jpg","texts/intrala.txt","music/aguas estancadas.mp3",prevDiaryEntry+"""-Esta isla parece totalmente deshabitada a primera vista\n""",4)