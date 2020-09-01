from MainFrame import *
from Intrala import intralaFrame
from Morthen import morthenFrame
from Kanilik import kanilikFrame
from IretZar import iretZarFrame
class portal(mainFrame):

    def __init__(self, parent):
        super().__init__(parent,"images/portal.jpg",["texts/portal.txt"],"music/test.mp3","""-He decidido adentrarme en el bosque en busca del portal que me llevará a Entoras
Despues de varios dias de camino, encotre lo que buscaba\n""",1,"portal",
        [[["conocimiento","experiencias","poder","riquezas"],
        ["mi familia","mis amigos","no pienso dejar nada atras","mi vida"],
        ["magia elemental","magia druidrica","necromancia y demonologia","magia arcana"],
        ["Intento no meterme en problemas","Los resuelvo por la fuerza","Utilizo mi ingenio","Todo se puede resolver hablando"]]],
        [[16,17,18,19]])     #nota para despues : implementar que la lista de decision points sea array 2d [[]] para que cada lista este asociada a un dialogo

        self.mapButton["command"]=lambda:self.emptyfunc()      #not allowed to use map before going inside the portal

    def chooseNext(self):
        selector = self.optionChooser(self.optionChecked[self.countDecisions])
        print(selector)
        self.nextF=selector.index(max(selector))+2  #el +2 es para cuadrar con el numero de zona de las cuatro iniciales
        
        morthenFrame(self.parent,self.diaryNotes)
        intralaFrame(self.parent,self.diaryNotes)
        kanilikFrame(self.parent,self.diaryNotes)
        iretZarFrame(self.parent,self.diaryNotes)               

        Zones[0].playButton["command"]=lambda:Zones[0].toggle(Zones[self.nextF])   #if we go to title from next frame, if we touch play button we come back to that frame
        self.toggle(Zones[self.nextF])

