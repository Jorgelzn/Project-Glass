from MainFrame import *
from Intrala import intralaFrame
from Morthen import morthenFrame
from Kanilik import kanilikFrame
from IretZar import iretZarFrame
class portal(mainFrame):

    def __init__(self, parent):
        super().__init__(parent,"images/landscapes/portal.jpg","music/portal.mp3","""-He decidido adentrarme en el bosque en busca del portal que me llevará a Entoras
Despues de varios dias de camino, encotre lo que buscaba\n""","portal","texts/portal",
        [[["conocimiento","experiencias","poder","riquezas"],
        ["mi familia","mis amigos","no pienso dejar nada atras","mi vida"],
        ["magia elemental","magia druidrica","necromancia y demonologia","magia arcana"],
        ["Intento no meterme en problemas","Los resuelvo por la fuerza","Utilizo mi ingenio","Todo se puede resolver hablando"]]],
        [[16,17,18,19]])
        self.mapButton["command"]=lambda:self.emptyfunc()      #not allowed to use map before going inside the portal (next frame)

    def chooseNext(self):
        selector = self.optionChooser(self.optionChecked[self.countDecisions])
        if selector.index(max(selector))==0:
            morthenFrame(self.parent,self.diaryNotes)
        elif selector.index(max(selector))==1:
            kanilikFrame(self.parent,self.diaryNotes)
        elif selector.index(max(selector))==2:
            intralaFrame(self.parent,self.diaryNotes)
        elif selector.index(max(selector))==3:
            iretZarFrame(self.parent,self.diaryNotes)


        Zones[0].playButton["command"]=lambda:Zones[0].toggle(Zones[len(Zones)-1],True)   #if we go to title from next frame, if we touch play button we come back to that frame
        self.toggle(Zones[len(Zones)-1],True)

