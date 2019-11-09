import tkinter
import tkinter.ttk
import csv
import datetime
import time
from Profile import Profile
from GUI import GUI



    def loginPanel(self):
        login = tkinter.PanedWindow(self.frame,bg="#228B22")

        panel_top =  tkinter.PanedWindow(login,bg="#228B22")
        panel_bottom = tkinter.PanedWindow(login, bg="white")

        mainlabel = tkinter.Label(panel_top,text="Constituency Management System",bg="#228B22",fg="white",font="sans-serif 20 bold")
        mainlabel.place(x=15, y=5, width=self.width * 2 + 5, height=120)

        background = tkinter.PhotoImage(file="backg.png")
        backgroundlabel = tkinter.Label(panel_bottom,image=background)
        backgroundlabel.image = background
        backgroundlabel.place(x=-5, y=-2, width=self.width * 2 + 10, height=self.height*2-120)

        sign_in = tkinter.PanedWindow(backgroundlabel, bg="white",sashwidth= 10)
        sign_in.place(x=self.width-int(self.width*0.51)/2, y=self.height-280, width=int(self.width*0.51)+int(self.width*0.1818), height=int(self.width*0.51)+int(self.width*0.1818))

        jlpimage = tkinter.PhotoImage(file="jlp.png")
        jlpimage_label = tkinter.Label(sign_in, image=jlpimage,bg="white")
        jlpimage_label.image = jlpimage
        jlpimage_label.place(x=0, y=0, width=int(self.width*0.51)+int(self.width*0.1818),height=200)

        forgotpassword = tkinter.Label(sign_in,text="Forgot Password?",font="Arial 7",fg="purple",bg="white")
        forgotpassword.place(x=-1, y=330,width=int(self.width*0.51)+int(self.width*0.1818),height=30)

        userimage = tkinter.PhotoImage(file="user.png",width=20,height=20)
        userimage_label = tkinter.Label(sign_in,image=userimage,bg="white")
        userimage_label.image=userimage
        userimage_label.place(x=0, y=200, width=32,height=32)

        lockimage = tkinter.PhotoImage(file="lock.png",width=20, height=20)
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
        funct = lambda e: self.authenicate(System.authenticate(user_name.get(),password.get()))
        loginbutton.bind('<ButtonPress-1>',funct)
        loginbutton.place(x=0, y=270,width=int(self.width*0.51)+int(self.width*0.1818))

        self.message_label = tkinter.Label(sign_in, text="",fg="red",bg="white")
        self.message_label.place(x=-1, y=300,width=int(self.width*0.51)+int(self.width*0.1818))

        clearmessage = lambda e: self.clear_message()
        password.bind('<Key>', clearmessage)
        user_name.bind('<Key>', clearmessage)

        password.bind('<ButtonPress-1>',GUI.clearfield)
        user_name.bind('<ButtonPress-1>', GUI.clearfield)

        forgotpassword.bind('<ButtonPress-1>', GUI.nothing)
        password.bind('<FocusOut>', GUI.resetfield)
        user_name.bind('<FocusOut>', GUI.resetfield)

        panel_top.place(x=-2, y=0, width=self.width * 2 + 10, height=120)
        panel_bottom.place(x=-2, y=120, width=self.width * 2 + 10, height=self.height*2-120)
        login.pack(fill=tkinter.BOTH,expand=1)

    def SecetaryPanel(self):
        self.allrecords = []
        secpanel = tkinter.PanedWindow(self.frame, bg="green")

        panel_left = tkinter.PanedWindow(secpanel, bg="#f5f5f5")
        panel_right = tkinter.PanedWindow(secpanel, bg="#228B22")

        panel_left.place(x=0,y=0,width=int(self.width*self.scale*0.66),height=self.height*self.scale)
        panel_right.place(x=int(self.width*self.scale*0.66),y=0,width=int(self.width*self.scale*0.33),height=self.height*self.scale)

        imagepanel = tkinter.PanedWindow(panel_left, bg="#f5f5f5")
        imagepanel.place(x=0, y=0, width=int(self.width * self.scale * 0.66), height=64)


        logo = tkinter.PhotoImage(file="jlplogo.png")
        logo_label = tkinter.Label(imagepanel,image=logo)
        logo_label.image = logo
        logo_label.place(x=0,y=0,width=128,height=64)

        minister = tkinter.PhotoImage(file="minister.png")
        minister_label = tkinter.Label(imagepanel, image=minister)
        minister_label.image = minister
        minister_label.place(x=128, y=0, width=int(self.width*self.scale*0.66)-128, height=64)

        buttonpanel = tkinter.PanedWindow(panel_left, bg="white")
        buttonpanel.place(x=0, y=64, width=int(self.width * self.scale * 0.66), height=64)
       

        edit_button = tkinter.Button(buttonpanel, text="Edit Profile",bg="yellow")
        edit_button.place(x=int(self.width * self.scale * 0.66)/5*2,y=0,width=int(self.width * self.scale * 0.66)/5)        

        information_panel = tkinter.PanedWindow(panel_left,cursor="hand2",bg="blue")
        information_panel.place(x=0, y=100, width=int(self.width * self.scale * 0.66)-10, height=self.height*2-150)


        recordlist = tkinter.ttk.Treeview(information_panel,column=(),cursor="hand2", selectmode="extended",height=self.height*2-150)
        recordlist.grid(row=0,column=0,sticky='nsew')
        recordlist.heading('#0', text='Records')
        tkinter.ttk.Style().configure('Treeview',rowheight=40,relief='flat',borderwidth=0,bordercolor="blue")
        recordlist.place(x=0,y=0,width=int(self.width * self.scale * 0.66)-20,height=self.height*2-150)

        scrollbar = tkinter.Scrollbar(information_panel,cursor="hand2",orient="vertical", command=recordlist.yview)
        scrollbar.pack(side=tkinter.RIGHT ,fill=tkinter.Y)
        recordlist.configure(yscrollcommand=scrollbar.set)

        do_hyfunct = lambda: self.placerecords(recordlist,"","history")
        history_button = tkinter.Button(buttonpanel, text="History",bg="yellow",command=do_hyfunct)
        history_button.place(x=int(self.width * self.scale * 0.66)/5,y=0,width=int(self.width * self.scale * 0.66)/5)

        do_phfunct = lambda: self.pushselected(recordlist)
        push_button = tkinter.Button(buttonpanel,text="Push Record",bg="yellow",command=do_phfunct)
        push_button.place(x=0,y=0,width=int(self.width * self.scale * 0.66)/5)

        do_dyfunct = lambda: self.placerecords(recordlist,"", "daily")
        daily_button = tkinter.Button(buttonpanel, text="Get Daily",bg="yellow",command=do_dyfunct)
        daily_button.place(x=int(self.width * self.scale * 0.66)/5*4,y=0,width=int(self.width * self.scale * 0.66)/5)

        load_button = tkinter.Button(buttonpanel, text="Load Profiles",bg="yellow")
        load_button.place(x=int(self.width * self.scale * 0.66)/5*3,y=0,width=int(self.width * self.scale * 0.66)/5)
        search = tkinter.PanedWindow(panel_right,bg="#228B22")
        search.place(x=0,y=0,width=int(self.width*self.scale*0.33),height=64)

        searchlabel = tkinter.Label(search,bg="#228B22",text="SEARCH : ",font="Arial 12 bold",fg="white")
        searchlabel.place(x=20,y=20)

        searchbox = tkinter.Entry(search,bg="white",font="Arial 12 bold")
        searchbox.place(x=120,y=20)

        searchimage = tkinter.PhotoImage(file="search.png")
        searchbutton = tkinter.Label(search,image=searchimage)
        searchbutton.image = searchimage
        searchbutton.place(x=305,y=20)

        pfunct = lambda e: self.placerecords(recordlist,searchbox.get(),"search")
        pfunct2 = lambda e: print(e)
        searchbutton.bind('<Button-1>', pfunct)
        searchbox.bind('<Key>',pfunct2)
        secpanel.pack(fill=tkinter.BOTH, expand=1)



    def pushselected(self,p):
        for y in p.selection():
            for x in range(len(p.get_children())):
                if p.item(y) == p.item(p.get_children()[x]):
                    self.system.pushdailyrecord(self.allrecords[x])
           
    def placerecords(self,p,keyword="",f="search"):
        try:
            [p.delete(x) for x in p.get_children()]
        except:
            pass

        self.allrecords = []
        rlist = []
        if f =="search":
            rlist = self.system.searchrecords(keyword)
        elif f == "history":
            rlist = self.system.loadhistory()
        else:
            rlist = self.system.getdailyrecord(datetime.datetime.now().strftime("%Y-%m-%d"))

        if type(rlist[0]) != str:
            for x in range(0,len(rlist)):
                self.frame.update()
                time.sleep(0.1)
                self.addpane(p,x, rlist[x])
                try:
                    self.frame.update()
                    self.frame.update_idletasks()
                except:
                    exit()
        

    def addpane(self,p,temp,info,display=["First Name","Last Name","Address","RRC Number","Occupation"]):
        label="\t"
        count=0;
        self.photoimage.append(tkinter.PhotoImage(file="user2.gif"))
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        for h in display:
            count=count+1
            label = label+ h +" : "+info.info[h]+" \t"
            if count % 3 ==0:
                label = label +"\t\t"+ '\n\t'
        p.insert('', 'end', text=label,image=self.photoimage[temp],value=())
        self.allrecords.append(info)

    def nothing(self):
        print("some action")

    def clear_message(self):
        self.message_label['text'] = ""

    def resetfield(e):
        if e.widget.get() == '':
            e.widget.insert(0, str(e.widget['text']))
            e.widget['fg'] = 'gray'

    def clearfield(e):
        e.widget.delete(0, 'end')
        e.widget['fg'] = 'black'

    def authenicate(self,value):
        print(value)
        if value == 1:
            [x.destroy() for x in self.frame.winfo_children()]
            self.SecetaryPanel()
        elif value == 0:
            [x.destroy() for x in self.frame.winfo_children()]
            self.MPPanel()
        elif value == -1:
            self.message_label['text'] = "Invalid Username"
        elif value == -2:
            self.message_label['text'] = "Invalid Password"
        else:
            print("Something when wrong with login in")

    def logout(self):
        [x.destroy() for x in self.frame.winfo_children()]
        self.loginPanel()

class System:
    def __init__(self):
        self.profiles = []
        self.heads = []
        self.profiles = self.loadprofiles()

    def loadprofiles(self):
        flag = False
        profiles = []
        try:
            with open('data.csv',newline='') as datafile:
                data = csv.reader(datafile)
                for row in data:
                    if flag == True :
                        if row[0] != '' and row[1] != '':
                            profile = Profile(self.heads,row)
                            profiles.append(profile)
                    else:
                        flag = True
                        self.heads = row

                self.profiles = profiles
                return profiles
            datafile.close()
        except:
            return "Data file not found"

    def createprofile(self,fields,info):
        try:
            profile = Profile(fields,info)
            with open('data.csv','a',newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerow(info)
            datafile.close()
            System.addtohistory(self,profile)
            return profile
        except:
            return "file not created"

    def addprofile(self,profile):
        try:
            with open('data.csv','a',newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerow(profile.info)
            datafile.close()
            System.addtohistory(self,profile)
        except:
            return "Could not add file"

    def editprofile(self,profile,info,fields=[]):
        if fields == []:
            fields = self.heads

        recordsearch = str("".join(profile.info.values())).lower()

        for d in range(0,len(fields)):
            profile.info[fields[d]] = info[d]

        alldata = System.loadprofiles(self)

        for d in range(0,len(alldata)):
            if str("".join(alldata[d].info.values())).lower() == recordsearch:
                alldata[d] = profile
                break

        try:
            with open('data.csv','w',newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerow(self.heads)
                for r in alldata:
                    writer.writerow(list(r.info.values()))

            datafile.close()
            System.addtohistory(self,profile)
            return profile
        except:
            return "file not updated"

    def pushdailyrecord(self,profile):
        currentdate = datetime.datetime.now()
        date = currentdate.strftime("%Y-%m-%d")
        filename = str(date)+".csv"
        try:
            with open(filename, 'a',newline='') as dailyrecords:
                writer = csv.writer(dailyrecords)
                writer.writerow(profile.data)
            dailyrecords.close()
            System.addtohistory(self,profile)
            return filename
        except:
            return "Could not add record"

    def getdailyrecord(self,date,fields=[]):
        if fields == []:
            fields = self.heads
        filename = str(date) + ".csv"
        records = []
        try:
            with open(filename, newline='') as recordfile:
                data = csv.reader(recordfile)

                for row in data:
                    records.append(Profile(fields,row))
                return records
            recordfile.close()
        except:
            return "Cannot get Daily Records"

    def searchrecords(self,search):
        try:
            data = self.profiles
            searchreults = []
            parsesearch = [str("".join(x.info.values())).lower() for x in data]
            search = search.lower()
            for parse in range(0,len(parsesearch)):
                if search in parsesearch[parse]:
                    searchreults.append(data[parse])

            return searchreults
        except:
            return "File not found"

    def addtohistory(self,profile):
        try:
            with open('history.csv','a',newline='') as history:
                writer = csv.writer(history)
                writer.writerow(profile.data)
            history.close()
        except:
            return "Unable to add to history"

    def loadhistory(self,fields=[]):
        if fields == []:
            fields = self.heads
        history = []
        try:
            with open('history.csv', newline='') as historyfile:
                data = csv.reader(historyfile)
                for row in data:
                    history.append(Profile(fields,row))
                historyfile.close()
                return history
            historyfile.close()
        except:
            return "No history file found"

    def authenticate(user_name,password):
        try:
            with open('logininfo.data', newline='') as loginfile:
                data = csv.reader(loginfile,delimiter=' ')
                for row in data:
                    if row[0] == user_name:
                        if row[1] == password:
                            loginfile.close()
                            if row[2] == 'mp':
                                return 1
                            else:
                                return 0
                        else:
                            return -2
            loginfile.close()
            return -1
        except:
            return  -3

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
