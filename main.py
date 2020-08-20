from tkinter import *
from Frames import *
from PIL import Image,ImageTk




def main():
    root = Tk()
    root.title("Entoras")
    root.geometry("1000x800")
    root.iconbitmap("images/Entoras.ico")
    root.resizable(False,False)

    loadingImage = ImageTk.PhotoImage(Image.open("images/loading.jpg"))     #setting loading image
    loading = Label(image=loadingImage)
    loading.pack()

    root.after(2000,lambda:start())     #we use the loading label to wait while the frames compile

    def start():                #defined to use it in after function
        game=titleFrame(root)
        loading.pack_forget()
        game.myFrame.pack()
        
    root.mainloop()





if __name__ == "__main__":
    main()