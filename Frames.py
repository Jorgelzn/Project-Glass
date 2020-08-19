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



class titleFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/b.jpg")
        self.nextF=rFrame(self.parent)
        #self.nextF.nextF=self para enlazar la siguiente frame con esta
        self.playButton=Button(self.myFrame,text="PLAY",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)


class textTest(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/forest.jpg")
        self.textFrame=Frame(self.myFrame)
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)

        self.menuFrame=Frame(self.myFrame,bg="#325062")
        self.menuFrame.place(rely=0,relx=0,relwidth=1,relheight=0.1)

        self.graphicFrame=Frame(self.myFrame,bg="white")
        self.graphicFrame.place(rely=0.1,relx=0,relwidth=1,relheight=0.6)

        self.textFile=open("texts/testing.txt","r")
        self.phrases=self.textFile.read().splitlines()
        self.actualPhrase = 0
        

        self.mainImage = ImageTk.PhotoImage(Image.open(self.bg).resize((1000,int(0.6*800)), Image.ANTIALIAS))
        self.imageLabel = Label(self.graphicFrame,image=self.mainImage)
        self.imageLabel.pack()

        self.menuButton=Button(self.menuFrame,text="Menu",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF))
        self.menuButton.place(rely=0,relx=0,relwidth=0.2,relheight=1)

        self.inventoryButton=Button(self.menuFrame,text="Inventory",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF))
        self.inventoryButton.place(rely=0,relx=0.8,relwidth=0.2,relheight=1)

        self.text = Label(self.textFrame,text=self.phrases[self.actualPhrase],borderwidth=10, relief="ridge",bg="#325062",fg="#4FC6B2",font=("Verdana", 15))
        self.text.place(rely=0,relx=0,relwidth=0.8,relheight=1)

        self.nextButton=Button(self.textFrame,text="Next",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.nextPhrase())
        self.nextButton.place(rely=0,relx=0.8,relwidth=0.2,relheight=1)

    def nextPhrase(self):
        if self.actualPhrase==len(self.phrases)-1:
            print("no mas")
        else:
            self.actualPhrase+=1
            self.text["text"]=self.phrases[self.actualPhrase]

class rFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/r.jpg")
        self.nextF=textTest(self.parent)
        self.playButton=Button(self.myFrame,text="Main Menu",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)





#nota para mi : si las frames no se guardan en variables no se ven o se comportan raro