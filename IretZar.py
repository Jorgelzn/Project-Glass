from MainFrame import *

class iretZarFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images/landscapes/iret-zar/iret-zar.jpg","music/desert.mp3",prevDiaryEntry+"""-Parece que este desierto no tiene final\n""",5,"iretzar1","texts/iret-zar")
        self.changeObject(InventoryImages[1],ObjectsDesc[1])  #put map

        self.changeObject(InventoryImages[5],ObjectsDesc[5])