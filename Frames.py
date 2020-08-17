from tkinter import *
from PIL import Image,ImageTk

class frame():

    def __init__(self,parent,bg):
        self.w=1000
        self.h=800
        self.bg = bg
        self.parent=parent
        self.myFrame = Frame(self.parent,width=self.w,height=self.h)
        self.myFrame.pack()
        self.bgImage = ImageTk.PhotoImage(Image.open(self.bg))
        self.bgLabel = Label(self.myFrame,image=self.bgImage)
        self.bgLabel.pack()


    def toggle(self,toelem):
        self.myFrame.pack_forget()
        toelem.myFrame.pack()



class mainFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/b.jpg")
        self.nextF=rFrame(self.parent)
        self.nextF.nextF=self
        self.playButton=Button(self.myFrame,text="PLAY",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)
        print("NUMERO 1")


class textTest(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/forest.jpg")
        self.text1=Label(self.myFrame,text="hey bros",bg="#325062",fg="#4FC6B2")
        self.text1.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)

class rFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/r.jpg")
        self.playButton=Button(self.myFrame,text="Main Menu",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)
        print("NUMERO 2")





#nota para mi : si las frames no se guardan en variables no se ven o se comportan raro