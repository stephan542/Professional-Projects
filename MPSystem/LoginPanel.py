import tkinter

from System import System
from SecretaryPanel import SecretaryPanel

class loginPanel:
    def __init__(self,frame,width,height,gui):
        self.frame = frame
        self.width = width
        self.height = height
        self.gui = gui

    def showView(self):
        login = tkinter.PanedWindow(self.frame,bg="#228B22")

        panel_top =  tkinter.PanedWindow(login,bg="#228B22")
        panel_bottom = tkinter.PanedWindow(login, bg="white")

        mainlabel = tkinter.Label(panel_top,text="Constituency Management System",bg="#228B22",fg="white",font="sans-serif 20 bold")
        mainlabel.place(x=15, y=5, width=self.width * 2 + 5, height=120)

        background = tkinter.PhotoImage(file="assets/images/backg.png")
        backgroundlabel = tkinter.Label(panel_bottom,image=background)
        backgroundlabel.image = background
        backgroundlabel.place(x=-5, y=-2, width=self.width * 2 + 10, height=self.height*2-120)

        sign_in = tkinter.PanedWindow(backgroundlabel, bg="white",sashwidth= 10)
        sign_in.place(x=self.width-int(self.width*0.51)/2, y=self.height-280, width=int(self.width*0.51)+int(self.width*0.1818),
                      height=int(self.width*0.51)+int(self.width*0.1818))

        jlpimage = tkinter.PhotoImage(file="assets/images/jlp.png")
        jlpimage_label = tkinter.Label(sign_in, image=jlpimage,bg="white")
        jlpimage_label.image = jlpimage
        jlpimage_label.place(x=0, y=0, width=int(self.width*0.51)+int(self.width*0.1818),height=200)

        forgotpassword = tkinter.Label(sign_in,text="Forgot Password?",font="Arial 7",fg="purple",bg="white")
        forgotpassword.place(x=-1, y=330,width=int(self.width*0.51)+int(self.width*0.1818),height=30)

        userimage = tkinter.PhotoImage(file="assets/images/user.png",width=20,height=20)
        userimage_label = tkinter.Label(sign_in,image=userimage,bg="white")
        userimage_label.image=userimage
        userimage_label.place(x=0, y=200, width=32,height=32)

        lockimage = tkinter.PhotoImage(file="assets/images/lock.png",width=20, height=20)
        lockimage_label = tkinter.Label(sign_in, image=lockimage,bg="white")
        lockimage_label.image = lockimage
        lockimage_label.place(x=0, y=225,width=32,height=32)

        user_name  = tkinter.Entry(sign_in,text="user_name",font="Arial 12", relief=tkinter.FLAT,width=100,fg='gray')
        user_name.place(x=32, y=200,width=int(self.width*0.51)+int(self.width*0.1818),height=32)
        user_name.insert(0,"user_name")

        password = tkinter.Entry(sign_in,text="password",font="Arial 12", relief=tkinter.FLAT, width=100,fg='gray')
        password.place(x=32, y=225,width=int(self.width*0.51)+int(self.width*0.1818),height=32)
        password.insert(0, "password")

        loginbutton = tkinter.Button(sign_in,text="Login",font="Arial 10 bold",bg='green')
        funct = lambda e: self.authenicate(System().authenticate(user_name.get(),password.get()))
        loginbutton.bind('<ButtonPress-1>',funct)
        loginbutton.place(x=0, y=270,width=int(self.width*0.51)+int(self.width*0.1818))

        self.message_label = tkinter.Label(sign_in, text="",fg="red",bg="white")
        self.message_label.place(x=-1, y=300,width=int(self.width*0.51)+int(self.width*0.1818))

        clearmessage = lambda e: self.clear_message()
        password.bind('<Key>', clearmessage)
        user_name.bind('<Key>', clearmessage)

        password.bind('<ButtonPress-1>',clearfield)
        user_name.bind('<ButtonPress-1>',clearfield)

        forgotpassword.bind('<ButtonPress-1>', self.gui.nothing)
        password.bind('<FocusOut>',resetfield)
        user_name.bind('<FocusOut>',resetfield)

        panel_top.place(x=-2, y=0, width=self.width * 2 + 10, height=120)
        panel_bottom.place(x=-2, y=120, width=self.width * 2 + 10, height=self.height*2-120)
        login.pack(fill=tkinter.BOTH,expand=1)

    def clear_message(self):
        self.message_label['text'] = ""

    def authenicate(self,value):
        if value == 1:
            [x.destroy() for x in self.frame.winfo_children()]
            SecretaryPanel(self.frame,self.width,self.height,2,self.gui).showView()
        elif value == 0:
            [x.destroy() for x in self.frame.winfo_children()]
            #self.MPPanel()
        elif value == -1:
            self.message_label['text'] = "Invalid Username"
        elif value == -2:
            self.message_label['text'] = "Invalid Password"
        else:
            print("Something when wrong with login in")

   
            
def clearfield(e):
        e.widget.delete(0, 'end')
        e.widget['fg'] = 'black'

def resetfield(e):
        if e.widget.get() == '':
            e.widget.insert(0, str(e.widget['text']))

            e.widget['fg'] = 'gray'
