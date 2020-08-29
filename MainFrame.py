from Frame import *

class mainFrame(frame):

    def __init__(self,parent,bg,dialogue,song,number):
        super().__init__(parent,bg,song,number)
        print("FRAME")

        #variables

        self.diaryNotes="""-He decidido adentrarme en el bosque en busca del portal que me llevará a Entoras
Despues de varios dias de camino, encotre lo que buscaba\n"""

        self.decisionPoints=[]   #decice when to show the options to choose in dialogues ( 1d only)
        self.optionChecked=[]     #to store the decisions made in dialogues (1d or more dimensions)
        self.options=[]            #store text of the different options (1d or more dimensions)
        self.actualDecision=0       #store the decision in which we are in the moment to keep track where we are in dialogue to iterate arrays of decions and options
        self.nextF = 0              #variable used to choose which will be the next frame to go in the array of connected frames
        #setting all frames

        self.textFrame=Frame(self.myFrame)
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)

        self.graphicFrame=Frame(self.myFrame,bg="#325062")
        self.graphicFrame.place(rely=0,relx=0,relwidth=1,relheight=0.7)

        self.menuFrame = Frame(self.myFrame,bg="#325062")

        self.inventoryFrame = Frame(self.myFrame,bg="#325062")

        self.descriptionFrame = Frame(self.myFrame,bg="#325062")

        self.mapFrame = Frame(self.myFrame,bg="#325062")

        self.diaryFrame = Frame(self.myFrame,bg="#325062")

        #opening text file

        self.textFile=open(dialogue,"r")
        self.phrases=self.textFile.read().splitlines()
        self.actualPhrase = 0
        
        #setting all elements in the frames

        #IMAGES
        self.mainImage = ImageTk.PhotoImage(Image.open(self.bg).resize((1000,int(0.7*800)), Image.ANTIALIAS))
        self.imageLabel = Label(self.graphicFrame,image=self.mainImage)
        self.imageLabel.place(rely=0,relx=0,relwidth=1,relheight=1)
        self.menuImage = Image.open(self.bg).filter(ImageFilter.BLUR)       #blur image for menu and inventory
        self.menuBg=ImageTk.PhotoImage(self.menuImage)
        self.bgLabel["image"]=self.menuBg
        self.mapImage = ImageTk.PhotoImage(Image.open("images/bigmap.jpg"))
        self.inventoryImages = [ImageTk.PhotoImage(Image.open("images/question.png").resize((70,114))),
                                ImageTk.PhotoImage(Image.open("images/map.jpg").resize((150,150)))]
        self.inventoryIcon = ImageTk.PhotoImage(Image.open("images/inventory.png").resize((200,160)))
        self.menuIcon = ImageTk.PhotoImage(Image.open("images/menu.png").resize((200,160)))

        #MAP
        self.mapL = Label(self.mapFrame,image=self.mapImage)
        self.mapL.pack()
        self.backM = Button(self.mapFrame,text="Back",bg="#325062",fg="#4FC6B2",borderwidth=5,activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.mapFrame.place_forget())
        self.backM.place(rely=0.9,relx=0,relwidth=1,relheight=0.1)

        #DIARY

        self.diaryText = Label(self.diaryFrame,text=self.diaryNotes, relief="ridge",bg="#325062",fg="#4FC6B2",font=("Verdana", 10))
        self.diaryText.place(rely=0,relx=0,relwidth=1,relheight=1)
        self.backD = Button(self.diaryFrame,text="Back",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.diaryFrame.place_forget())
        self.backD.place(rely=0.9,relx=0,relwidth=1,relheight=0.1)


        #MENU BUTTONS
        self.menuButton=Button(self.graphicFrame,bg="#325062",borderwidth=5, relief="raised",activebackground="#325062",image=self.menuIcon,command=lambda:self.toggleElem(self.menuFrame,0.15,0.35,0.3,0.7))
        self.menuButton.place(rely=0,relx=0,relwidth=0.2,relheight=0.25)

        self.titleButton = Button(self.menuFrame,text="Title Screen",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:[self.toggle(Zones[0]),self.hideElem(self.menuFrame)])
        self.titleButton.place(rely=0,relx=0,relwidth=1,relheight=0.25)
        
        self.mapButton = Button(self.menuFrame,text="Map",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggleElem(self.mapFrame,0,0,1,1))
        self.mapButton.place(rely=0.25,relx=0,relwidth=1,relheight=0.25)

        self.diaryButton = Button(self.menuFrame,text="Diary",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggleElem(self.diaryFrame,0.15,0.2,0.6,0.8))
        self.diaryButton.place(rely=0.5,relx=0,relwidth=1,relheight=0.25)

        self.continueButton = Button(self.menuFrame,text="Continue",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.hideElem(self.menuFrame))
        self.continueButton.place(rely=0.75,relx=0,relwidth=1,relheight=0.25)


        #DESCRIPTION BUTTONS

        self.descriptionImageL = Label(self.descriptionFrame,bg="#325062",image=self.inventoryImages[0])
        self.descriptionImageL.place(rely=0,relx=0,relwidth=1,relheight=0.6)
        self.descriptionL = Label(self.descriptionFrame,text="",bg="#325062",fg="#4FC6B2",font=("Verdana", 15))
        self.descriptionL.place(rely=0.6,relx=0,relwidth=1,relheight=0.3)
        self.backI = Button(self.descriptionFrame,text="Back",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:[self.hideElem(self.descriptionFrame),self.toggleElem(self.inventoryFrame,0.1,0.15,0.7,0.8)])
        self.backI.place(rely=0.9,relx=0,relwidth=1,relheight=0.1)


        #INVENTORY BUTTONS
        self.inventoryButton=Button(self.graphicFrame,bg="#325062",borderwidth=5, relief="raised",activebackground="#325062",image=self.inventoryIcon,command=lambda:self.toggleElem(self.inventoryFrame,0.1,0.15,0.7,0.8))
        self.inventoryButton.place(rely=0,relx=0.8,relwidth=0.2,relheight=0.25)

        self.continueButton = Button(self.inventoryFrame,text="Continue",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.hideElem(self.inventoryFrame))
        self.continueButton.place(rely=0.9,relx=0,relwidth=1,relheight=0.1)
        self.objects=[]
        self.objectsDesc=["""Mapa de Entoras
Se pueden apreciar las diferentes regiones de este mundo""",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
                          "Objecto misterioso que aun no ha sido descubierto",
        ]
        for i in range(12):
            self.objects.append(Button(self.inventoryFrame,bg="#325062",activebackground="#325062",width=169,height=185,image=self.inventoryImages[0],command=lambda:[self.toggleElem(self.descriptionFrame,0.1,0.15,0.7,0.8),self.inventoryFrame.place_forget(),self.setObjectDesc(self.objects[i]["image"],self.objectsDesc[1])]))
            self.objects[i].grid(row=int(i/4),column=int(i%4))


        #TEXT DISPLAY AND ACTION BUTTON
        self.text = Label(self.textFrame,text=self.phrases[self.actualPhrase],borderwidth=10, relief="ridge",bg="#325062",fg="#4FC6B2",font=("Verdana", 15))
        self.text.place(rely=0,relx=0,relwidth=0.8,relheight=1)

        self.nextButton=Button(self.textFrame,text="Next",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.action())
        self.nextButton.place(rely=0,relx=0.8,relwidth=0.2,relheight=1)

        #SELECTOR OF OPTIONS IN DIALOGUE

        self.selector = Frame(self.textFrame,bg="#325062")
        self.optionButtons=[]
        self.optionButtons.append(Button(self.selector,text="",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.checkOption(0)))
        self.optionButtons[0].place(rely=0,relx=0,relwidth=1,relheight=0.25)
        self.optionButtons.append(Button(self.selector,text="",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.checkOption(1)))
        self.optionButtons[1].place(rely=0.25,relx=0,relwidth=1,relheight=0.25)
        self.optionButtons.append(Button(self.selector,text="",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.checkOption(2)))
        self.optionButtons[2].place(rely=0.5,relx=0,relwidth=1,relheight=0.25)
        self.optionButtons.append(Button(self.selector,text="",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.checkOption(3)))
        self.optionButtons[3].place(rely=0.75,relx=0,relwidth=1,relheight=0.25)
     


    def checkOption(self,number):                           #function used to check which option is selected in the decision and store it in the optionchecked array
        if 1 in self.optionChecked[self.actualDecision]:
            for i in range(len(self.optionChecked[self.actualDecision])):
                self.optionChecked[self.actualDecision][i]=0
        for i in range(len(self.optionButtons)):
            if i == number:
                self.optionButtons[i]["bg"]="#406070"
                self.optionButtons[i]["activebackground"]="#406070"
            else:
                self.optionButtons[i]["bg"]="#325062"
                self.optionButtons[i]["activebackground"]="#325062"
        self.optionChecked[self.actualDecision][number]=1
        print(self.optionChecked)


    def action(self):                                   #function used to determine what to do when the button next is pressed

        if self.actualPhrase in self.decisionPoints:        #if we are in a decision point of the dialogue, it is replaced by the options table in order to choose
            self.selector.place(rely=0,relx=0,relwidth=0.8,relheight=1)
            if 1 in self.optionChecked[self.actualDecision]:        #if in the actual decision (self.optionChecked[actual]) there is a one
                self.actualDecision+=1              #next decision for next decision point
                self.selector.place_forget()        #go back to text hiding selector
                self.actualPhrase+=1                #go to next phrase
                self.text["text"]=self.phrases[self.actualPhrase]   #change text to next phrase
                if self.actualDecision in range(len(self.options)):
                    for i in range(len(self.optionButtons)):
                        self.optionButtons[i]["text"]=self.options[self.actualDecision][i]      #change text of decision buttons for next decision
                        self.optionButtons[i]["bg"]="#325062"                                   #reset default color for buttons
                        self.optionButtons[i]["activebackground"]="#325062"
        else:                                               #if we are not in a decision the dialogue proceeds as normal
            if self.actualPhrase==len(self.phrases)-1:      #if we are in the last phrase of the dialogue we will go to the next frame
                    self.chooseNext()
            else:                                           #the normal case is that we just go to the next phrase in the dialogue
                self.actualPhrase+=1
            self.text["text"]=self.phrases[self.actualPhrase]


    def toggleElem(self,elem,ly,lx,lw,lh):                      #function used to show inventory and menu
        self.textFrame.place_forget()
        self.graphicFrame.place_forget()
        elem.place(rely=ly,relx=lx,relwidth=lw,relheight=lh)


    def hideElem(self,elem):                                    #function used to get out of inventory and menu
        elem.place_forget()
        self.graphicFrame.place(rely=0,relx=0,relwidth=1,relheight=0.7)
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)

    def reset(self):                                            #reset values of selected 

        self.actualPhrase=0
        self.actualDecision=0
        self.text["text"]=self.phrases[self.actualPhrase]

        for j in range(len(self.optionChecked)):            #set all decisions to 0
            for i in range(len(self.optionChecked[j])):
                self.optionChecked[j][i]=0

        if len(self.options)!=0:                        #if there is options in the frame
            for i in range(len(self.optionButtons)):
                self.optionButtons[i]["text"]=self.options[self.actualDecision][i]      #change text of decision buttons for first option again
                self.optionButtons[i]["bg"]="#325062"                                   #reset default color for buttons
                self.optionButtons[i]["activebackground"]="#325062"

    def setObjectDesc(self,image,text):
        self.descriptionImageL["image"]=image
        self.descriptionL["text"]=text

    def chooseNext(self):
        pass
    
    def emptyfunc(self):
        pass
