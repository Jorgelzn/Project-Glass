from tkinter import *
from PIL import Image,ImageTk,ImageFilter
from pygame import mixer

Zones=[]                                                        #global array to store all the frames in the game
InventoryImages=[]                                              #global array to store the images of the inventory
ObjectsDesc=["""Objecto misterioso
Todavía no ha sido descubierto""",
"""Mapa de Entoras
Se pueden apreciar las diferentes regiones de este mundo""",
"""Moneda Pirata
Utilizada por la gente de Intrala para el comercio""",
"""Runa de escarcha
Desprende una leve energía mágica""",
"""Amuleto salvaje
Un colmillo tallado cuelga de la cuerda""",
"""Anillo solar
Una gema naranja brilla en el centro del anillo.
Aparenta haber estado muchos años enterrado"""]
mixer.init()
mixer.music.set_volume(1)

class frame():

    def __init__(self,parent,bg,song,number,name):
        self.w=1000
        self.h=800
        self.bg = bg
        self.parent=parent
        self.name=name                                                      #name of the frame
        self.myFrame = Frame(self.parent,width=self.w,height=self.h)
        self.bgImage = ImageTk.PhotoImage(Image.open(self.bg))
        self.bgLabel = Label(self.myFrame,image=self.bgImage)
        self.bgLabel.pack()
        self.song=song                                                      #song of the frame
        self.number=number                                                  #position of the frame in the array of Zones

        checking=True                                                       #checking that the frame is not already in the Zones list before inserting
        for i in Zones:             
            if self.name==i.name:
                checking=False
        if checking:
            Zones.insert(self.number,self)                                  #insert the frame in the zones list

    def toggle(self,toelem,music=False):                                    #method used to hide the actual frame and display the frame passed as parameter
        self.myFrame.pack_forget()                                          #hide actual frame
        toelem.myFrame.pack()                                               #display element
        if music:                               
            mixer.music.load(toelem.song)                                   #display music
            mixer.music.play(loops=-1)                                      #loope=-1 means infinite loops of the song  