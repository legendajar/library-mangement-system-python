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
        self.lbl_search = Label(search_bar, text='Search: ',font='Arial 12 bold',bg='#9bc9ff', fg='white')
        self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
        self.ent_search=Entry(search_bar,width=30,bd=10)
        self.ent_search.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.btn_search=Button(search_bar, text='Search',font='arial 12 bold', bg='#fcc324',fg='white')
        self.btn_search.grid(row=0,column=4,padx=20,pady=10)

        # list bar
        list_bar = LabelFrame(centerRight,width=440,height=175,text='List Box',bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text='Sort By', font='times 16 bold', fg='#2488ff', bg='#fcc324')
        lbl_list.grid(row=0,column=2)
        self.listChoice = IntVar()
        rb1=Radiobutton(list_bar,text='All Books',var=self.listChoice, value=1, bg='#fcc324')
        rb2=Radiobutton(list_bar,text='In Library',var=self.listChoice, value=2, bg='#fcc324')
        rb3=Radiobutton(list_bar,text='Borrow Books',var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list=Button(list_bar,text='List Books',bg='#2488ff',fg='white',font='arial 12')
        btn_list.grid(row=1,column=3,padx=40,pady=10)
        
        image_bar = Frame(centerRight,width=440,height=350)
        image_bar.pack(fill=BOTH)
        self.title_right=Label(image_bar, text='Welcome to our Library', font='arial 12')
        self.title_right.grid(row=0)
        self.img_library=PhotoImage(file='Image/library.png')
        self.lblImg = Label(image_bar, image=self.img_library)
        self.lblImg.grid(row=1)
        
        # add book
        self.iconbook = PhotoImage(file="Image/add-book.png")
        self.btngive = Button(topFrame, text='Add Book', font="Arial 12 bold", padx=10, image=self.iconbook, compound=LEFT)
        self.btngive.pack(side=LEFT)
        
        # add member button        
        self.iconmember = PhotoImage(file="Image/user.png")
        self.btnmember = Button(topFrame,text='Add Member',font='arial 12 bold',padx=10,image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT)
        
        # give book
        self.icongive = PhotoImage(file="Image/book.png")
        self.btngive = Button(topFrame, text='Give Book', font="Arial 12 bold", padx=10,image=self.icongive,compound=LEFT)
        self.btngive.pack(side=LEFT)
        



def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.iconbitmap('Image/logo.png')
    root.mainloop()

if __name__ == '__main__':
    main()