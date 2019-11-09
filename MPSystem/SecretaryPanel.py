from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
import tkinter
from  tkinter import messagebox
import datetime
import time

from System import System

class SecretaryPanel:
    def __init__(self,frame,width,height,scale,gui):
        self.allrecords = []
        self.photoimage = []
        self.frame = frame
        self.width = width
        self.height = height
        self.scale = scale
        self.gui = gui
        self.task = 0
        self.editprofile = None
        
    def setuppanels(self):
        self.secpanel = tkinter.PanedWindow(self.frame, bg="#EEEEEE")

        self.panel_left = tkinter.PanedWindow(self.secpanel, bg="#f5f5f5")
        self.panel_right = tkinter.PanedWindow(self.secpanel, bg="#EEEEEE")

        self.panel_left.place(x=0,y=0,width=int(self.width*self.scale*0.66),height=self.height*self.scale)
        self.panel_right.place(x=int(self.width*self.scale*0.66),y=0,width=int(self.width*self.scale*0.33),height=self.height*self.scale)

        imagepanel = tkinter.PanedWindow(self.panel_left, bg="#f5f5f5")
        imagepanel.place(x=0, y=0, width=int(self.width * self.scale * 0.66), height=64)


        logo = tkinter.PhotoImage(file="assets/images/jlplogo.png")
        logo_label = tkinter.Label(imagepanel,image=logo)
        logo_label.image = logo
        logo_label.place(x=0,y=0,width=128,height=64)

        minister = tkinter.PhotoImage(file="assets/images/minister.png")
        minister_label = tkinter.Label(imagepanel, image=minister)
        minister_label.image = minister
        minister_label.place(x=128, y=0, width=int(self.width*self.scale*0.66)-128, height=64)

        self.buttonpanel = tkinter.PanedWindow(self.panel_left, bg="white")
        self.buttonpanel.place(x=0, y=64, width=int(self.width * self.scale * 0.66), height=64)

        information_panel = tkinter.PanedWindow(self.panel_left,cursor="hand2",bg="blue")
        information_panel.place(x=0, y=100, width=int(self.width * self.scale * 0.66)-10, height=self.height*2-150)

        self.recordlist = tkinter.ttk.Treeview(information_panel,column=(),cursor="hand2", selectmode="extended",height=self.height*2-150)
        self.recordlist.grid(row=0,column=0,sticky='nsew')
        self.recordlist.heading('#0', text='Records')
        tkinter.ttk.Style().configure('Treeview',rowheight=40,relief='flat',borderwidth=0,bordercolor="blue")
        self.recordlist.place(x=0,y=0,width=int(self.width * self.scale * 0.66)-20,height=self.height*2-150)

        scrollbar = tkinter.Scrollbar(information_panel,cursor="hand2",orient="vertical", command=self.recordlist.yview)
        scrollbar.pack(side=tkinter.RIGHT ,fill=tkinter.Y)
        self.recordlist.configure(yscrollcommand=scrollbar.set)

        self.loadinglabel = tkinter.Label(self.panel_left,bg="#EEEEEE",text="100%",font="Arial 10 bold",fg="black")
        self.loadinglabel.place(x=5,y=self.height*2-30)

        addeditpanel = tkinter.PanedWindow(self.panel_right,bg="#EEEEEE")
        addeditpanel.place(x=5,y=self.height*self.scale-425,height=415,width=int(self.width*self.scale*0.33)-5)
        
        analysispanel = tkinter.ttk.Notebook(self.panel_right,cursor="hand2")
        tkinter.ttk.Style().layout("Tab",[('Notebook.tab', {'sticky': 'nswe', 'children':
                [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                [('Notebook.label', {'side': 'top', 'sticky': ''})],})],})])

        analysispanel.place(x=5,y=90,height=110,width=int(self.width*self.scale*0.33)-5)

        analysis1 = tkinter.PanedWindow(analysispanel,bg="#EEEEEE")
        analysis2 = tkinter.PanedWindow(analysispanel,bg="#EEEEEE")
        analysis3 = tkinter.PanedWindow(analysispanel,bg="#EEEEEE")

        self.getgraph(analysis1)
        self.setstats(analysis2)

        analysispanel.add(analysis1,text="Analysis \t\t\t\t")
        analysispanel.add(analysis2,text="Stats     \t\t\t\t")
        analysispanel.add(analysis3,text="Charts \t\t\t\t")
        

        profimages = tkinter.PhotoImage(file="assets/images/user3.png")
        proflabel = tkinter.Label(addeditpanel,image=profimages)
        proflabel.image = profimages
        proflabel.place(x=0,y=25,width=128,height=128)

        headingform = tkinter.Label(addeditpanel,bg="cyan",text="Add/Edit Profiles",font="Arial 14 bold",fg="black")
        headingform.place(x=0,y=0,width=int(self.width*self.scale*0.33)-5,height=25)

        self.edit_entries = []
        listin = 1
        skip = False

        titles = self.gettitleinfo()

        for l in range(len(titles)):
            format_head = titles[l]
            
            editform = tkinter.Label(addeditpanel,bg="#EEEEEE",text=format_head,font="Arial 9 bold",fg="black")
            editentry = tkinter.Entry(addeditpanel,bg="white",font="Arial 9 bold")
            
            self.edit_entries.append(editentry)

            if(l<4):
                editform.place(x=130,y=30*listin)
                editentry.place(x=220,y=30*listin,width=150) 
                listin = listin + 1   
            else:
                if len(format_head)>=16 or format_head=="Address" :
                    if skip:
                        listin = listin + 1
                    editform.place(x=0,y=30*listin)
                    editentry.place(x=130,y=30*listin,width=220)
                    listin = listin + 1
                    skip = False
                else:
                    if skip:
                        editform.place(x=170,y=30*listin)
                        editentry.place(x=250,y=30*listin,width=100)
                        listin = listin + 1
                        skip = False
                    else:
                        editform.place(x=0,y=30*listin)
                        editentry.place(x=70,y=30*listin,width=100)
                        skip = True

        do_usfunct = lambda: [self.recordlist.selection_remove(t) for t in self.recordlist.selection()] + [x.delete(0,"end") for x in self.edit_entries] and self.changeupdatebtn()
        self.addeditbutton = tkinter.Button(self.panel_right,bg="#EBEB00",text="Create Profile",command=self.addrecord)
        self.addeditbutton.place(x=0,y=self.height*self.scale-35)

        self.unselectbutton = tkinter.Button(self.panel_right,bg="#EEEEEE",text="Clear",relief="flat",fg="gray",cursor="hand2",command=do_usfunct)
        self.unselectbutton.place(x=100,y=self.height*self.scale-35)
                       

    def setupbuttons(self):
        do_etfunct = lambda: self.setedited(self.recordlist)
        edit_button = tkinter.Button(self.buttonpanel, text="Edit Profile",bg="#EBEB00",command=do_etfunct)
        edit_button.place(x=int(self.width * self.scale * 0.66)/5*2,y=0,width=int(self.width * self.scale * 0.66)/5)    

        do_hyfunct = lambda: self.placerecords(self.recordlist,"","history")
        history_button = tkinter.Button(self.buttonpanel, text="History",bg="#EBEB00",command=do_hyfunct)
        history_button.place(x=int(self.width * self.scale * 0.66)/5,y=0,width=int(self.width * self.scale * 0.66)/5)

        do_phfunct = lambda: self.pushselected(self.recordlist)
        push_button = tkinter.Button(self.buttonpanel,text="Push Record",bg="#EBEB00",command=do_phfunct)
        push_button.place(x=0,y=0,width=int(self.width * self.scale * 0.66)/5)

        do_dyfunct = lambda: self.placerecords(self.recordlist,"", "daily")
        daily_button = tkinter.Button(self.buttonpanel, text="Get Daily",bg="#EBEB00",command=do_dyfunct)
        daily_button.place(x=int(self.width * self.scale * 0.66)/5*4,y=0,width=int(self.width * self.scale * 0.66)/5)

        do_ldfunct = lambda: self.placerecords(self.recordlist,"","search")
        load_button = tkinter.Button(self.buttonpanel, text="Load Profiles",bg="#EBEB00",command=do_ldfunct)
        load_button.place(x=int(self.width * self.scale * 0.66)/5*3,y=0,width=int(self.width * self.scale * 0.66)/5)

        search = tkinter.PanedWindow(self.panel_right,bg="#EEEEEE")
        search.place(x=0,y=0,width=int(self.width*self.scale*0.33),height=64)

        searchlabel = tkinter.Label(search,bg="#EEEEEE",text="Search : ",font="Arial 12 bold",fg="black")
        searchlabel.place(x=18,y=20)

        searchbox = tkinter.Entry(search,bg="white",font="Arial 12 bold")
        searchbox.place(x=90,y=20,width=220)

        searchimage = tkinter.PhotoImage(file="assets/images/search.png")
        searchbutton = tkinter.Label(search,cursor="hand2",image=searchimage,bg="#EEEEEE")
        searchbutton.image = searchimage
        searchbutton.place(x=305,y=20)

        pfunct = lambda e: self.placerecords(self.recordlist,searchbox.get(),"search")
        searchbutton.bind('<Button-1>', pfunct)
        searchbox.bind('<Return>',pfunct)
        self.secpanel.pack(fill=tkinter.BOTH, expand=1)

        stopbutton = tkinter.Button(self.panel_left,bg="#EEEEEE",text="Stop",font="Arial 10 bold",fg="red",cursor="hand2",relief="flat",command=self.stoploop)
        stopbutton.place(x=int(self.width * self.scale * 0.66)-50,y=self.height*2-40)

        self.recordlist.bind("<Double-1>",lambda e: self.setedited(self.recordlist))
    
    def stoploop(self):self.task = 0
    def changeupdatebtn(self):
        self.addeditbutton["text"] = "Create Profile"
        self.addeditbutton["command"] = self.addrecord
        self.editprofile = None

    def setedited(self,p):
        if len(p.selection())!=0:
            [x.delete(0,"end") for x in self.edit_entries]
            editable = p.item(p.selection()[0])

            titles = self.gettitleinfo()

            for x in range(len(p.get_children())):
                    if editable == p.item(p.get_children()[x]):
                        for y in range(len(titles)):
                            self.edit_entries[y].insert(0,self.allrecords[x].info[titles[y]])
                            self.editprofile = self.allrecords[x]
                        break
            self.addeditbutton["text"] = "Update Profile"
            self.addeditbutton["command"] = self.updaterecord
        

    def showView(self):
        self.setuppanels()
        self.setupbuttons()
            
    def pushselected(self,p):
        for y in p.selection():
            for x in range(len(p.get_children())):
                if p.item(y) == p.item(p.get_children()[x]):
                    self.gui.system.pushdailyrecord(self.allrecords[x])
           
    def placerecords(self,p,keyword="",f="search"):
        try:
            [p.delete(x) for x in p.get_children()]
            [x.delete(0,"end") for x in self.edit_entries]
        except:
            pass

        self.allrecords = []
        rlist = []
        if f =="search":
            rlist = self.gui.system.searchrecords(keyword)
        elif f == "history":
            rlist = self.gui.system.loadhistory()
        else:
            rlist = self.gui.system.getdailyrecord(datetime.datetime.now().strftime("%Y-%m-%d"))

        siz = len(rlist)
        if len(rlist) == 0 or type(rlist[0]) != str:
            self.task = 1
            for x in range(0,siz):
                if(self.task==0):
                    siz = -1
                    break
                self.frame.update()
                time.sleep(0.1)
                self.addpane(p,x, rlist[x])
                self.loadinglabel["text"] = str(x+1)+"/"+str(siz)+" Loading... "+str(int((x+1)/siz*100))+"% "
                siz = len(rlist)
                try:
                    self.frame.update()
                    self.frame.update_idletasks()
                except:
                    exit()
        else:
            siz = 0
            messagebox.showinfo("System", "No Records")

        if siz>=0:
            self.loadinglabel["text"] = str(siz)+" Records"+" Loaded 100%"        
        self.task=0
        self.frame.update()
        self.frame.update_idletasks()
        

    def addpane(self,p,temp,info,display=["First Name","Last Name","Address","RRC Number","Occupation"]):
        label="\t"
        count=0
        self.photoimage.append(tkinter.PhotoImage(file="assets/images/user2.gif"))
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        for h in display:
            count=count+1
            label = label+ h +" : "+info.info[h]+" \t"
            if count % 3 ==0:
                label = label +"\t\t\t"+ '\n\t'
        p.insert('', 'end', text=label,image=self.photoimage[temp],value=())
        self.allrecords.append(info)
    
    def addrecord(self):
        ed  = len([x for x in self.edit_entries if x.get() !=""])
        if ed !=0:
            info = self.getsortedinfo()
            self.gui.system.createprofile(self.gui.system.heads,info)
            self.gui.system.loadprofiles()
            [x.delete(0,"end") for x in self.edit_entries]
            self.placerecords(self.recordlist,"","history")
            self.updatestates(self.statlabels,self.statentr)
            messagebox.showinfo("System", "Record Added")
        else:
            messagebox.showinfo("System", "No data")
        
    def updaterecord(self):
        info = self.getsortedinfo()
        self.gui.system.editprofile(self.editprofile,info,self.gui.system.heads)
        self.gui.system.loadprofiles()
        self.placerecords(self.recordlist,"","history")
        self.updatestates(self.statlabels,self.statentr)
        messagebox.showinfo("System", "Record Update")

    def getsortedinfo(self):
        titles = self.gettitleinfo()
        sortedds={}
        ds = dict(zip(titles,self.edit_entries))
        for x in self.gui.system.heads:
            sortedds[x] = ds[x].get()
        
        return list(sortedds.values())

    def getgraph(self,g):
        (v,x) = self.gui.system.getpoints()

        fig = Figure(figsize=(6,6))
        proj = fig.add_subplot(111)
        proj.scatter(v,x,color='green')
        proj.plot(v,x)
        proj.invert_yaxis()
        proj.set_ylabel("Visits", fontsize=7)
        proj.set_xlabel("Day", fontsize=7)
        proj.tick_params(labelsize=4)

        graphcanvas = FigureCanvasTkAgg(fig, master=g)
        graphcanvas.get_tk_widget().pack()
        graphcanvas.draw()
    
    def gettitleinfo(self):
        titles = self.gui.system.heads
        temp = titles[4:]
        temp.sort()
        return titles[:4] + temp 

    def setstats(self,g):
        s = self.gui.system.getstats()
        self.statlabels = []
        self.statentr = []

        p=0
        p2=1
        for k,v in s.items():
            lab = tkinter.Label(g,bg="#EEEEEE",text=str(k)+": ",font="Arial 10 bold",fg="black")
            en = tkinter.Label(g,bg="#EEEEEE",text=str(v),font="Arial 10 bold",fg="black")
            lab.place(x=2+p2,y=20*p)
            en.place(x=80+p2,y=20*p)
            self.statlabels.append(lab)
            self.statentr.append(en)
            p=p+1
            if p == 4:
                p=0
                p2=p2+150
    
    def updatestates(self,l,e):
        s = self.gui.system.getstats()
        for x in range(len(l)):
            e[x]["text"] = s["".join(l[x]["text"][:-2])]
