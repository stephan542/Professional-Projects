import csv
import datetime
import time

from Profile import Profile


class System:
    def __init__(self):
        self.profiles = []
        self.heads = []
        self.profiles = self.loadprofiles()

    def loadprofiles(self):
        flag = False
        profiles = []
        try:
            with open('assets/files/data.csv',newline='') as datafile:
                data = csv.reader(datafile)
                
                for row in data:
                    if flag == True :
                        if row[0] != '' and row[1] != '':
                            profile = Profile(self.heads,row)
                            profiles.append(profile)
                    else:
                        flag = True
                        if row[2] == "¿":
                            row[0] = row[0][3:]
                        self.heads = row
                
                self.profiles = profiles
                return profiles
            datafile.close()
        except:
            return "Data file not found"

    def createprofile(self,fields,info):
        try:
            profile = Profile(fields,info)
            with open('assets/files/data.csv','a',newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerow(info)
            datafile.close()
            self.addtohistory(profile)
            return profile
        except:
            return "file not created"

    def addprofile(self,profile):
        try:
            with open('assets/files/data.csv','a',newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerow(profile.info)
            datafile.close()
            self.addtohistory(profile)
        except:
            return "Could not add file"

    def editprofile(self,profile,info,fields=[]):
        if fields == []:
            fields = self.heads

        recordsearch = str("".join(profile.info.values())).lower()

        for d in range(0,len(fields)):
            profile.info[fields[d]] = info[d]
        
        profile.data = list(profile.info.values())
        alldata = self.loadprofiles()

        for d in range(0,len(alldata)):
            if str("".join(alldata[d].info.values())).lower() == recordsearch:
                alldata[d] = profile
                break

        try:
            with open('assets/files/data.csv','w',newline='') as datafile:
                writer = csv.writer(datafile)
                writer.writerow(self.heads)
                for r in alldata:
                    writer.writerow(list(r.info.values()))

            datafile.close()
            self.addtohistory(profile)
            return profile
        except:
            return "file not updated"

    def pushdailyrecord(self,profile):
        currentdate = datetime.datetime.now()
        date = currentdate.strftime("%Y-%m-%d")
        filename = "assets/files/"+str(date)+".csv"
        try:
            with open(filename, 'a',newline='') as dailyrecords:
                writer = csv.writer(dailyrecords)
                writer.writerow(profile.data)
            dailyrecords.close()
            self.addtohistory(profile)
            with open("assets/files/historicdata.csv", 'a',newline='') as historicfile:
                writer = csv.writer(historicfile)
                writer.writerow(["".join(date.split("/")),profile.data])
            historicfile.close()
            return filename
        except:
            return "Could not add record"

    def getdailyrecord(self,date,fields=[]):
        if fields == []:
            fields = self.heads
        filename = "assets/files/"+str(date) + ".csv"
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
            parsesearch = [str("".join([x for x in str("".join(x.info.values())).lower() if x!=" "])) for x in data]
            search = search.lower()
            search = "".join([x for x in search if x!=" "])
            for parse in range(0,len(parsesearch)):
                if search in parsesearch[parse]:
                    searchreults.append(data[parse])

            return searchreults
        except:
            return "File not found"

    def addtohistory(self,profile):
        try:
            with open('assets/files/history.csv','a',newline='') as history:
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
            with open('assets/files/history.csv', newline='') as historyfile:
                data = csv.reader(historyfile)
                for row in data:
                    history.append(Profile(fields,row))
                historyfile.close()
                return history
            historyfile.close()
        except:
            return "No history file found"

    def authenticate(self,user_name,password):
        try:
            with open('assets/files/logininfo.data', newline='') as loginfile:
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

    def getpoints(self):
        flag=False
        y={}
        try:
            with open('assets/files/historicdata.csv', newline='') as historicfile:
                data = csv.reader(historicfile)
                for row in data:
                   if flag:
                        y[row[0]] = y.get(row[0],0) + 1
                   else:
                        flag=True
            historicfile.close()
            return [list(y.keys()),list(y.values())]
        except:
            return ([],[])
    
    def getstats(self,s=["JLP","PNP","Dead"]):
        statistic = {}
        for t in s:
            statistic[t] = len([x for x in self.profiles if x.info["Canvas"].lower() == t.lower()])
        statistic["Other"] = len([x for x in self.profiles if x.info["Canvas"].lower() not in s] )
        return statistic