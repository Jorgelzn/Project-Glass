from MainFrame import *

class kanilikFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/kanilik/selvaKanilik.jpg","music/elfos nocturnos.mp3",prevDiaryEntry+"""-Nunca antes habia visto una selva como esta\n""",3,"kanilik1","texts/kanilik")
        self.changeObject(InventoryImages[1],ObjectsDesc[1]) #put map

        self.changeObject(InventoryImages[4],ObjectsDesc[4])