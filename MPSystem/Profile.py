class Profile:
    def __init__(self,fields,data):
        self.info = {}
        self.heads = fields
        self.data = data
        for i in range(0,len(self.heads)):
            try:
                self.info[self.heads[i]] = self.data[i]
            except:
                self.info[self.heads[i]] = " "
