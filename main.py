from tkinter import *
from Frames import *
from PIL import Image,ImageTk



def main():
    root = Tk()
    root.title("Glass")
    root.geometry("1000x800")
    root.resizable(False,False)
    
    mainFrame(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()