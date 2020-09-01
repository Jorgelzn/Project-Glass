from Frame import *

class mainFrame(frame):

    def __init__(self,parent,bg,dialogue,song,diaryEntry,number,name,options=None,decisions=None):
        super().__init__(parent,bg,song,number,name)
        print("FRAME")
        #variables
        self.decisionPoints=[]
        if decisions!=None:
            self.decisionPoints=decisions   #decice when to show the options to choose in dialogues ( 1d only)
        self.optionChecked=[]     #to store the decisions made in dialogues (1d or more dimensions)
        for i in range(len(self.decisionPoints)):
            self.optionChecked.append([0,0,0,0])
        self.options=options            #store text of the different options (1d or more dimensions)
        self.actualDecision=0       #store the decision in which we are in the moment to keep track where we are in dialogue to iterate arrays of decions and options
        self.nextF = 0              #variable used to choose which will be the next frame to go in the array of connected frames
        self.diaryNotes=diaryEntry
        self.countDialogue=0
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

        #opening text files
        self.phrases=[]
        for i in dialogue:
            textFile=open(i,"r")
            self.phrases.append(textFile.read().splitlines())
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
        self.inventoryIcon = ImageTk.PhotoImage(Image.open("images/inventory.png").resize((200,160)))
        self.menuIcon = ImageTk.PhotoImage(Image.open("images/menu.png").resize((200,160)))

        #MAP
        self.mapL = Label(self.mapFrame,image=self.mapImage)
        self.mapL.pack()
        self.backM = Button(self.mapFrame,text="Back",bg="#325062",fg="#4FC6B2",borderwidth=5,activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.mapFrame.place_forget())
        self.backM.place(rely=0.9,relx=0,relwidth=1,relheight=0.1)
        self.intralaMap=Button(self.mapFrame,text="Intrala",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15))
        self.intralaMap.place(rely=0.6,relx=0.05,relwidth=0.1,relheight=0.1)
        self.iretZarMap=Button(self.mapFrame,text="Iret-Zar",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15))
        self.iretZarMap.place(rely=0.6,relx=0.5,relwidth=0.1,relheight=0.1)
        self.morthenMap=Button(self.mapFrame,text="Morthen",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15))
        self.morthenMap.place(rely=0.1,relx=0.2,relwidth=0.1,relheight=0.1)
        self.kanilikMap=Button(self.mapFrame,text="Kanilik",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15))
        self.kanilikMap.place(rely=0.3,relx=0.4,relwidth=0.1,relheight=0.1)
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

        self.descriptionImageL = Label(self.descriptionFrame,bg="#325062",image=InventoryImages[0])
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
        for i in range(12):
            self.objects.append(Button(self.inventoryFrame,bg="#325062",activebackground="#325062",width=169,height=185,image=InventoryImages[0],command=lambda:[self.toggleElem(self.descriptionFrame,0.1,0.15,0.7,0.8),self.inventoryFrame.place_forget(),self.setObjectDesc(self.objects[i]["image"],ObjectsDesc[0])]))
            self.objects[i].grid(row=int(i/4),column=int(i%4))

        #TEXT DISPLAY AND ACTION BUTTON
        self.text = Label(self.textFrame,text=self.phrases[self.countDialogue][self.actualPhrase],borderwidth=10, relief="ridge",bg="#325062",fg="#4FC6B2",font=("Verdana", 15))
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

        if self.options!=None:
            for i in range(len(self.optionButtons)):                #setting first option is obtion buttons
                self.optionButtons[i]["text"]=self.options[0][i]
     


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
                if self.actualPhrase==len(self.phrases[self.countDialogue])-1:      #if we are in the last phrase of the dialogue execute method chooseNext to decide what to do
                    self.chooseNext()
                else:
                    self.actualPhrase+=1                #go to next phrase
                    self.text["text"]=self.phrases[self.countDialogue][self.actualPhrase]   #change text to next phrase
                    self.actualDecision+=1              #next decision for next decision point
                self.selector.place_forget()        #go back to text hiding selector
                if self.actualDecision in range(len(self.options)):
                    for i in range(len(self.optionButtons)):
                        self.optionButtons[i]["text"]=self.options[self.actualDecision][i]      #change text of decision buttons for next decision
                        self.optionButtons[i]["bg"]="#325062"                                   #reset default color for buttons
                        self.optionButtons[i]["activebackground"]="#325062"
        else:                                               #if we are not in a decision the dialogue proceeds as normal
            if self.actualPhrase==len(self.phrases[self.countDialogue])-1:      #if we are in the last phrase of the dialogue execute method chooseNext to decide what to do
                    self.chooseNext()
            else:                                           #the normal case is that we just go to the next phrase in the dialogue
                self.actualPhrase+=1
            self.text["text"]=self.phrases[self.countDialogue][self.actualPhrase]


    def toggleElem(self,elem,ly,lx,lw,lh):                      #function used to show inventory and menu
        self.textFrame.place_forget()
        self.graphicFrame.place_forget()
        elem.place(rely=ly,relx=lx,relwidth=lw,relheight=lh)


    def hideElem(self,elem):                                    #function used to get out of inventory and menu
        elem.place_forget()
        self.graphicFrame.place(rely=0,relx=0,relwidth=1,relheight=0.7)
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)

    def setObjectDesc(self,image,text):
        self.descriptionImageL["image"]=image
        self.descriptionL["text"]=text

    def changeObject(self,image,desc):
        counter=0
        for i in range(len(self.objects)):                  #loop to choose the next available position in inventory (next position with an ? in it)
            if self.objects[i]["image"]!=self.objects[len(self.objects)-1]["image"]:
                counter+=1
        self.objects[counter]["image"]=image      #image of object is changed
        self.objects[counter]["command"]=lambda:[self.toggleElem(self.descriptionFrame,0.1,0.15,0.7,0.8),self.inventoryFrame.place_forget(),self.setObjectDesc(self.objects[counter]["image"],desc)]  #description of object is added

    def optionChooser(self,optionsToCheck):
        selector=[0,0,0,0]
        if type(optionsToCheck[0])==type(1):
            for i in range(4):
                if optionsToCheck[i]==1:
                    selector[i]+=1
        else:
            for i in optionsToCheck:        #cuenta que opciones se han elegido y las acomula en el selector
                for j in range(4):
                    if i[j]==1:
                        selector[j]+=1
        return selector
    
    def dialogueChanger(self,number):
        self.actualPhrase=0
        self.actualDecision=0
        self.countDialogue=number
        self.text["text"]=self.phrases[self.countDialogue][self.actualPhrase]   #change text to next phrase
        for i in range(len(self.optionChecked)):
            for j in range(len(self.optionChecked[i])):
                self.optionChecked[i][j]=0

    def chooseNext(self):
        pass
    
    def emptyfunc(self):
        pass
