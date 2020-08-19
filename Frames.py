from tkinter import *
from PIL import Image,ImageTk,ImageFilter

class frame():

    def __init__(self,parent,bg):
        self.w=1000
        self.h=800
        self.bg = bg
        self.parent=parent
        self.myFrame = Frame(self.parent,width=self.w,height=self.h)
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
        self.credits = creditsFrame(self.parent)
        self.credits.titleScreen=self
        self.playButton=Button(self.myFrame,text="Explore",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggle(self.nextF))
        self.playButton.place(rely=0.7,relx=0.4,relwidth=0.2,relheight=0.1)

        self.restartButton=Button(self.myFrame,text="New Adventure",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggle(self.nextF))
        self.restartButton.place(rely=0.85,relx=0.4,relwidth=0.2,relheight=0.1)

        self.creditsButton=Button(self.myFrame,text="Credits",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggle(self.credits))
        self.creditsButton.place(rely=0.05,relx=0.05,relwidth=0.1,relheight=0.05)


class creditsFrame(frame):

    def __init__(self, parent):
        super().__init__(parent,"images/credits.jpg")
        self.text=Label(self.myFrame,text="""Programer and Designer:
Jorge Lizcano

Images:
Chris Cold
Luka Mivsek""",bg="#325062",fg="#4FC6B2",font=("Verdana", 10))
        self.text.place(rely=0.1,relx=0.3,relwidth=0.4,relheight=0.7)
        print("NUMERO 3")
        self.titleButton = Button(self.myFrame,text="Title Screen",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggle(self.titleScreen))
        self.titleButton.place(rely=0.85,relx=0.3,relwidth=0.4,relheight=0.1)

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
        self.inventoryImage = ImageTk.PhotoImage(Image.open("images/question.png"))


        #MENU BUTTONS
        self.menuButton=Button(self.graphicFrame,text="Menu",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggleElem(self.menuFrame,0.15,0.35,0.3,0.7))
        self.menuButton.place(rely=0,relx=0,relwidth=0.2,relheight=0.15)

        self.titleButton = Button(self.menuFrame,text="Title Screen",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:[self.toggle(self.titleScreen),self.hideElem(self.menuFrame)])
        self.titleButton.place(rely=0,relx=0,relwidth=1,relheight=0.3)
        
        self.mapButton = Button(self.menuFrame,text="Map",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15))
        self.mapButton.place(rely=0.3,relx=0,relwidth=1,relheight=0.4)

        self.continueButton = Button(self.menuFrame,text="Continue",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.hideElem(self.menuFrame))
        self.continueButton.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)


        #INVENTORY BUTTONS
        self.inventoryButton=Button(self.graphicFrame,text="Inventory",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",command=lambda:self.toggleElem(self.inventoryFrame,0.1,0.15,0.7,0.8))
        self.inventoryButton.place(rely=0,relx=0.8,relwidth=0.2,relheight=0.15)

        self.continueButton = Button(self.inventoryFrame,text="Continue",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.hideElem(self.inventoryFrame))
        self.continueButton.place(rely=0.9,relx=0,relwidth=1,relheight=0.1)

        self.object1  = Button(self.inventoryFrame,text="obj1",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object1.grid(row=0,column=0)
        self.object2  = Button(self.inventoryFrame,text="obj2",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object2.grid(row=0,column=1)
        self.object3  = Button(self.inventoryFrame,text="obj3",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object3.grid(row=0,column=2)
        self.object4  = Button(self.inventoryFrame,text="obj4",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object4.grid(row=0,column=3)
        self.object1  = Button(self.inventoryFrame,text="obj5",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object1.grid(row=1,column=0)
        self.object2  = Button(self.inventoryFrame,text="obj6",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object2.grid(row=1,column=1)
        self.object3  = Button(self.inventoryFrame,text="obj7",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object3.grid(row=1,column=2)
        self.object4  = Button(self.inventoryFrame,text="obj8",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object4.grid(row=1,column=3)
        self.object1  = Button(self.inventoryFrame,text="obj9",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object1.grid(row=2,column=0)
        self.object2  = Button(self.inventoryFrame,text="obj10",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object2.grid(row=2,column=1)
        self.object3  = Button(self.inventoryFrame,text="obj11",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object3.grid(row=2,column=2)
        self.object4  = Button(self.inventoryFrame,text="obj12",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",width=169,height=185,image=self.inventoryImage)
        self.object4.grid(row=2,column=3)


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

    def toggleElem(self,elem,ly,lx,lw,lh):
        self.textFrame.place_forget()
        self.graphicFrame.place_forget()
        elem.place(rely=ly,relx=lx,relwidth=lw,relheight=lh)

    def hideElem(self,elem):
        elem.place_forget()
        self.graphicFrame.place(rely=0,relx=0,relwidth=1,relheight=0.7)
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)







#nota para mi : si las frames no se guardan en variables no se ven o se comportan raro