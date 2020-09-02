from tkinter import *
from PIL import Image,ImageTk
from TitleFrame import titleFrame




def main():
    root = Tk()
    root.title("Entoras")
    root.geometry("1000x800")
    root.iconbitmap("images/Entoras.ico")
    root.resizable(False,False)

    loadingImage = ImageTk.PhotoImage(Image.open("images/loading.jpg"))     #setting loading image
    loading = Label(image=loadingImage)
    loading.pack()                          #draw loading image

    root.after(2000,lambda:start())     #we use the loading label to wait while the frames compile, after 2 seconds, start the game

    def start():                #defined to use it in after function
        game=titleFrame(root)      #create first scene object
        loading.pack_forget()   #forget the loading image
        game.myFrame.pack()     #draw first scene
        
    root.mainloop()             #main loop of the game





if __name__ == "__main__":
    main()