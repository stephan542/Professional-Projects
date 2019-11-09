import tkinter
import tkinter.ttk
import datetime
import time

from Profile import Profile
from System import System
from MainMenu import MainMenu
from LoginPanel import loginPanel
from SecretaryPanel import SecretaryPanel

class GUI:
    def __init__(self,width=540,height=320,scale=2):
        self.width = width
        self.height = height
        self.scale = scale
        self.photoimage = []
        self.system = System()

        self.frame = self.createframe()
        self.menu = MainMenu(self.frame,self).createmenu()
        self.frame.config(menu=self.menu)
        SecretaryPanel(self.frame,self.width,self.height,self.scale,self).showView()
        #loginPanel(self.frame,self.width,self.height,self).showView()
        self.frame.mainloop()

    def createframe(self):
        self.title = "Constituency Management System"

        self.framedimension = str(self.width*self.scale)+"x"+str(self.height*self.scale)+"+0+0"

        frame = tkinter.Tk()
        tkinter.ttk.Style().theme_use("clam")
        
        frame.title(self.title)
        frame.geometry(self.framedimension)
        frame.minsize(width=self.width*self.scale,height=self.height*self.scale)
        frame.resizable(width=0,height=0)
    
        return frame


    def nothing(self):
        print("some action")
   
    def logout(self):
        [x.destroy() for x in self.frame.winfo_children()]
        loginPanel(self.frame,self.width,self.height,self).showView()


if __name__ == '__main__':
    #s = System.searchrecords(System,"jerome")[0]
    #for x in System.loadhistory(System):
    #   print(x.info)
    #a = datetime.datetime.now().strftime("%Y-%m-%d")
    #print([x.info for x in System.getdailyrecord(System,a)])
    #for x in System.searchrecords(System,"jerome"):
    #   print(x.info)
    #print(s.info)
    #print(System.editprofile(System,s,['Wilson'],['Last Name']).info)
    #print(System.pushdailyrecord(System,s))
    #for x in System.loadprofiles(System):
    #    print(x.info)
    #print(System.createprofile(None,['First Name','LastName','Address','Vote'],["Dean","Winchester","Manchester","PNP"]).info)
    gui = GUI()
