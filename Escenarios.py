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
        selector=[0,0,0,0]
        for i in self.optionChecked:        #cuenta que opciones se han elegido y las acomula en el selector
            for j in range(4):
                if i[j]==1:
                    selector[j]+=1

        print(selector)
        self.nextF=selector.index(max(selector))+2  #el +2 es para cuadrar con el numero de zona de las cuatro iniciales
        if len(Zones)<5:                #apaño cutre pa que no se vuelvan a crear las frames solo una vez introducidas por primera vez en Zones
            morthenFrame(self.parent,self.diaryNotes)
            intralaFrame(self.parent,self.diaryNotes)
            kanilikFrame(self.parent,self.diaryNotes)
            iretZarFrame(self.parent,self.diaryNotes)               


        Zones[0].playButton["command"]=lambda:Zones[0].toggle(Zones[self.nextF])   #if we go to title from next frame, if we touch play button we come back to that frame
        self.toggle(Zones[self.nextF])
        
class morthenFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/morthen.jpg","texts/morthen.txt","music/wolf and moon.mp3",prevDiaryEntry+"""-Me encuentro ante un enorme muro de hielo\n""",2)
        self.changeObject(InventoryImages[1],ObjectsDesc[1],0)
        self.changeObject(InventoryImages[3],ObjectsDesc[3],1)

class kanilikFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/selvaKanilik.jpg","texts/kanilik.txt","music/elfos nocturnos.mp3",prevDiaryEntry+"""-Nunca antes habia visto una selva como esta\n""",3)
        self.changeObject(InventoryImages[1],ObjectsDesc[1],0)
        self.changeObject(InventoryImages[4],ObjectsDesc[4],1)


class intralaFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/intrala.jpg","texts/intrala.txt","music/aguas estancadas.mp3",prevDiaryEntry+"""-Esta isla parece totalmente deshabitada a primera vista\n""",4)
        self.changeObject(InventoryImages[1],ObjectsDesc[1],0)
        self.changeObject(InventoryImages[2],ObjectsDesc[2],1)
class iretZarFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/iret-zar.jpg","texts/iret-zar.txt","music/desert.mp3",prevDiaryEntry+"""-Parece que este desierto no tiene final\n""",5)
        self.changeObject(InventoryImages[1],ObjectsDesc[1],0)
        self.changeObject(InventoryImages[5],ObjectsDesc[5],1)