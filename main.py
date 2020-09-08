from tkinter import *
from PIL import Image,ImageTk
from TitleFrame import titleFrame


root = Tk()
root.overrideredirect(True)                                             #Remove border
root.resizable(False,False)                                             #window cannot resize

width=1000                                                              #value for width of window
height=800                                                              #value for height of window
x = str(int(root.winfo_screenwidth()/2 - width/2))                      #calculations for centering the window in the screen
y = str(int(root.winfo_screenheight()/2 - height/2))
geo=str(width)+"x"+str(height)+"+"+x+"+"+y
root.geometry(geo)                                                      #size of the window


loadingImage = ImageTk.PhotoImage(Image.open("images/loading.jpg").resize((1000,800), Image.ANTIALIAS))     #setting loading image
loading = Label(image=loadingImage)
loading.pack()


def start():                                                            #defined to use it in after function
    game=titleFrame(root)                                               #create first scene object
    loading.pack_forget()                                               #forget the loading image
    game.myFrame.pack()                                                 #draw first scene


def main():                                                         #draw loading image

    root.after(2000,lambda:start())                                         #we use the loading label to wait while the frames compile, after 2 seconds, start the game
    root.mainloop()                                                         #main loop of the game





if __name__ == "__main__":
    main()