from tkinter import *
from PIL import Image,ImageTk,ImageFilter
from pygame import mixer

Zones=[]
InventoryImages=[]
ObjectsDesc=["Objecto misterioso que aun no ha sido descubierto",
"""Mapa de Entoras
Se pueden apreciar las diferentes regiones de este mundo""",
"""Moneda Pirata
Utilizada por la gente de Intrala para el comercio"""]
mixer.init()
mixer.music.set_volume(1)

class frame():

    def __init__(self,parent,bg,song,number):
        self.w=1000
        self.h=800
        self.bg = bg
        self.parent=parent
        self.myFrame = Frame(self.parent,width=self.w,height=self.h)
        self.bgImage = ImageTk.PhotoImage(Image.open(self.bg))
        self.bgLabel = Label(self.myFrame,image=self.bgImage)
        self.bgLabel.pack()
        self.song=song
        Zones.insert(number,self)

    def toggle(self,toelem):
        self.myFrame.pack_forget()
        toelem.myFrame.pack()
        mixer.music.load(toelem.song)
        mixer.music.play()