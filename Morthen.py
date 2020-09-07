from MainFrame import *

class morthenFrame(mainFrame):

    def __init__(self, parent,prevDiaryEntry):
        super().__init__(parent,"images//landscapes/morthen/morthen.jpg",["texts/morthen.txt"],"music/wolf and moon.mp3",prevDiaryEntry+"""-Me encuentro ante un enorme muro de hielo\n""",2,"morthen1")
        self.changeObject(InventoryImages[1],ObjectsDesc[1]) #put map
        self.changeObject(InventoryImages[3],ObjectsDesc[3])