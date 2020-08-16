from tkinter import *
from PIL import Image,ImageTk

class frame():

    def __init__(self,parent,bg):
        self.w=1000
        self.h=800
        self.bg = bg
        self.parent=parent
        self.myFrame = Frame(parent,width=self.w,height=self.h)
        self.myFrame.pack()
        self.bgImage = ImageTk.PhotoImage(Image.open(self.bg))
        self.bgLabel = Label(self.myFrame,image=self.bgImage)
        self.bgLabel.pack()


    def toggle(self,toelem):
        self.myFrame.destroy()
        toelem.myFrame.pack()



class mainFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/b.jpg")
        self.playButton=Button(self.myFrame,text="PLAY",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(rFrame(self.parent)))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)

class rFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/r.jpg")
        self.playButton=Button(self.myFrame,text="Main Menu",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(mainFrame(self.parent)))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)