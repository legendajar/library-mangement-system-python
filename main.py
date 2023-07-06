from tkinter import *
from tkinter import ttk

class Main(object):
    def __init__(self,master):
        self.master = master

        # frames
        mainFrame = Frame(self.master)
        mainFrame.pack()

        # top frames
        topFrame = Frame(mainFrame, width = 1350, height = 70, bg = '#fafafa', padx = 20, relief = SUNKEN, borderwidth = 2)
        topFrame.pack(side=TOP, fill=X)

        # center frame
        centerFrame = Frame(mainFrame, width=1350,relief=RIDGE,bg="#e0f0f0",height=680)
        centerFrame.pack(side=TOP)

        # center left Frame
        centerLeft = Frame(centerFrame, width=900,height=700,bg='#f0f0f0',borderwidth=2,relief=SUNKEN)
        centerLeft.pack(side=LEFT)

        # center right frame
        centerRight = Frame(centerFrame,width=450,height=700,bg="#e0f0f0",borderwidth=2,relief=SUNKEN)
        centerRight.pack()

        # search bar
        search_bar = LabelFrame(centerRight,width=440,height=175,text='Search Box',bg='#9bc9ff')
        search_bar.pack(fill=BOTH)

        # list bar
        list_bar = LabelFrame(centerRight,width=440,height=175,text='List Box',bg='#fcc324')
        list_bar.pack(fill=BOTH)

        #add book
        self.iconbook = PhotoImage(file='Image/book.png')
        self.btnbook = Button(topFrame,text='Add Book',compound=LEFT,font='arial 12 bold')
        self.btnbook.pack(side=LEFT,padx=10)



def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.iconbitmap('Image/logo.png')
    root.mainloop()

if __name__ == '__main__':
    main()