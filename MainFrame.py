from Frame import *
import os
class mainFrame(frame):

    def __init__(self,parent,bg,song,diaryEntry,name,directoryName,options=None,decisions=None,events=None,point=0):
        super().__init__(parent,bg,song,name)
        print("FRAME")  

        #VARIABLES 

        self.decisionPoints=[[]]                            #variable to know the pharses of the dialogues in which there is going to be a decision, 2d to cover multiple dialogues
        if decisions!=None:                                 #only if the parameter decisions is not None we pass the value to the attribute
            self.decisionPoints=decisions                   #decice when to show the options to choose in dialogues
        self.optionChecked=[]                               #to store the decisions made in dialogues, 2d to cover the multiple dialogues
        for i in range(len(self.decisionPoints)):
            self.optionChecked.append([])                   #for each dialogue we append a list
            for j in range(len(self.decisionPoints[i])):    #for each list/dialogue there a list of arrays [0,0,0,0] so if we have to dialogues with 2 decisions we have [[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]
                self.optionChecked[i].append([0,0,0,0])
        self.options=options                                #store text of the different options, 2d to cover multiples dialogues
        self.actualDecision=0                               #store the decision in which we are in the moment to keep track where we are in dialogue to iterate arrays of decions and options
        self.actualPhrase = 0                               #store the phrase in which we are (in the actual dialogue) to navigate in the phrases array
        self.diaryNotes=diaryEntry                          #used to store the text that will be displayed in the diary section
        self.countDialogue=0                                #variable used to know in which dialogue  of the array of dialogues we are
        self.countDecisions=0                               #variable used to know which array of decisions we have to use of the options array
        self.objectsName=[]                                 #variable that is used to store the description of the objects in the frame inventory (to diferenciate between them as copy them to next frame)
        self.loader=True                                    #variable used to create the frame objects just once
        self.events=events
        self.pointChecker=point
        #SETTING ALL THE FRAMES USED IN THE MAIN FRAME

        self.textFrame=Frame(self.myFrame)                                  #frame used for the display of the text and the next button
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)      #place at the lower part of the window

        self.graphicFrame=Frame(self.myFrame,bg="#325062")                  #part used to show the image of the frame, the menu button and the inventory button
        self.graphicFrame.place(rely=0,relx=0,relwidth=1,relheight=0.7)     #placed above the textframe

        self.menuFrame = Frame(self.myFrame,bg="#325062")                   #frame used to display the menu once the menu button is used

        self.inventoryFrame = Frame(self.myFrame,bg="#325062")              #frame used to display the inventory once the inventory button is used

        self.descriptionFrame = Frame(self.myFrame,bg="#325062")            #frame used to show the description of the objects when the object button is used

        self.mapFrame = Frame(self.myFrame,bg="#325062")                    #frame used to display the map once the map button is used

        self.diaryFrame = Frame(self.myFrame,bg="#325062")                  #frame used to display the diary when the diary button is used

        #opening text files
        self.phrases=[]                                                     #array storing all the dialogues and phrases, it is 2d to store all the dialogues [["dialogue","1"],["dialogue","2"]]
        for i in os.listdir(directoryName):
            textFile=open(directoryName+"/"+i,"r")
            self.phrases.append(textFile.read().splitlines())               #each position of phrases (phrases[i]) stores one dialogue array, ["hola","buenas","tardes"]


        #SETTING ALL THE ELEMENTES IN THE FRAME


        #IMAGES
        self.mainImage = ImageTk.PhotoImage(Image.open(self.bg).resize((self.w,int(0.7*self.h)), Image.ANTIALIAS))   #image of the frame
        self.imageLabel = Label(self.graphicFrame,image=self.mainImage)                                         #label where the image is placed
        self.imageLabel.place(rely=0,relx=0,relwidth=1,relheight=1)                                             #placed ocuppying all the graphicframe space
        self.menuImage = Image.open(self.bg).resize((self.w,self.h), Image.ANTIALIAS)
        self.menuImage=self.menuImage.filter(ImageFilter.BLUR)                                           #blur image for menu and inventory
        self.menuBg=ImageTk.PhotoImage(self.menuImage)                                                          #blur version of main image to use as background in the menu and inventory
        self.bgLabel["image"]=self.menuBg                                                                       #set image
        self.mapImage = ImageTk.PhotoImage(Image.open("images/bigmap.jpg"))                                     #image for the map section
        self.inventoryIcon = ImageTk.PhotoImage(Image.open("images/inventory.png").resize((200,160)))           #image for the inventory button
        self.menuIcon = ImageTk.PhotoImage(Image.open("images/menu.png").resize((200,160)))                     #image for the menu button


        #MAP
        self.mapL = Label(self.mapFrame,image=self.mapImage)        #label to place the map inside, placed in the map frame 
        self.mapL.pack()                                            #place the label with the map image

        #buttons for the map section
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
        self.diaryText.place(rely=0,relx=0,relwidth=1,relheight=1)          #place the text of the diary frame

        self.backD = Button(self.diaryFrame,text="Back",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.diaryFrame.place_forget())
        self.backD.place(rely=0.9,relx=0,relwidth=1,relheight=0.1)          #place back button for the diary, it goes back to menu frame


        #MENU BUTTONS
        self.menuButton=Button(self.graphicFrame,bg="#325062",borderwidth=5, relief="raised",activebackground="#325062",image=self.menuIcon,command=lambda:self.toggleElem(self.menuFrame,0.15,0.35,0.3,0.7))
        self.menuButton.place(rely=0,relx=0,relwidth=0.2,relheight=0.25)

        self.titleButton = Button(self.menuFrame,text="Title Screen",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:[self.toggle(Zones[0],True),self.hideElem(self.menuFrame)])
        self.titleButton.place(rely=0,relx=0,relwidth=1,relheight=0.25)
        
        self.mapButton = Button(self.menuFrame,text="Map",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggleElem(self.mapFrame,0,0,1,1))
        self.mapButton.place(rely=0.25,relx=0,relwidth=1,relheight=0.25)

        self.diaryButton = Button(self.menuFrame,text="Diary",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.toggleElem(self.diaryFrame,0.15,0.2,0.6,0.8))
        self.diaryButton.place(rely=0.5,relx=0,relwidth=1,relheight=0.25)

        self.continueButton = Button(self.menuFrame,text="Continue",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.hideElem(self.menuFrame))
        self.continueButton.place(rely=0.75,relx=0,relwidth=1,relheight=0.25)


        #DESCRIPTION BUTTONS
        self.descriptionImageL = Label(self.descriptionFrame,bg="#325062",image=InventoryImages[0])
        self.descriptionImageL.place(rely=0,relx=0,relwidth=1,relheight=0.6)        #label to store the image of the description of an object, placed in description frame

        self.descriptionL = Label(self.descriptionFrame,text="",bg="#325062",fg="#4FC6B2",font=("Verdana", 15))
        self.descriptionL.place(rely=0.6,relx=0,relwidth=1,relheight=0.3)           #label to store the text of the description of an object, placed in description frame

        self.backI = Button(self.descriptionFrame,text="Back",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:[self.hideElem(self.descriptionFrame),self.toggleElem(self.inventoryFrame,0.1,0.15,0.7,0.8)])
        self.backI.place(rely=0.9,relx=0,relwidth=1,relheight=0.1)                  #button to get back to the inventory (hide the description of an object)


        #INVENTORY BUTTONS
        self.inventoryButton=Button(self.graphicFrame,bg="#325062",borderwidth=5, relief="raised",activebackground="#325062",image=self.inventoryIcon,command=lambda:self.toggleElem(self.inventoryFrame,0.1,0.15,0.7,0.8))
        self.inventoryButton.place(rely=0,relx=0.8,relwidth=0.2,relheight=0.25)     #inventory button to access inventory, placed in the graphic frame

        self.continueButton = Button(self.inventoryFrame,text="Continue",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.hideElem(self.inventoryFrame))
        self.continueButton.place(rely=0.89,relx=0,relwidth=1,relheight=0.11)         #continue button to go back to game (hide inventory), placed at the lower part of inventory frame

        self.objects=[]                                                             #array used to store all the buttons for the objects in the inventory
        for i in range(12):                                                         #there will be 12 objects
            self.objects.append(Button(self.inventoryFrame,bg="#325062",activebackground="#325062",width=self.w*0.17,height=self.h*0.23,image=InventoryImages[0],command=lambda:[self.toggleElem(self.descriptionFrame,0.1,0.15,0.7,0.8),self.inventoryFrame.place_forget(),self.setObjectDesc(self.objects[i]["image"],ObjectsDesc[0])]))
            self.objects[i].grid(row=int(i/4),column=int(i%4))                      #grid layout used to palce the objects in the inventory frame (4x3)


        #TEXT DISPLAY AND ACTION BUTTON
        self.text = Label(self.textFrame,text=self.phrases[self.countDialogue][self.actualPhrase],borderwidth=10, relief="ridge",bg="#325062",fg="#4FC6B2",font=("Verdana", 15))
        self.text.place(rely=0,relx=0,relwidth=0.8,relheight=1)             #label showing the text of the frame in the textframe

        self.nextButton=Button(self.textFrame,text="Next",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.action())
        self.nextButton.place(rely=0,relx=0.8,relwidth=0.2,relheight=1)     #button used to pass to the next text or used when you have selected an option, placed at the right part of textframe


        #SELECTOR OF OPTIONS IN DIALOGUE
        self.optionButtons=[]                                                           #array to store the 4 buttons of the options
        self.selector = Frame(self.textFrame,bg="#325062")                              #frame used to place the buttons for a decision to be choosen, will be placed in the textframe
        self.optionButtons.append(Button(self.selector,text="",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.checkOption(0)))
        self.optionButtons[0].place(rely=0,relx=0,relwidth=1,relheight=0.25)            
        self.optionButtons.append(Button(self.selector,text="",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.checkOption(1)))
        self.optionButtons[1].place(rely=0.25,relx=0,relwidth=1,relheight=0.25)
        self.optionButtons.append(Button(self.selector,text="",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.checkOption(2)))
        self.optionButtons[2].place(rely=0.5,relx=0,relwidth=1,relheight=0.25)
        self.optionButtons.append(Button(self.selector,text="",bg="#325062",fg="#4FC6B2",activebackground="#325062",activeforeground="#4FC6B2",font=("Verdana", 15),command=lambda:self.checkOption(3)))
        self.optionButtons[3].place(rely=0.75,relx=0,relwidth=1,relheight=0.25)

        if self.options!=None:                                                          #check that the attribute options is not None because parameter was not None
            for i in range(len(self.optionButtons)):                                    
                self.optionButtons[i]["text"]=self.options[self.countDecisions][0][i]   #set the text of the option buttons to the first decision that will appear
     


    def checkOption(self,number):                                                                   #function used to check which option is selected in the decision and store it in the optionchecked array
        if 1 in self.optionChecked[self.countDecisions][self.actualDecision]:                       #if there is already a 1 in an option of the actual decision we have to set all the options to 0 because we have choosen another one
            for i in range(len(self.optionChecked[self.countDecisions][self.actualDecision])):      #a for loop only for the actual decision (will be always 4 iterations ex: [0,0,1,0]->[0,0,0,0])
                self.optionChecked[self.countDecisions][self.actualDecision][i]=0                   #set all options in the decision to 0

        for i in range(len(self.optionButtons)):                                                    #for used to set the color of the chosen option to a brighter one to identify chosen option
            if i == number:                                                                         #change color of chosen button
                self.optionButtons[i]["bg"]="#406070"
                self.optionButtons[i]["activebackground"]="#406070"
            else:                                                                                   #all other buttons get the default color
                self.optionButtons[i]["bg"]="#325062"
                self.optionButtons[i]["activebackground"]="#325062"
        self.optionChecked[self.countDecisions][self.actualDecision][number]=1                      #the the chosen option to one in the optionChecked array
        print(self.optionChecked[self.countDecisions])                                              #print the actual decision to test if we are setting the option correctly


    def action(self):                                                                          #function used to determine what to do when the button next is pressed
        if  self.pointChecker!=100 and self.actualPhrase in self.decisionPoints[self.pointChecker]:                       #if we are in a decision point of the dialogue, text is replaced by the options table in order to choose
            self.selector.place(rely=0,relx=0,relwidth=0.8,relheight=1)                         #place the option buttons
            if 1 in self.optionChecked[self.countDecisions][self.actualDecision]:               #if in the actual decision (self.optionChecked[actual]) there is a one (we use next button with an option chosen)
                if self.actualPhrase==len(self.phrases[self.countDialogue])-1:                   #if we are in the last phrase of the dialogue execute method chooseNext to decide what to do
                    self.chooseNext()                                                           #method defined in each individual frame
                else:                                                                           #if we are not in the last phrase
                    self.actualPhrase+=1                                                        #go to next phrase
                    self.text["text"]=self.phrases[self.countDialogue][self.actualPhrase]       #change text to next phrase
                    self.actualDecision+=1                                                      #next decision for next decision point
                self.selector.place_forget()                                                    #go back to text hiding selector
            if self.actualDecision in range(len(self.options[self.countDecisions])):        #checking that the actual decision is the range of the options array in the actual dialogue
                for i in range(len(self.optionButtons)):
                    self.optionButtons[i]["text"]=self.options[self.countDecisions][self.actualDecision][i]         #change text of decision buttons for next decision
                    self.optionButtons[i]["bg"]="#325062"                                                           #reset default color for buttons
                    self.optionButtons[i]["activebackground"]="#325062"
        else:                                                                           #if we are not in a decision the dialogue proceeds as normal
            if self.actualPhrase==len(self.phrases[self.countDialogue])-1:              #if we are in the last phrase of the dialogue execute method chooseNext to decide what to do
                self.chooseNext()                                                   #method defined in each individual frame
            else:                                                                       #the normal case is that we just go to the next phrase in the dialogue
                self.actualPhrase+=1                                                    #go to next phrase
            self.text["text"]=self.phrases[self.countDialogue][self.actualPhrase]       #change the text of the frame to the one of the following phrase


    def toggleElem(self,elem,ly,lx,lw,lh):                          #method used to show inventory and menu
        self.textFrame.place_forget()                               #hide text frame
        self.graphicFrame.place_forget()                            #hide graphic frame
        elem.place(rely=ly,relx=lx,relwidth=lw,relheight=lh)        #place the element passed as parameter


    def hideElem(self,elem):                                                #function used to get out of inventory and menu
        elem.place_forget()                                                 #hide element passed as parameter
        self.graphicFrame.place(rely=0,relx=0,relwidth=1,relheight=0.7)     #place graphic frame
        self.textFrame.place(rely=0.7,relx=0,relwidth=1,relheight=0.3)      #place text frame


    def setObjectDesc(self,image,text):                 #method used to set the text an image of the description of an object
        self.descriptionImageL["image"]=image           #change image of the image label in description frame
        self.descriptionL["text"]=text                  #change text of text label in description frame


    def changeObject(self,image,desc):                                                          #method to change the image of object in inventory and its description
        counter=0                                                                               #variable to navigate in the objects array
        if desc not in self.objectsName:                                                        #if desc is already in objectsName, it means that the object is already in the inventory so we dont want to repeat it and we dont change the object
            self.objectsName.append(desc)                                                       #if desc not in objectsName we add it, for not repeating this object
            for i in range(len(self.objects)):                                                  #loop to choose the next available position in inventory (next position with an ? in it)
                if self.objects[i]["image"]!=self.objects[len(self.objects)-1]["image"]:        #if actual image is not the ? image, go to next object
                    counter+=1                                                                  #add 1 to counter
            self.objects[counter]["image"]=image                                                #image of object is changed
            self.objects[counter]["command"]=lambda:[self.toggleElem(self.descriptionFrame,0.1,0.15,0.7,0.8),self.inventoryFrame.place_forget(),self.setObjectDesc(self.objects[counter]["image"],desc)]    #description of object is changed


    def optionChooser(self,optionsToCheck):             #method to sum up the decisions chosen in the option buttons and store them in the selector array
        selector=[0,0,0,0]                              #each decision sums 1 to its position in the selector decision:[0,1,0,0]->selector:[x,y+1,z,t]                                       #if the options parameter is 2d we use 2 loops to travel in the array
        for i in optionsToCheck:        
            for j in range(4):
                if i[j]==1:                         #if the position is 1 add 1 to the same position in the selector
                    selector[j]+=1
        return selector
    

    def dialogueChanger(self,number,deci=0,point=100):                                        #method to change the dialogue that will be shown in the text box and the decisions that wll be used
        self.actualPhrase=0                                                         #set actual phrase to 0 to start dialogue at the beginninng
        self.actualDecision=0                                                       #set decision to 0 to start at the first decision of the new dialogue
        self.countDecisions=deci                                                    #set the decisions to the value of the parameter
        self.countDialogue=number                                                   #set the dialogue to the value of the parameter
        self.pointChecker=point                                                  #set the point of decision for the dialogue
        self.text["text"]=self.phrases[self.countDialogue][self.actualPhrase]       #change text to first phrase of the new dialogue
        for i in range(len(self.optionChecked[self.countDecisions])):               #for to set the array to optionschecked to 0
            for j in range(len(self.optionChecked[self.countDecisions][i])):
                self.optionChecked[self.countDecisions][i][j]=0


    def copyingObjects(self,elem):                                                  #method used to pass all the objects in the inventory of a frame to another frame
        for i in range(len(self.objects)):                                          #loop for all objects
            if i < len(self.objectsName):                                           
                elem.changeObject(self.objects[i]["image"],self.objectsName[i])     #if object is in objectsName set the description of that array
            else:
                elem.changeObject(self.objects[i]["image"],ObjectsDesc[0])          #if object is not in objectsName set description of unknown object

    def zoneChanger(self,zone,dialogue=0,options=0,point=0,music=False):
        number=0
        for i in range(len(Zones)):
            if Zones[i].name==zone:
                number=i
        Zones[0].playButton["command"]=lambda:Zones[0].toggle(Zones[number],True)       #if we go to title from next frame, if we touch play button we come back to that frame
        if Zones[number].diaryText["text"] not in self.diaryText["text"]:                       #check para no repetir diary entrys
            Zones[number].diaryText["text"]=self.diaryNotes+Zones[number].diaryNotes                                  #update diary notes
        self.copyingObjects(Zones[number])                                              #copy objects to next zone
        self.dialogueChanger(dialogue,options,point)                                              #reset the dialogue of the actual zone
        self.toggle(Zones[number],music)                                                      #change to the next zone


    def chooseNext(self):                       #method that will be different in each frame, so each frame will have to implement it
        pass
    

    def emptyfunc(self):                        #empty method
        pass
