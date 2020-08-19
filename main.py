from tkinter import *
from Frames import *
from PIL import Image,ImageTk



def main():
    root = Tk()
    root.title("Entoras")
    root.geometry("1000x800")
    root.iconbitmap("images/Entoras.ico")
    root.resizable(False,False)
    
    game=titleFrame(root)
    game.myFrame.pack()
    root.mainloop()

if __name__ == "__main__":
    main()