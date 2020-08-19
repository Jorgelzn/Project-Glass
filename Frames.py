from tkinter import *
from PIL import Image,ImageTk,ImageFilter

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
        self.nextF=None
        self.titleScreen=None
    def toggle(self,toelem):
        self.myFrame.pack_forget()
        toelem.myFrame.pack()



class titleFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/title.jpg")
        print("NUMERO 1")
        self.nextF=mainFrame(self.parent)
        self.nextF.titleScreen=self
        self.playButton=Button(self.myFrame,text="Explore",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF),font=("Verdana", 15))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)

        self.restartButton=Button(self.myFrame,text="New Adventure",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF),font=("Verdana", 15))
        self.restartButton.place(rely=0.85,relx=0.4,relwidth=0.2,relheight=0.1)

        self.creditsButton=Button(self.myFrame,text="Credits",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF),font=("Verdana", 15))
        self.creditsButton.place(rely=0.05,relx=0.05,relwidth=0.1,relheight=0.05)


class mainFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/forest.jpg")
        print("NUMERO 2")
        #setting all frames

        self.textFrame=Frame(self.myFrame)
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)

        self.graphicFrame=Frame(self.myFrame,bg="white")
        self.graphicFrame.place(rely=0,relx=0,relwidth=1,relheight=0.7)

        self.menuFrame = Frame(self.myFrame,bg="#325062")

        self.inventoryFrame = Frame(self.myFrame,bg="#325062")

        #opening text file

        self.textFile=open("texts/testing.txt","r")
        self.phrases=self.textFile.read().splitlines()
        self.actualPhrase = 0
        
        #setting all elements in the frames

        #IMAGES
        self.mainImage = ImageTk.PhotoImage(Image.open(self.bg).resize((1000,int(0.7*800)), Image.ANTIALIAS))
        self.imageLabel = Label(self.graphicFrame,image=self.mainImage)
        self.imageLabel.place(rely=0,relx=0,relwidth=1,relheight=1)
        self.menuImage = Image.open(self.bg).filter(ImageFilter.BLUR)
        self.menuBg=ImageTk.PhotoImage(self.menuImage)
        self.bgLabel["image"]=self.menuBg

        #MENU BUTTONS
        self.menuButton=Button(self.graphicFrame,text="Menu",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggleElem(self.menuFrame))
        self.menuButton.place(rely=0,relx=0,relwidth=0.2,relheight=0.15)

        self.titleButton = Button(self.menuFrame,text="Title Screen",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggle(self.titleScreen))
        self.titleButton.place(rely=0,relx=0,relwidth=1,relheight=0.3)
        
        self.mapButton = Button(self.menuFrame,text="Map",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15))
        self.mapButton.place(rely=0.3,relx=0,relwidth=1,relheight=0.4)

        self.continueButton = Button(self.menuFrame,text="Continue",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.hideElem(self.menuFrame))
        self.continueButton.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)

        #INVENTORY BUTTONS
        self.inventoryButton=Button(self.graphicFrame,text="Inventory",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggleElem(self.inventoryFrame))
        self.inventoryButton.place(rely=0,relx=0.8,relwidth=0.2,relheight=0.15)

        self.continueButton = Button(self.inventoryFrame,text="Continue",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.hideElem(self.inventoryFrame))
        self.continueButton.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)

        #TEXT DISPLAY AND ACTION BUTTON
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

    def toggleElem(self,elem):
        self.textFrame.place_forget()
        self.graphicFrame.place_forget()
        elem.place(rely=0.15,relx=0.35,relwidth=0.3,relheight=0.7)

    def hideElem(self,elem):
        elem.place_forget()
        self.graphicFrame.place(rely=0,relx=0,relwidth=1,relheight=0.7)
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)















"""class rFrame(frame):

    def __init__(self,parent):
        super().__init__(parent,"images/r.jpg")
        self.nextF=mainFrame(self.parent)
        self.nextF.titleScreen=self.titleScreen
        self.playButton=Button(self.myFrame,text="Main Menu",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggle(self.nextF))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)

"""



#nota para mi : si las frames no se guardan en variables no se ven o se comportan raro