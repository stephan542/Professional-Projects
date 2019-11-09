import tkinter

class MainMenu:
        def __init__(self,frame,gui):
            self.frame = frame
            self.gui = gui

        def createmenu(self):
            menubar = tkinter.Menu(self.frame,bg="#D3D3D3")
            file_submenu = tkinter.Menu(menubar,tearoff = 0)
            help_submenu = tkinter.Menu(menubar,tearoff = 0)

            file_submenu.add_command(label="Create Profile",command=self.gui.nothing)
            file_submenu.add_separator()
            file_submenu.add_command(label="Exit", command=self.frame.quit)

            menubar.add_cascade(label="File",menu=file_submenu)
            menubar.add_cascade(label="Help", menu=help_submenu)

            return menubar
